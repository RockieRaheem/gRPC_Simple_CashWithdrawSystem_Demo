"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    0,
    '',
    'withdraw.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ewithdraw.proto\"5\n\x0fWithdrawRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x01\"I\n\x10WithdrawResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x13\n\x0bnew_balance\x18\x02 \x01(\x01\x12\x0f\n\x07message\x18\x03 \x01(\t2D\n\x0fWithdrawService\x12\x31\n\x08Withdraw\x12\x10.WithdrawRequest\x1a\x11.WithdrawResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'withdraw_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_WITHDRAWREQUEST']._serialized_start=18
  _globals['_WITHDRAWREQUEST']._serialized_end=71
  _globals['_WITHDRAWRESPONSE']._serialized_start=73
  _globals['_WITHDRAWRESPONSE']._serialized_end=146
  _globals['_WITHDRAWSERVICE']._serialized_start=148
  _globals['_WITHDRAWSERVICE']._serialized_end=216
# @@protoc_insertion_point(module_scope)
