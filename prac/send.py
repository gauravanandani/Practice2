#!/usr/bin/python2

import socket

ip="127.0.0.1"
port="9090"

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

d=raw_input("Enter your msg to send")
s.sendto(d,(ip,port))
