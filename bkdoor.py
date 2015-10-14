#!/usr/bin/env python
# encoding: utf-8

from eventlet import backdoor
import eventlet

message = "we are the world"

def _funca():
    print "abc"
    return "123"
def _change_mess(s="save rock'n roll"):
    global message
    message = s
backdoor_locals = {'funca': _funca,'change_mess':_change_mess}
eventlet.spawn(backdoor.backdoor_server, eventlet.listen(('localhost', 3000)),locals=backdoor_locals)
while True:
    print "aaa"
    print message
    eventlet.sleep(10)
