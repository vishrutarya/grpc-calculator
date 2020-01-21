import grpc

import calculator_pb2, calculator_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel("localhost:50051")

# create a stub: converts parameters passed between client and server during a remote procedure call
stub = calculator_pb2_grpc.CalculatorStub(channel)

# create a valid request message
request = calculator_pb2.Number(value=9)

# make the remote procedure call (rpc)
response = stub.SquareRoot(request)

print(response.value)