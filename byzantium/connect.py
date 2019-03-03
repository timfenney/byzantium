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

connection = redis.Redis(host='192.168.1.131', password='qwertpoiuy')

def publish(data):
    connection.publish(CHANNEL, data)

def set_device(device):
    connection.set(DEVICE, device)

def get_device():
    return connection.get(DEVICE)
