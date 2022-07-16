# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: histogram.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='histogram.proto',
  package='histogram',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0fhistogram.proto\x12\thistogram\"<\n\x0fHistogram2DList\x12)\n\thistogram\x18\x01 \x03(\x0b\x32\x16.histogram.Histogram2D\"\x82\x01\n\x0bHistogram2D\x12\x10\n\x04\x64\x61ta\x18\x01 \x03(\x05\x42\x02\x10\x01\x12\x1e\n\x05xbins\x18\x02 \x01(\x0b\x32\x0f.histogram.Bins\x12\x1e\n\x05ybins\x18\x03 \x01(\x0b\x32\x0f.histogram.Bins\x12!\n\x04meta\x18\x04 \x03(\x0b\x32\x13.histogram.MetaPair\"\x18\n\x04\x42ins\x12\x10\n\x04\x62ins\x18\x01 \x03(\x01\x42\x02\x10\x01\"&\n\x08MetaPair\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\xc2\x01\n\x0bHistogram4D\x12\x10\n\x04\x64\x61ta\x18\x01 \x03(\x05\x42\x02\x10\x01\x12\x1e\n\x05xbins\x18\x02 \x01(\x0b\x32\x0f.histogram.Bins\x12\x1e\n\x05ybins\x18\x03 \x01(\x0b\x32\x0f.histogram.Bins\x12\x1e\n\x05zbins\x18\x04 \x01(\x0b\x32\x0f.histogram.Bins\x12\x1e\n\x05tbins\x18\x05 \x01(\x0b\x32\x0f.histogram.Bins\x12!\n\x04meta\x18\x06 \x03(\x0b\x32\x13.histogram.MetaPair\":\n\x0bUniformBins\x12\x0e\n\x06number\x18\x01 \x01(\x05\x12\x0c\n\x04left\x18\x02 \x01(\x01\x12\r\n\x05right\x18\x03 \x01(\x01\"L\n\x12UniformHistogram1D\x12$\n\x04\x62ins\x18\x01 \x01(\x0b\x32\x16.histogram.UniformBins\x12\x10\n\x04\x64\x61ta\x18\x02 \x03(\x05\x42\x02\x10\x01\x62\x06proto3'
)




_HISTOGRAM2DLIST = _descriptor.Descriptor(
  name='Histogram2DList',
  full_name='histogram.Histogram2DList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='histogram', full_name='histogram.Histogram2DList.histogram', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=90,
)


_HISTOGRAM2D = _descriptor.Descriptor(
  name='Histogram2D',
  full_name='histogram.Histogram2D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='histogram.Histogram2D.data', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xbins', full_name='histogram.Histogram2D.xbins', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ybins', full_name='histogram.Histogram2D.ybins', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meta', full_name='histogram.Histogram2D.meta', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=223,
)


_BINS = _descriptor.Descriptor(
  name='Bins',
  full_name='histogram.Bins',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bins', full_name='histogram.Bins.bins', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=225,
  serialized_end=249,
)


_METAPAIR = _descriptor.Descriptor(
  name='MetaPair',
  full_name='histogram.MetaPair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='histogram.MetaPair.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='histogram.MetaPair.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=251,
  serialized_end=289,
)


_HISTOGRAM4D = _descriptor.Descriptor(
  name='Histogram4D',
  full_name='histogram.Histogram4D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='histogram.Histogram4D.data', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xbins', full_name='histogram.Histogram4D.xbins', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ybins', full_name='histogram.Histogram4D.ybins', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zbins', full_name='histogram.Histogram4D.zbins', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tbins', full_name='histogram.Histogram4D.tbins', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meta', full_name='histogram.Histogram4D.meta', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=292,
  serialized_end=486,
)


_UNIFORMBINS = _descriptor.Descriptor(
  name='UniformBins',
  full_name='histogram.UniformBins',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='histogram.UniformBins.number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left', full_name='histogram.UniformBins.left', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right', full_name='histogram.UniformBins.right', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=488,
  serialized_end=546,
)


_UNIFORMHISTOGRAM1D = _descriptor.Descriptor(
  name='UniformHistogram1D',
  full_name='histogram.UniformHistogram1D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bins', full_name='histogram.UniformHistogram1D.bins', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='histogram.UniformHistogram1D.data', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=548,
  serialized_end=624,
)

_HISTOGRAM2DLIST.fields_by_name['histogram'].message_type = _HISTOGRAM2D
_HISTOGRAM2D.fields_by_name['xbins'].message_type = _BINS
_HISTOGRAM2D.fields_by_name['ybins'].message_type = _BINS
_HISTOGRAM2D.fields_by_name['meta'].message_type = _METAPAIR
_HISTOGRAM4D.fields_by_name['xbins'].message_type = _BINS
_HISTOGRAM4D.fields_by_name['ybins'].message_type = _BINS
_HISTOGRAM4D.fields_by_name['zbins'].message_type = _BINS
_HISTOGRAM4D.fields_by_name['tbins'].message_type = _BINS
_HISTOGRAM4D.fields_by_name['meta'].message_type = _METAPAIR
_UNIFORMHISTOGRAM1D.fields_by_name['bins'].message_type = _UNIFORMBINS
DESCRIPTOR.message_types_by_name['Histogram2DList'] = _HISTOGRAM2DLIST
DESCRIPTOR.message_types_by_name['Histogram2D'] = _HISTOGRAM2D
DESCRIPTOR.message_types_by_name['Bins'] = _BINS
DESCRIPTOR.message_types_by_name['MetaPair'] = _METAPAIR
DESCRIPTOR.message_types_by_name['Histogram4D'] = _HISTOGRAM4D
DESCRIPTOR.message_types_by_name['UniformBins'] = _UNIFORMBINS
DESCRIPTOR.message_types_by_name['UniformHistogram1D'] = _UNIFORMHISTOGRAM1D
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Histogram2DList = _reflection.GeneratedProtocolMessageType('Histogram2DList', (_message.Message,), {
  'DESCRIPTOR' : _HISTOGRAM2DLIST,
  '__module__' : 'histogram_pb2'
  # @@protoc_insertion_point(class_scope:histogram.Histogram2DList)
  })
_sym_db.RegisterMessage(Histogram2DList)

Histogram2D = _reflection.GeneratedProtocolMessageType('Histogram2D', (_message.Message,), {
  'DESCRIPTOR' : _HISTOGRAM2D,
  '__module__' : 'histogram_pb2'
  # @@protoc_insertion_point(class_scope:histogram.Histogram2D)
  })
_sym_db.RegisterMessage(Histogram2D)

Bins = _reflection.GeneratedProtocolMessageType('Bins', (_message.Message,), {
  'DESCRIPTOR' : _BINS,
  '__module__' : 'histogram_pb2'
  # @@protoc_insertion_point(class_scope:histogram.Bins)
  })
_sym_db.RegisterMessage(Bins)

MetaPair = _reflection.GeneratedProtocolMessageType('MetaPair', (_message.Message,), {
  'DESCRIPTOR' : _METAPAIR,
  '__module__' : 'histogram_pb2'
  # @@protoc_insertion_point(class_scope:histogram.MetaPair)
  })
_sym_db.RegisterMessage(MetaPair)

Histogram4D = _reflection.GeneratedProtocolMessageType('Histogram4D', (_message.Message,), {
  'DESCRIPTOR' : _HISTOGRAM4D,
  '__module__' : 'histogram_pb2'
  # @@protoc_insertion_point(class_scope:histogram.Histogram4D)
  })
_sym_db.RegisterMessage(Histogram4D)

UniformBins = _reflection.GeneratedProtocolMessageType('UniformBins', (_message.Message,), {
  'DESCRIPTOR' : _UNIFORMBINS,
  '__module__' : 'histogram_pb2'
  # @@protoc_insertion_point(class_scope:histogram.UniformBins)
  })
_sym_db.RegisterMessage(UniformBins)

UniformHistogram1D = _reflection.GeneratedProtocolMessageType('UniformHistogram1D', (_message.Message,), {
  'DESCRIPTOR' : _UNIFORMHISTOGRAM1D,
  '__module__' : 'histogram_pb2'
  # @@protoc_insertion_point(class_scope:histogram.UniformHistogram1D)
  })
_sym_db.RegisterMessage(UniformHistogram1D)


_HISTOGRAM2D.fields_by_name['data']._options = None
_BINS.fields_by_name['bins']._options = None
_HISTOGRAM4D.fields_by_name['data']._options = None
_UNIFORMHISTOGRAM1D.fields_by_name['data']._options = None
# @@protoc_insertion_point(module_scope)
