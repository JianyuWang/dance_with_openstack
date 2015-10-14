#!/usr/bin/env python
# encoding: utf-8


import os
def _search_dirs(dirs, basename, extension=""):
    for d in dirs:
        path = os.path.join(d, '%s%s' % (basename, extension))
        if os.path.exists(path):
            print "%s" % path
            return path
if __name__ == "__main__":
    _search_dirs(["/root/workspace"],"test",".sh")
    #result = _search_dirs("/root/workspace","test",".sh")
    #print "%s" % result
