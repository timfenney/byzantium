# -*- coding: utf-8 -*-
#
# This file provides the ability to consume or emit.
from . import serialize
from . import events

import redis

# fixme: remove hard-coded configuration
CHANNEL = 'byzantium'
connection = redis.Redis(host='192.168.1.131', password='qwertpoiuy')

def emit(data):
    connection.publish(CHANNEL, data)

