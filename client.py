import grpc

import calculator_pb2, calculator_pb2_grpc

def print_results(request, response, procedure_name) -> None:
    """
    Prints results of a fulfilled request.
    """
    procedure_names_dict = {
        'SquareRoot': calculator_pb2_grpc.CalculatorServicer.SquareRoot.__name__,
        'Square': calculator_pb2_grpc.CalculatorServicer.Square.__name__,
    }
    print_string = f"Request: {procedure_names_dict[procedure_name]} for {request.value}.\nResponse: {response.value}.\n"
    print(print_string)


# open a gRPC channel
channel = grpc.insecure_channel("localhost:50051")

# create a stub: converts parameters passed between client and server during a remote procedure call
stub = calculator_pb2_grpc.CalculatorStub(channel)

# create a valid request message
request = calculator_pb2.Number(value=9)

# make the remote procedure call (rpc)
response = stub.SquareRoot(request)

print_results(request, response, 'SquareRoot')


# make new requests and fulfill
request = calculator_pb2.Number(value=16)
response = stub.SquareRoot(request)
print_results(request, response, 'SquareRoot')


# request: square
request = calculator_pb2.Number(value=5)
response = stub.Square(request)
print_results(request, response, 'Square')
