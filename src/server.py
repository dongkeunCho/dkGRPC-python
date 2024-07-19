import grpc
import grpc_admin
from src.grpc import grpc_pb2
from src.grpc import grpc_pb2_grpc
from src.grpc.Id_Manager import Id_Manager
from concurrent import futures
import threading
from time import sleep
import logging

from grpc_health.v1 import health
from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc


logging.basicConfig(level=logging.INFO)


def _toggle_health(health_servicer: health.HealthServicer, service: str):
    next_status = health_pb2.HealthCheckResponse.SERVING
    while True:
        if next_status == health_pb2.HealthCheckResponse.SERVING:
            next_status = health_pb2.HealthCheckResponse.NOT_SERVING
        else:
            next_status = health_pb2.HealthCheckResponse.SERVING

        health_servicer.set(service, next_status)
        sleep(5)


def _configure_health_server(server: grpc.Server):
    health_servicer = health.HealthServicer(
        experimental_non_blocking=True,
        experimental_thread_pool=futures.ThreadPoolExecutor(max_workers=10),
    )
    health_pb2_grpc.add_HealthServicer_to_server(health_servicer, server)

    # Use a daemon thread to toggle health status
    toggle_health_status_thread = threading.Thread(
        target=_toggle_health,
        args=(health_servicer, "helloworld.Greeter"),
        daemon=True,
    )
    toggle_health_status_thread.start()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_pb2_grpc.add_Id_ManagerServicer_to_server(Id_Manager(), server)
    server.add_insecure_port("[::]:50051")
    grpc_admin.add_admin_servicers(server)
    _configure_health_server(server)
    server.start()
    server.wait_for_termination()
    

if __name__ =="__main__":
    serve()