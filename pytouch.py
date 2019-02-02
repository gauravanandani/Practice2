#!/usr/bin/python2
import os,sys
a=sys.argv[1:]

for i in a:
	if os.path.isdir(i):
		print "dir is already exists"+i
	elif os.path.isfile(i):
		print "a file already exists with the name"+i
	else:
		os.mkdir(i)
