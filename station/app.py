from concurrent import futures

import grpc
from grpc_services import sensors_pb2_grpc
from grpc_services.services import Monitoring


def serve():
    """
    Listen for grpc transfer protocol over selected port
    """

    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sensors_pb2_grpc.add_MonitoringServicer_to_server(Monitoring(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()

    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
