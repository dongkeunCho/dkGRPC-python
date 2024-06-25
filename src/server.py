import grpc
from src.grpc import grpc_pb2_grpc
from src.grpc.Id_Manager import Id_Manager
from concurrent import futures
import logging

logging.basicConfig(level=logging.INFO)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_pb2_grpc.add_Id_ManagerServicer_to_server(Id_Manager(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()
    

if __name__ =="__main__":
    serve()