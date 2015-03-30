#!/usr/bin/env python

import sys
import dzmq

if len(sys.argv) > 1:
    topic = sys.argv[1]
else:
    topic = 'foo'
if len(sys.argv) > 2:
    msg = sys.argv[2]
else:
    msg = 'foobar'

d = dzmq.DZMQ()
d.advertise(topic)

i = 0
while True:
    d.publish(topic, '%s %d' % (msg, i))
    d.spinOnce(0.2)
    i += 1
