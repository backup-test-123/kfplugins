module github.com/swiftdiaries/tfoperatorplugin

go 1.13

require (
	github.com/flyteorg/flytepluginexample v0.0.0-20191123001225-b713d77b78da
	github.com/golang/protobuf v1.3.2
	github.com/kubeflow/common v0.0.0-20200116014622-88a0cd071cf1
	github.com/kubeflow/tf-operator v0.5.3
	github.com/lyft/flyteplugins v0.2.2
	github.com/lyft/flytepropeller v0.1.13
	github.com/mitchellh/mapstructure v1.1.2
	github.com/pkg/errors v0.8.1
	github.com/spf13/pflag v1.0.5
	github.com/stretchr/testify v1.4.0
	k8s.io/api v0.0.0-20191031065753-b19d8caf39be
	k8s.io/apimachinery v0.0.0-20191030190112-bb31b70367b7
	sigs.k8s.io/controller-runtime v0.3.1-0.20191029211253-40070e2a1958
)

replace k8s.io/apimachinery v0.0.0 => github.com/lyft/apimachinery v0.0.0-20191031200210-047e3ea32d7f

replace k8s.io/api v0.0.0 => github.com/lyft/api v0.0.0-20191031200350-b49a72c274e0
