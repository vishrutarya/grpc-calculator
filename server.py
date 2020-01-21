import grpc 
from concurrent import futures
import time

import calculator_pb2, calculator_pb2_grpc

import calculator

# DEFINE CALCULATOR SERVICE
class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):

    def SquareRoot(self, request, context):
        """
        Exposes calculator.square_root() and calls it to return the square root of the `request` param.
        """
        
        #  init the response as an instance of the Number class
        response = calculator_pb2.Number() 
        
        # set the response value to the result of the call to the square_root method
        response.value = calculator.square_root(request.value)
        
        return response

    def Square(self, request, context):
        """
        Exposes calculator.square() and calls it to return the square of the `request` param.
        """ 

        response = calculator_pb2.Number()
        response.value = calculator.square(request.value)
        return response


# INSTANTIATE GRPC SERVER
# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# attach the server functions class to the server
calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)

# init server: list to port 50051
server.add_insecure_port("[::]:50051")
# start server
server.start()
print("Server started; listening on (unsecured) port 50051.")

# add sleep-loop to keep server alive
try:
    while True:
        time.sleep(86400) # 86,400 seconds == 1 day
except KeyboardInterrupt:
    server.stop(0)

