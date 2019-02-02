#!/usr/bin/python2

import socket

ip="127.0.0.2"
port="9090"

s=socket.socket(socket.AF_INET,socket.SOCK_DRAM)

s.bind(ip,port)

print s.recfrom(100)
