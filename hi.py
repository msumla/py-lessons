#!/usr/bin/python

print "Hi!"

for line in open("/etc/passwd"):
	if line.startswith("root") and "/bash" in line:
		print ("Line")
print "New line"

name = raw_input("Name?")

if name == ("asd"):
	print "Is asd"
else:
	print "Not asd"
