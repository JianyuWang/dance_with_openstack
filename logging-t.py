#!/usr/bin/env python
# encoding: utf-8

import logging
logging.basicConfig(filename='/var/log/example.log',level=logging.DEBUG,format='%(asctime)s %(message)s')
try:
    1/0
except Exception, e:
    logging.exception(e)
    raise
