.. _api_file_tfoperator.proto:

tfoperator.proto
================

.. _api_msg_flyte.plugins.tfoperator.TFOperatorPluginTask:

flyte.plugins.tfoperator.TFOperatorPluginTask
---------------------------------------------

`[flyte.plugins.tfoperator.TFOperatorPluginTask proto] <https://github.com/lyft/flyteidl/blob/master/protos/tfoperator.proto#L7>`_

Optional Proto for TFOperatorPlugin

.. code-block:: json

  {}




.. _api_msg_flyte.plugins.tfoperator.TFJob:

flyte.plugins.tfoperator.TFJob
------------------------------

`[flyte.plugins.tfoperator.TFJob proto] <https://github.com/lyft/flyteidl/blob/master/protos/tfoperator.proto#L11>`_

TODO(swiftdiaries):: add resource (CPUs, Memory) requirements and accelerator (GPU) requirements 

.. code-block:: json

  {
    "image": "...",
    "num_ps": "...",
    "replicas": "...",
    "command": "...",
    "args": "{...}",
    "volumeClaimName": "..."
  }

.. _api_field_flyte.plugins.tfoperator.TFJob.image:

image
  (`string <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_) 
  
.. _api_field_flyte.plugins.tfoperator.TFJob.num_ps:

num_ps
  (`int32 <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_) 
  
.. _api_field_flyte.plugins.tfoperator.TFJob.replicas:

replicas
  (`int32 <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_) 
  
.. _api_field_flyte.plugins.tfoperator.TFJob.command:

command
  (`string <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_) 
  
.. _api_field_flyte.plugins.tfoperator.TFJob.args:

args
  (map<`string <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_, `string <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_>) 
  
.. _api_field_flyte.plugins.tfoperator.TFJob.volumeClaimName:

volumeClaimName
  (`string <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_) 
  

