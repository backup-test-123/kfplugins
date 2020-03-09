import json
import os
import sys
from tfoperatorplugin.sdk.tasks import tfjob_task
from flytekit.sdk.workflow import workflow_class
from flytekit.sdk.types import Types
from flytekit.configuration import TemporaryConfiguration

mnist_trainer_args = dict()
@tfjob_task.tf_job_task(
    image='ciscoai/mnist:3088D0CF',
    num_ps=1,
    replicas=2,
    command='python /opt/model.py',
    args=mnist_trainer_args,
    volumeClaimName='mnist-trainer-claim')
def mnist_trainer():
    pass

@workflow_class
class DemoWorkflow(object):
    mnist_task = mnist_trainer()

if __name__ == '__main__':
    _PROJECT = 'demo'
    _DOMAIN = 'development'
    _USAGE = "Usage:\n\n" \
             "\tpython sample.py render_task\n" \
             "\tpython sample.py execute <version> <train data path> <validation data path> <hyperparameter json>\n"

    with TemporaryConfiguration(
            os.path.join(os.path.dirname(__file__), "flyte.config")):
        if sys.argv[1] == 'render_task':
            DemoWorkflow.validate()
        else:
            print(_USAGE)
