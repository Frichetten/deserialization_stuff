#!/usr/bin/env python3

import socket, pickle

HOST = "0.0.0.0"
PORT = 9090

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    connection, address = s.accept()
    with connection: 
        print("My friend at ", address, " sent me some data")
        received_data = connection.recv(1024)
        pickle.loads(received_data)