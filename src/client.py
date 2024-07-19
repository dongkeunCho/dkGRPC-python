import grpc
from src.grpc import grpc_pb2_grpc
from src.grpc import grpc_pb2
from src.grpc.Id_Manager import Id_Manager
from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc
from time import sleep

def health_check_call(stub: health_pb2_grpc.HealthStub):
    request = health_pb2.HealthCheckRequest(service="helloworld.Greeter")
    resp = stub.Check(request)
    if resp.status == health_pb2.HealthCheckResponse.SERVING:
        print("server is serving")
    elif resp.status == health_pb2.HealthCheckResponse.NOT_SERVING:
        print("server stopped serving")

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = grpc_pb2_grpc.Id_ManagerStub(channel)
        health_stub = health_pb2_grpc.HealthStub(channel)
        stub.setId(grpc_pb2.req(id="1001"))
        res = stub.getId(grpc_pb2.req(id=None))
        print(res.id)

        # Check health status every 1 second for 30 seconds
        for _ in range(30):
            health_check_call(health_stub)
            sleep(1)

    
    

if __name__ =="__main__":
    run()