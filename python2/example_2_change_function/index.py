#!/usr/bin/env python2
from flask import Flask, request
import cPickle

app = Flask(__name__)

@app.route('/')
def home():
    cPickle.loads(str(request.args.get('pickle')))
    return finished()

def finished():
    return "The function completed!"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)
