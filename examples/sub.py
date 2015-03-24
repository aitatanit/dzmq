#!/usr/bin/env python

import sys
import pybsonmq

if len(sys.argv) > 1:
    topic = sys.argv[1]
else:
    topic = 'foo'


def cb1(topic, msg):
    print('1: Got %s on %s' % (msg, topic))


def cb2(topic, msg):
    print('2: Got %s on %s' % (msg, topic))

d = pybsonmq.DZMQ()
d.subscribe(topic, cb1)
d.subscribe(topic, cb2)
d.spin()
