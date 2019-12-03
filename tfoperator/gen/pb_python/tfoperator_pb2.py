# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tfoperator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tfoperator.proto',
  package='flyte.plugins.tfoperator',
  syntax='proto3',
  serialized_pb=_b('\n\x10tfoperator.proto\x12\x18\x66lyte.plugins.tfoperator\"\x16\n\x14TFOperatorPluginTask\"#\n\rTFApplication\"\x12\n\x04Type\x12\n\n\x06PYTHON\x10\x00\"\xee\x01\n\x05TFJob\x12\x45\n\x0f\x61pplicationType\x18\x01 \x01(\x0e\x32,.flyte.plugins.tfoperator.TFApplication.Type\x12\r\n\x05image\x18\x02 \x01(\t\x12\x10\n\x08replicas\x18\x03 \x01(\x05\x12\x37\n\x04\x61rgs\x18\x04 \x03(\x0b\x32).flyte.plugins.tfoperator.TFJob.ArgsEntry\x12\x17\n\x0fvolumeClaimName\x18\x05 \x01(\t\x1a+\n\tArgsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x37Z5github.com/swiftdiaries/tfoperatorplugin/common/protob\x06proto3')
)



_TFAPPLICATION_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='flyte.plugins.tfoperator.TFApplication.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PYTHON', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=87,
  serialized_end=105,
)
_sym_db.RegisterEnumDescriptor(_TFAPPLICATION_TYPE)


_TFOPERATORPLUGINTASK = _descriptor.Descriptor(
  name='TFOperatorPluginTask',
  full_name='flyte.plugins.tfoperator.TFOperatorPluginTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=68,
)


_TFAPPLICATION = _descriptor.Descriptor(
  name='TFApplication',
  full_name='flyte.plugins.tfoperator.TFApplication',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TFAPPLICATION_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=105,
)


_TFJOB_ARGSENTRY = _descriptor.Descriptor(
  name='ArgsEntry',
  full_name='flyte.plugins.tfoperator.TFJob.ArgsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='flyte.plugins.tfoperator.TFJob.ArgsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='flyte.plugins.tfoperator.TFJob.ArgsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=303,
  serialized_end=346,
)

_TFJOB = _descriptor.Descriptor(
  name='TFJob',
  full_name='flyte.plugins.tfoperator.TFJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='applicationType', full_name='flyte.plugins.tfoperator.TFJob.applicationType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image', full_name='flyte.plugins.tfoperator.TFJob.image', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='replicas', full_name='flyte.plugins.tfoperator.TFJob.replicas', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='args', full_name='flyte.plugins.tfoperator.TFJob.args', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volumeClaimName', full_name='flyte.plugins.tfoperator.TFJob.volumeClaimName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TFJOB_ARGSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=346,
)

_TFAPPLICATION_TYPE.containing_type = _TFAPPLICATION
_TFJOB_ARGSENTRY.containing_type = _TFJOB
_TFJOB.fields_by_name['applicationType'].enum_type = _TFAPPLICATION_TYPE
_TFJOB.fields_by_name['args'].message_type = _TFJOB_ARGSENTRY
DESCRIPTOR.message_types_by_name['TFOperatorPluginTask'] = _TFOPERATORPLUGINTASK
DESCRIPTOR.message_types_by_name['TFApplication'] = _TFAPPLICATION
DESCRIPTOR.message_types_by_name['TFJob'] = _TFJOB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TFOperatorPluginTask = _reflection.GeneratedProtocolMessageType('TFOperatorPluginTask', (_message.Message,), dict(
  DESCRIPTOR = _TFOPERATORPLUGINTASK,
  __module__ = 'tfoperator_pb2'
  # @@protoc_insertion_point(class_scope:flyte.plugins.tfoperator.TFOperatorPluginTask)
  ))
_sym_db.RegisterMessage(TFOperatorPluginTask)

TFApplication = _reflection.GeneratedProtocolMessageType('TFApplication', (_message.Message,), dict(
  DESCRIPTOR = _TFAPPLICATION,
  __module__ = 'tfoperator_pb2'
  # @@protoc_insertion_point(class_scope:flyte.plugins.tfoperator.TFApplication)
  ))
_sym_db.RegisterMessage(TFApplication)

TFJob = _reflection.GeneratedProtocolMessageType('TFJob', (_message.Message,), dict(

  ArgsEntry = _reflection.GeneratedProtocolMessageType('ArgsEntry', (_message.Message,), dict(
    DESCRIPTOR = _TFJOB_ARGSENTRY,
    __module__ = 'tfoperator_pb2'
    # @@protoc_insertion_point(class_scope:flyte.plugins.tfoperator.TFJob.ArgsEntry)
    ))
  ,
  DESCRIPTOR = _TFJOB,
  __module__ = 'tfoperator_pb2'
  # @@protoc_insertion_point(class_scope:flyte.plugins.tfoperator.TFJob)
  ))
_sym_db.RegisterMessage(TFJob)
_sym_db.RegisterMessage(TFJob.ArgsEntry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z5github.com/swiftdiaries/tfoperatorplugin/common/proto'))
_TFJOB_ARGSENTRY.has_options = True
_TFJOB_ARGSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)