#!/usr/bin/env python
# encoding: utf-8

from eventlet import GreenPool
import itertools

def worker(line):
    if line != "\n":
#        return line.replace("\n","")+"0"
        return line.strip()+"0"
pool = GreenPool()
for result in pool.imap(worker,open("tt",'r')):
    print(result)

p = open("/etc/hosts",'r')
def rr(line):
    return line.strip()
for tt in itertools.imap(rr,p):
    print tt
