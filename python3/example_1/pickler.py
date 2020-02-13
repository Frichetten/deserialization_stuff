#!/usr/bin/env python3

import pickle, builtins

class Pickeler(object):
    def __reduce__(self):
        return(builtins.exec,("variable = 'Hello enemy!'",))

variable = "Hi friend!"

print(variable)

data = pickle.dumps(Pickeler())
pickle.loads(data)

print(variable)