# Simple gRPC service: calculator

# Summary

Implements a near-minimal gRPC service to provide a high-level working model of Google's open-sourced remote procedure call (RPC) framework.

The service implemented is a simple calculator. By exposing two methods, the calculator enables the client to enter a number and receive either the number's square or square root, as desired.

# Quick start

`$ git clone https://github.com/vishrutarya/grpc-calculator`
`$ cd grpc-calculator`
`$ pip install -r requirements.txt`
`$ python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto` -- Auto-generates the protobuf files from the .$ proto file.
`$ python server.py` -- Instantiates the server.
`$ python client.py` -- Runs the simple client.


## File structure and descriptions

/grpc-calculator
├── calculator.proto        # defines protocol buffer (syntax, messages, services)
|
├── calculator.py           # module of functions to be exposed as the remote procedures
|
├── calculator_pb2.py       # auto-generated classes for messages and services
├── calculator_pb2_grpc.py  # auto-generated classes for server and client
|
├── client.py               # a simple client
├── server.py               # a server to expose the gRPC service
|
|
├── LICENSE
├── README.md
├── requirements.txt        
├── .gitignore

# References

1. Ramanan Balakrishnan's [blog post](https://engineering.semantics3.com/6c4e25f0c506) and [repo](https://github.com/ramananbalakrishnan/basic-grpc-python)
2. [gRPC docs](https://grpc.io/docs/)