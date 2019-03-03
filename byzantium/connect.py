# -*- coding: utf-8 -*-
#
# This file provides the ability to consume or emit.
from . import serialize
from . import events
import redis

# fixme: remove hard-coded configuration
NAMESPACE = 'byzantium'
DEVICE = NAMESPACE + '-device'
CHANNEL = NAMESPACE + '-events'

connection_ = redis.Redis(host='192.168.1.131', password='qwertpoiuy')

def publish(data):
    connection_.publish(CHANNEL, data)

def set_device(device):
    connection_.set(DEVICE, device)

def get_device():
    return connection.get(DEVICE)

def connection():
    return connection_
