import json

from rabbit import QueueConsumer

from . import sensors_pb2, sensors_pb2_grpc


class Monitoring(sensors_pb2_grpc.MonitoringServicer):
    """
    Override abstract layer to prevent NotImplementError and
    define grpc response
    """

    def GasData(self, request, context):
        queue_data = QueueConsumer().consume()

        if queue_data:
            data_dict = json.loads(queue_data)
            return sensors_pb2.DataResponse(
                sensor_id=data_dict['sensor_id'],
                gas_type=data_dict['gas_type'],
                value=data_dict['value'],
                timestamp=data_dict['timestamp'],
            )

        return sensors_pb2.DataResponse()
