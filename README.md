# generate grpc python files
1. open terminal
2. command : cd <working-directory>
3. command : python -m grpc_tools.protoc -I./src/grpc  --python_out=./src/grpc --grpc_python_out=./src/grpc ./src/grpc/grpc.proto
4. open grpc_pb2_grpc.py
5. modify line 6 : import src.grpc.grpc_pb2 as grpc__pb2
