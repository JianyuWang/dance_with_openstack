#!/usr/bin/env python
# encoding: utf-8

from eventlet import event
import eventlet
evt = event.Event()
def baz(b):
    evt.send(b + 1)
_ = eventlet.spawn_n(baz,3)
evt.wait()
