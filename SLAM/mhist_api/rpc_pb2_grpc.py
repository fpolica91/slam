# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import rpc_pb2 as rpc__pb2


class MhistStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Store = channel.unary_unary(
        '/proto.Mhist/Store',
        request_serializer=rpc__pb2.MeasurementMessage.SerializeToString,
        response_deserializer=rpc__pb2.Nothing.FromString,
        )
    self.StoreStream = channel.stream_unary(
        '/proto.Mhist/StoreStream',
        request_serializer=rpc__pb2.MeasurementMessage.SerializeToString,
        response_deserializer=rpc__pb2.Nothing.FromString,
        )
    self.Retrieve = channel.unary_unary(
        '/proto.Mhist/Retrieve',
        request_serializer=rpc__pb2.RetrieveRequest.SerializeToString,
        response_deserializer=rpc__pb2.RetrieveResponse.FromString,
        )
    self.Subscribe = channel.unary_stream(
        '/proto.Mhist/Subscribe',
        request_serializer=rpc__pb2.Filter.SerializeToString,
        response_deserializer=rpc__pb2.MeasurementMessage.FromString,
        )


class MhistServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Store(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StoreStream(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Retrieve(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Subscribe(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MhistServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Store': grpc.unary_unary_rpc_method_handler(
          servicer.Store,
          request_deserializer=rpc__pb2.MeasurementMessage.FromString,
          response_serializer=rpc__pb2.Nothing.SerializeToString,
      ),
      'StoreStream': grpc.stream_unary_rpc_method_handler(
          servicer.StoreStream,
          request_deserializer=rpc__pb2.MeasurementMessage.FromString,
          response_serializer=rpc__pb2.Nothing.SerializeToString,
      ),
      'Retrieve': grpc.unary_unary_rpc_method_handler(
          servicer.Retrieve,
          request_deserializer=rpc__pb2.RetrieveRequest.FromString,
          response_serializer=rpc__pb2.RetrieveResponse.SerializeToString,
      ),
      'Subscribe': grpc.unary_stream_rpc_method_handler(
          servicer.Subscribe,
          request_deserializer=rpc__pb2.Filter.FromString,
          response_serializer=rpc__pb2.MeasurementMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'proto.Mhist', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
