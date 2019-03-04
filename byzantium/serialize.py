# -*- coding: utf-8 -*-

# This file provides the serialize() function. The idea is to have an app-wide
# strategy, which other components don't need to know about.

import json

def serialize(data):
    import pdb; pdb.set_trace()
    return json.dumps(data)

def deserialize(serialized):
    return json.loads(serialized)
