#!/usr/bin/env python3

import pickle, builtins

class Pickle(object):
    def __reduce__(self):
        return (builtins.exec, ("print('Load me from a file')",))

pickle.dump(Pickle(), open('pickle','wb'))