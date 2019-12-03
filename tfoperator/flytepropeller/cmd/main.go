package main

import (
	_ "github.com/flyteorg/flytepluginexample/go/exampleplugin"
	_ "github.com/lyft/flyteplugins/go/tasks/plugins/k8s/container"
	_ "github.com/lyft/flyteplugins/go/tasks/plugins/k8s/sidecar"
	"github.com/lyft/flytepropeller/cmd/controller/cmd"
)

func main() {
	cmd.Execute()
}
