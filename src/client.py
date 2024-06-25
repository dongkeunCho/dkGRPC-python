import grpc
from src.grpc import grpc_pb2_grpc
from src.grpc import grpc_pb2
from src.grpc.Id_Manager import Id_Manager
def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = grpc_pb2_grpc.Id_ManagerStub(channel)
        stub.setId(grpc_pb2.req(id="1001"))

        stub = grpc_pb2_grpc.Id_ManagerStub(channel)
        res = stub.getId(grpc_pb2.req(id=None))
        print(res.id)
    

if __name__ =="__main__":
    run()