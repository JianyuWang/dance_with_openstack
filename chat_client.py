#!/usr/bin/env python
# encoding: utf-8

import eventlet

cc=eventlet.connect(("0.0.0.0",3001))
message="hello,world!"
cc.sendall(message)
