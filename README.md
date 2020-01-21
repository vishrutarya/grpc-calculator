# Simple gRPC service: calculator

# Summary

Implements a near-minimal gRPC service. As such, provides a quick high-level introduction to Google's open-sourced remote procedure call (RPC) framework.

The service implemented is a simple calculator. By exposing two methods, the calculator enables the client to enter a number and receive either the number's square or square root, as desired.

# Quick start

In a terminal window, clone the repo, install requirements, create the auto-generated protobuf files, and instantiate the server:
```
git clone https://github.com/vishrutarya/grpc-calculator
cd grpc-calculator
pip install -r requirements.txt
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto
python server.py
```

In another terminal window, run the client:
```
python client.py
```

To close the server, interrupt the keyboard (`ctrl+c`) in the terminal window where the server is running.


## File structure and descriptions

```
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
```

# References

1. Ramanan Balakrishnan's [blog post](https://engineering.semantics3.com/6c4e25f0c506) and [repo](https://github.com/ramananbalakrishnan/basic-grpc-python)
2. [gRPC docs](https://grpc.io/docs/)