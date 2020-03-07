package tfplugin

import (
	"context"

	"github.com/lyft/flyteplugins/go/tasks/pluginmachinery"
	"github.com/lyft/flyteplugins/go/tasks/pluginmachinery/flytek8s"
	"github.com/lyft/flyteplugins/go/tasks/pluginmachinery/flytek8s/config"

	"github.com/pkg/errors"
	v1 "k8s.io/api/core/v1"

	pluginsCore "github.com/lyft/flyteplugins/go/tasks/pluginmachinery/core"
	"github.com/lyft/flyteplugins/go/tasks/pluginmachinery/k8s"
	"github.com/lyft/flyteplugins/go/tasks/pluginmachinery/utils"

	commonOp "github.com/kubeflow/common/job_controller/api/v1"
	tfOp "github.com/kubeflow/tf-operator/pkg/apis/tensorflow/v1"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"

	"github.com/flyteorg/kfplugins/tfoperator/gen/pb-go/proto"
)

const (
	//KindTFJob holds the Kind for a TFJob. It is used repeatedly throughout the plugin code
	KindTfJob     = "TFJob"
	pluginID      = "tfjob"
	tfJobTaskType = "tfjob"
)

// Sanity test that the plugin implements method of k8s.Plugin
var _ k8s.Plugin = tfOperatorPlugin{}

type tfOperatorPlugin struct {
	TfJobName string
	TfJob     tfOp.TFJob
}

func (m tfOperatorPlugin) BuildIdentityResource(ctx context.Context, taskCtx pluginsCore.TaskExecutionMetadata) (k8s.Resource, error) {
	return &tfOp.TFJob{
		TypeMeta: metav1.TypeMeta{
			Kind:       KindTfJob,
			APIVersion: tfOp.SchemeGroupVersion.String(),
		},
	}, nil
}

func (m tfOperatorPlugin) BuildResource(ctx context.Context, taskCtx pluginsCore.TaskExecutionContext) (k8s.Resource, error) {
	taskTemplate, err := taskCtx.TaskReader().Read(ctx)
	if err != nil {
		return nil, errors.Wrapf(err, "unable to fetch task specification")
	} else if taskTemplate == nil {
		return nil, errors.Errorf("nil task specification")
	}

	tfJob := proto.TFJob{}
	err = utils.UnmarshalStruct(taskTemplate.GetCustom(), &tfJob)
	if err != nil {
		return nil, errors.Wrapf(err, "invalid task specification for taskType [%s]", tfJobTaskType)
	}

	// Check if volume claim exists and create one if it doesn't
	// tfJobVolumeClaim := tfJob.GetVolumeClaimName()

	// annotations := utils.UnionMaps(config.GetK8sPluginConfig().DefaultAnnotations, utils.CopyMap(taskCtx.TaskExecutionMetadata().GetAnnotations()))
	// labels := utils.UnionMaps(config.GetK8sPluginConfig().DefaultLabels, utils.CopyMap(taskCtx.TaskExecutionMetadata().GetLabels()))
	// // If the container is part of the task template you can access it here
	container := taskTemplate.GetContainer()

	// When adding env vars there are some default env vars that are available, you can pass them through
	envVars := flytek8s.DecorateEnvVars(ctx, flytek8s.ToK8sEnvVar(container.GetEnv()), taskCtx.TaskExecutionMetadata().GetTaskExecutionID())
	tfJobEnvVars := make(map[string]string)
	for _, envVar := range envVars {
		tfJobEnvVars[envVar.Name] = envVar.Value
	}

	// common Pod Spec Template that maps into the TF Job ReplicaSpecs for - PS, Chief, Worker
	commonPodSpecTemplate := v1.PodTemplateSpec{
		Spec: v1.PodSpec{
			Containers: []v1.Container{
				{
					Name: "tensorflow",
					Image: tfJob.GetImage(),
					Command: tfJob.GetCommand(),
					EnvVars: tfJobEnvVars,
					Args: tfJob.GetArgs(),
					VolumeMounts: []v1.VolumeMount{
						Name: "tfjob-volume",
						MountPath: "/mnt/data",
					}
				}
			},
			Volumes: []v1.Volume{
				{
					Name: "tfjob-volume",
					VolumeSource: v1.VolumeSource{
						PersistentVolumeClaim: v1.PersistentVolumeClaimVolumeSource{
							ClaimName: tfJob.GetVolumeClaimName(),
							ReadOnly: false,
						},
					},
				},
			},
		},
	}

	tfJobReplicaSpecs := make(map[tfOp.TFReplicaType]*commonOp.ReplicaSpec)

	// Adds Parameter Server spec
	tfJobReplicaSpecs[tfOp.TFReplicaTypePS] = &commonOp.ReplicaSpec{
		Replicas:      tfJob.GetNumPs(),
		RestartPolicy: commonOp.RestartPolicyNever,
		Template:   commonPodSpecTemplate,   
	}
	// Adds Chief spec
	tfJobReplicaSpecs[tfOp.TFReplicaTypeChief] = &commonOp.ReplicaSpec{
		Replicas:      tfJob.GetReplicas(),
		RestartPolicy: commonOp.RestartPolicyNever,
		Template:   commonPodSpecTemplate,   
	}
	// Adds worker spec
	tfJobReplicaSpecs[tfOp.TFReplicaTypeWorker] = &commonOp.ReplicaSpec{
		Replicas:      tfJob.GetReplicas(),
		RestartPolicy: commonOp.RestartPolicyNever,
		Template:   commonPodSpecTemplate,   
	}

	// Combine everything into the TF Job Spec
	job := &tfOp.TFJob{
		TypeMeta: metav1.TypeMeta{
			Kind:       KindTfJob,
			APIVersion: tfOp.SchemeGroupVersion.String(),
		},
		Spec: tfOp.TFJobSpec{
			TFReplicaSpecs: tfJobReplicaSpecs,
		},
	}

	return job, nil
}

func getEventInfoForTFJob(tfjob *tfOp.TFJob) (*pluginsCore.TaskInfo, error) {
	// TODO(swiftdiaries): Get Logs and TFJob Status
	return nil, nil
}

func (m tfOperatorPlugin) GetTaskPhase(ctx context.Context, pluginContext k8s.PluginContext, resource k8s.Resource) (pluginsCore.PhaseInfo, error) {
	app := resource.(*tfOp.TFJob)
	info, err := getEventInfoForTFJob(app)
	if err != nil {
		return pluginsCore.PhaseInfoUndefined, err
	}

	occurredAt := time.Now()
	for _, condition := range app.Status.Conditions {
		if hasCondition(app.Status, commonOp.JobSucceeded) {
			return pluginsCore.PhaseInfoSuccess(info), nil
		} else if hasCondition(app.Status, commonOp.JobRunning) {
			return pluginsCore.PhaseInfoRunning(info), nil
		} else if hasConiditon(app.Status, commonOp.JobFailed) {
			return pluginsCore.PhaseInfoFailure(500, "Internal Failure", info)
		}
	}
}

func hasCondition(status commonOp.JobStatus, conditionType commonOp.JobConditionType) bool {
	for _, condition := range status.Conditions {
		if condition.Type == conditionType && condition.Status == v1.ConditionTrue {
			return true
		}
	}
	return false
}

func init() {
	if err := tfOp.AddToScheme(scheme.Scheme); err != nil {
		panic(err)
	}
	pluginmachinery.PluginRegistry().RegisterK8sPlugin(
		k8s.PluginEntry{
			ID:                  tfJobTaskType,
			RegisteredTaskTypes: []pluginsCore.TaskType{tfJobTaskType},
			ResourceToWatch: &tfOp.TFJob{},
			Plugin:          tfOperatorPlugin{},
			IsDefault:       false,
		})
}
