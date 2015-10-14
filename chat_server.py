#!/usr/bin/env python
# -*- coding: utf-8 -*-

import eventlet
from eventlet.green import socket
import re
from termcolor import colored
import logging

PORT = 3001
participants = set()
#participants = dict()
xiong_addr_re = re.compile('^111.')
name = dict()
color = dict()
change_name = re.compile('woshi')
logging.basicConfig(filename='/var/log/bar_tender.log',level=logging.DEBUG)

def read_chat_forever(writer, reader):
    line = reader.readline()
    while line:
        print line
        name[reader] = (line[5:] if change_name.match(line) else name[reader]).strip()
        #if change_name.match(line):
        #    name[reader] = line[5:].strip()
        print("Chat:", line.strip())
        for p in participants:
            try:
                if p is not writer:  # Don't echo
                    p.write(colored(name[reader]+":"+line,color[writer]))
                    p.flush()
            except socket.error as e:
                # ignore broken pipes, they just mean the participant
                # closed its connection already
                if e[0] != 32:
                    logging.exception(e)
                    raise
        line = reader.readline()
    participants.remove(writer)
#    participants.pop(writer)
    print("Participant left chat.")

try:
    print("ChatServer starting up on port %s" % PORT)
    server = eventlet.listen(('0.0.0.0', PORT))     #create server socket
    while True:
        new_connection, address = server.accept()   #connection is a new socket stands for a new clinet
        print("Participant joined chat.")
        new_writer = new_connection.makefile('w')
        participants.add(new_writer)
#        participants[new_writer] = ("兔兔" if xiong_addr_re.match(address[0]) else "熊熊")
        new_reader = new_connection.makefile('r')
        name[new_reader] = ("熊熊" if xiong_addr_re.match(address[0]) else "兔兔")
        color[new_writer] = ("blue" if xiong_addr_re.match(address[0]) else "magenta")
        new_writer.write(colored("欢迎来到我的酒馆！\n","green"))
        new_writer.flush()
        eventlet.spawn_n(read_chat_forever,
                         new_writer,
                         new_reader)
except (KeyboardInterrupt, SystemExit):
    print("ChatServer exiting.")
