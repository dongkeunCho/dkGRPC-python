import json
from src.grpc import grpc_pb2_grpc
from src.grpc import grpc_pb2

class Id_Manager(grpc_pb2_grpc.Id_ManagerServicer):
    def __init__(self):
        self.id = "None"

    def setId(self, request, context):
        self.id = request.id
        return grpc_pb2.res(id=None)
  
    def getId(self, request, context):
        return grpc_pb2.res(id=self.id)
