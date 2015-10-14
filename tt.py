#!/usr/bin/env python
# encoding: utf-8

import eventlet.greenthread as grth
import eventlet

def funa(a):
    #while True:
    a.write("aaa\n")
    a.flush()
    #grth.sleep(10)
    a.write("now a' back!\n")
    a.flush()
    #print "aaa"
    #grth.sleep(10)
    #print "a's back"

def funb(a):
    while True:
        a.write("bbb\n")
        a.flush()
        grth.sleep(10)
        a.write("now b' back!\n")
        a.flush()
#    print "bbb"
#    grth.sleep(10)
#    print "b's back"
def func():
    while True:
        print 1
#eventlet.spawn_n(func)

a=open("/tmp/thread",'w')
eventlet.spawn_n(funa,a)
#eventlet.spawn(funb,a)
