#!/usr/bin/env python
import greenlet
import time

def test1():
    print 12
#    gr2.switch()
#    greenlet.getcurrent().parent.switch()
#    print 34
    time.sleep(10)
    print 666
    print 666
    print 666


def test2():
    print 56
    gr1.switch()
    print 78

gr1=greenlet.greenlet(test1)
gr2=greenlet.greenlet(test2)
gr1.switch()
print "parent is here,and you will all be compeleted"      #parent is auto-created when exec,and is stand for main
gr2.switch()
