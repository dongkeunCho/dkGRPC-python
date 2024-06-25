import json
from src.grpc import grpc_pb2_grpc
from src.grpc import grpc_pb2

class Id_Manager(grpc_pb2_grpc.Id_ManagerServicer):
    def __init__(self):
        self.id = "None"

    def getId(self, request, context):
        return self.id

    def setId(self, request, context):
        params = json.loads(request.params)
        self.id = params['id']
        return grpc_pb2.Response(data=self.id)