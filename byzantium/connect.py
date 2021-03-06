# -*- coding: utf-8 -*-
#
# This file provides the ability to consume or emit.
from . import serialize
import redis

# fixme: remove hard-coded configuration
NAMESPACE = 'byzantium'
DEVICE = NAMESPACE + '-device' # this is what to set the device to
TYPING = NAMESPACE + '-typing'
ALL = NAMESPACE + '-*'
HOST='bob.local'

connection = redis.Redis(host=HOST, password='qwertpoiuy')
pubsub = connection.pubsub(ignore_subscribe_messages=True)

def publish(data):
    print("publishing: " + str(data))
    connection.publish(TYPING, data)

def set_device(device):
    connection.set(DEVICE, device)

def get_device():
    return connection.get(DEVICE)
