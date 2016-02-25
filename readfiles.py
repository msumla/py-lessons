import os
from datetime import datetime
times = [] #array

def humanize(bytes):
	if bytes < 1024:
		return "%.2f B" % bytes
	elif bytes < 1024 ** 2:
		return "%.2f kB" % (bytes / 1024.0)
	elif bytes < 1024 ** 3:
		return "%.2f MB" % (bytes / 1024.0 ** 2)
	else:
		return "%.2f GB" % (bytes / 1024.0 ** 3)

for filename in (os.listdir(".")): #list of files in the current directory
	mode, inode, device, nlink, uid, gid, size, atime, mtime, ctime =  os.stat(filename) #split
	times.append((filename, datetime.fromtimestamp(mtime), size)) #adding value to array on the 1. index
	
times.sort(key = lambda(filename, dt, size):dt) #sorting

for filename, dt, size in times:
	print filename, "@", dt, "-", humanize(size)
