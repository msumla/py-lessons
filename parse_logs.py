import os
import gzip
from readlog import Readlog
readlog = Readlog()
i = 0
 
# Following is the directory with log files,
# On Windows substitute it where you downloaded the files
root = "logs"

print("Parsing ..")
for filename in os.listdir(root):
    if not filename.startswith("access.log"):
#        print "Skipping unknown file:", filename
        continue
    if filename.endswith(".gz"):
#        print "Unpacking compressed file:", filename
#        readlog.readLog(gzip.open(os.path.join(root, filename)))
        i+=1
        continue
    readlog.readLog(open(os.path.join(root, filename)))
    i+=1

print "Log files parsed: ", i

res = readlog.users.items()
res.sort(key = lambda item:item[1], reverse=True)
print(res[:1])
