#!/usr/bin/env python
# encoding: utf-8

import eventlet
from eventlet import event

evt = event.Event()
evt1 = event.Event()
def funa(m):
    global evt
    print m
    evt.wait()
    print "a's back"

def funb(m):
    print m
    evt1.wait()
    print "b's back"
def func(m):
    print m
    evt1.send()
    evt.send()
    print "c's finished"
   # g_self=eventlet.getcurrent()
   # g_self.parent.sleep(0)
#r1=eventlet.spawn(funa,"a")
#r2=eventlet.spawn(funb,"b")
#r3=eventlet.spawn(func,"c")
#eventlet.sleep(0)
#evt1.wait()
#eventlet.sleep(0)
#eventlet.sleep(0)
#print eventlet.getcurrent()
pool=eventlet.GreenPool()
#pile=eventlet.GreenPile(pool)
pile=eventlet.GreenPile(1000)
#r1=pool.spawn(funa,"a")
#r2=pool.spawn(funb,"b")
#r3=pool.spawn(func,"c")
r1=pile.spawn(funa,"a")
r2=pile.spawn(funb,"b")
r3=pile.spawn(func,"c")
#titles=['title',]
#titles = '\n'.join(pile)
#print [titles]
#for i in pile:
#    pile.next()
pile.next()
#pool.waitall()
