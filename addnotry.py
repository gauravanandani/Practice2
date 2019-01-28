#!/usr/bin/python2
import webbrowser
try:
	x=raw_input("Enter number one")
	y=raw_input("Enter number two")
	print int(x)+int(y)



except:
	webbrowser.open_new_tab("http://www.google.com/search?q=calculator")

