from time import sleep

import grpc
from grpc_services import sensors_pb2, sensors_pb2_grpc


def monitor():
    """
    Send request over grpc protocol and print the response
    """
    try:
        with grpc.insecure_channel("localhost:50051") as channel:
            stub = sensors_pb2_grpc.MonitoringStub(channel)
            response = stub.GasData(sensors_pb2.DataRequest())

        print(f"Monitoring client received:\n{response}")
        sleep(1)
        monitor()

    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    monitor()
