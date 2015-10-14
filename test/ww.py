#!/usr/bin/env python
# encoding: utf-8
import eventlet
import os

def write_for_ever(writer):
    for i in range(1,5):
        writer.write("a")
        writer.flush()
    writer.close()
#w=open("/tmp/ww",'w')
#eventlet.spawn(write_for_ever,w)

def makenode():
    for i in range(1,5):
        os.mknode("/tmp/i")
def reca(w):
    print w
    line = raw_input("say something:\n")
    print line
#eventlet.spawn_n(reca("deng"))
eventlet.spawn_n(reca,
                 "duang")
#p =eventlet.GreenPile()
#pool = eventlet.GreenPool()
#pool.spawn(makenode)
