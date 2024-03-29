# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import sensors_pb2 as sensors__pb2


class MonitoringStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GasData = channel.unary_unary(
            '/gas_sensor.Monitoring/GasData',
            request_serializer=sensors__pb2.DataRequest.SerializeToString,
            response_deserializer=sensors__pb2.DataResponse.FromString,
        )


class MonitoringServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GasData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MonitoringServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GasData': grpc.unary_unary_rpc_method_handler(
            servicer.GasData,
            request_deserializer=sensors__pb2.DataRequest.FromString,
            response_serializer=sensors__pb2.DataResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'gas_sensor.Monitoring', rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Monitoring(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GasData(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gas_sensor.Monitoring/GasData',
            sensors__pb2.DataRequest.SerializeToString,
            sensors__pb2.DataResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
