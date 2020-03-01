from __future__ import absolute_import

from flytekit.models import common as _common

from tfoperator.gen.pb_python import tfoperator_pb2 as _tf_task

class TFJob(_common.FlyteIdlEntity):

    def __init__(self, image, replicas, args, volumeClaimName):
        self.__image__ = image
        self.__replicas = replicas
        self.__args = args
        self.__volumeClaimName = volumeClaimName
    
    @property
    def image(self):
        return self.__image__

    @property
    def replicas(self):
        return self.__replicas

    @property
    def args(self):
        return self.__args
    
    @property
    def volumeClaimName(self):
        return self.__volumeClaimName
    
    def to_flyte_idl(self):
        return _tf_task.TFJob(
            image=self.image,
            replicas=self.replicas,
            args=self.args,
            volumeClaimName=self.volumeClaimName,
        )

    @classmethod
    def from_flyte_idl(cls, pb2_object):
        return cls(
            image=pb2_object.image,
            replicas=pb2_object.replicas,
            args=pb2_object.args,
            volumeClaimName=pb2_object.volumeClaimName,
        )
