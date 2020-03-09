from __future__ import absolute_import

from flytekit.models import common as _common

from gen.pb_python import tfoperator_pb2 as _tf_task

class TFJob(_common.FlyteIdlEntity):

    def __init__(self, image, num_ps, replicas, command, args, volumeClaimName):
        self._image = image
        self._num_ps = num_ps
        self._replicas = replicas
        self._command = command
        self._args = args
        self._volumeClaimName = volumeClaimName
    
    @property
    def image(self):
        return self._image

    @property
    def num_ps(self):
        return self._num_ps
    
    @property
    def replicas(self):
        return self._replicas

    @property
    def command(self):
        return self._command

    @property
    def args(self):
        return self._args
    
    @property
    def volumeClaimName(self):
        return self._volumeClaimName
    
    def to_flyte_idl(self):
        return _tf_task.TFJob(
            image=self.image,
            num_ps=self.num_ps,
            replicas=self.replicas,
            command=self.command,
            args=self.args,
            volumeClaimName=self.volumeClaimName,
        )

    @classmethod
    def from_flyte_idl(cls, pb2_object):
        return cls(
            image=pb2_object.image,
            num_ps=pb2_object.num_ps,
            replicas=pb2_object.replicas,
            command=pb2_object.command,
            args=pb2_object.args,
            volumeClaimName=pb2_object.volumeClaimName,
        )
