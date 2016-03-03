import os
import gzip
from readlog import Readlog
readlog = Readlog()
#from argparser import Argparser
#argparser = Argparser()
i = 0

import argparse

parser = argparse.ArgumentParser(description='Apache2 log parser')
parser.add_argument('--path', help='Path to Apache2 log files', default="logs")
parser.add_argument('--top-urls', help="Find top URL-s", action='store_true')
parser.add_argument('--geoip', help="Resolve IP-s to country codes", action='store_true')

args = parser.parse_args()
print("We are expecting logs from:", args.path)
print("Do we want top URL-s?")
 
# Following is the directory with log files,
# On Windows substitute it where you downloaded the files
root = "logs"

print("Parsing ..")
for filename in os.listdir(args.path):
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

#res = readlog.users.items()
#res.sort(key = lambda item:item[1], reverse=True)
#print(res[:1])

res = readlog.ips.items()
res.sort(key = lambda item:item[1], reverse=True)
for o in range(3):
    print("Top ", o+1, res[o])
