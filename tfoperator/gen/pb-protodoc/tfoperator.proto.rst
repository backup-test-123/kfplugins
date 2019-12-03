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




.. _api_msg_flyte.plugins.tfoperator.TFApplication:

flyte.plugins.tfoperator.TFApplication
--------------------------------------

`[flyte.plugins.tfoperator.TFApplication proto] <https://github.com/lyft/flyteidl/blob/master/protos/tfoperator.proto#L14>`_


.. code-block:: json

  {}



.. _api_enum_flyte.plugins.tfoperator.TFApplication.Type:

Enum flyte.plugins.tfoperator.TFApplication.Type
------------------------------------------------

`[flyte.plugins.tfoperator.TFApplication.Type proto] <https://github.com/lyft/flyteidl/blob/master/protos/tfoperator.proto#L15>`_


.. _api_enum_value_flyte.plugins.tfoperator.TFApplication.Type.PYTHON:

PYTHON
  *(DEFAULT)* ⁣
  

.. _api_msg_flyte.plugins.tfoperator.TFJob:

flyte.plugins.tfoperator.TFJob
------------------------------

`[flyte.plugins.tfoperator.TFJob proto] <https://github.com/lyft/flyteidl/blob/master/protos/tfoperator.proto#L20>`_


.. code-block:: json

  {
    "applicationType": "...",
    "image": "...",
    "replicas": "...",
    "args": "{...}",
    "volumeClaimName": "..."
  }

.. _api_field_flyte.plugins.tfoperator.TFJob.applicationType:

applicationType
  (:ref:`flyte.plugins.tfoperator.TFApplication.Type <api_enum_flyte.plugins.tfoperator.TFApplication.Type>`) 
  
.. _api_field_flyte.plugins.tfoperator.TFJob.image:

image
  (`string <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_) 
  
.. _api_field_flyte.plugins.tfoperator.TFJob.replicas:

replicas
  (`int32 <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_) 
  
.. _api_field_flyte.plugins.tfoperator.TFJob.args:

args
  (map<`string <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_, `string <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_>) 
  
.. _api_field_flyte.plugins.tfoperator.TFJob.volumeClaimName:

volumeClaimName
  (`string <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_) 
  

