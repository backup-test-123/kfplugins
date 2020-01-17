package tfoperatorplugin

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

	"github.com/swiftdiaries/tfoperatorplugin/gen/pb-go/proto"
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
	tfJobReplicaSpecs := make(map[tfOp.TFReplicaType]*commonOp.ReplicaSpec)
	tfJobReplicaSpecs[tfOp.TFReplicaTypeWorker] = &commonOp.ReplicaSpec{
		Replicas:      tfJob.GetReplicas(),
		RestartPolicy: commonOp.RestartPolicyNever,
		Template:      v1.PodTemplateSpec{
			Spec: v1.PodSpec{
				Containers: []v1.Container{
					{
						Name: "tensorflow",
						Image: tfJob.GetImage(),
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
		},
	}
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
}

func init() {
	if err := tfOp.AddToScheme(scheme.Scheme); err != nil {
		panic(err)
	}
	pluginmachinery.PluginRegistry().RegisterK8sPlugin(
		k8s.PluginEntry{
			ID:                  tfJobTaskType,
			RegisteredTaskTypes: []pluginsCore.TaskType{tfJobTaskType},
			// TODO Type of the k8s resource, e.g. Pod
			ResourceToWatch: &tfOp.TFJob{},
			Plugin:          tfOperatorPlugin{},
			IsDefault:       false,
		})
}
