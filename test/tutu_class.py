#!/usr/bin/env python
# encoding: utf-8

class tutu(object):
    def __init__(self,_name,_age):
        self.name=_name
        self.age=_age

l=[]
l.append(tutu('saber',26))
l.append(tutu('archer',27))
print l
print l[0].age
