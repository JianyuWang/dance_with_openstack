#!/usr/bin/env python
# encoding: utf-8

import argparse

parser = argparse.ArgumentParser(description='Example with long option names')

parser.add_argument('--noarg', action="store_true", default=False)
#parser.add_argument('--witharg', action="store", dest="witharg")
parser.add_argument('--witharg', action="store", default="v")
parser.add_argument('--witharg2', action="store", dest="witharg2", type=int)

print parser.parse_args(['--noarg', '--witharg', 'val', '--witharg2=3'])
#args1 = parser.parse_args(['--noarg', '--witharg', 'val', '--witharg2=3'])
args1 = parser.parse_args()


print args1.noarg
print args1.witharg

