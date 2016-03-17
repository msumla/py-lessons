import os
import gzip

from readlog import Readlog
readlog = Readlog()

from lxml import etree
from lxml.cssselect import CSSSelector  

#from argparser import Argparser
#argparser = Argparser()
import argparse

from jinja2 import Environment, FileSystemLoader # templating engine
import codecs

#from humanizer import Human
#humanize = Humanize()

parser = argparse.ArgumentParser(description='Apache2 log parser')
parser.add_argument('--path', help='Path to Apache2 log files', default="logs")
parser.add_argument('--top-urls', help="Find top URL-s", action='store_true')
parser.add_argument('--geoip', help="Resolve IP-s to country codes", action='store_true')

args = parser.parse_args()
print("We are expecting logs from:", args.path)
#print("Do we want top URL-s?")
 
# Following is the directory with log files,
# On Windows substitute it where you downloaded the files
root = "logs"

print("Parsing ..")

parsed = 0
for filename in os.listdir(args.path):
    if not filename.startswith("access.log"):
#        print "Skipping unknown file:", filename
        continue
    if filename.endswith(".gz"):
#       print "Unpacking compressed file:", filename
#        readlog.readLog(gzip.open(os.path.join(root, filename)))
        parsed+=1
        continue
    readlog.readLog(open(os.path.join(root, filename)))
    parsed+=1

print("Log files parsed: ", parsed)
    
resu = readlog.cntrs.items()
resu.sort(key = lambda item:item[1], reverse=True)
document = etree.parse(open('BlankMap-World6.svg'))

for u in range(100):
#    print("Top countries ", u+1, resu[u])

    sel = CSSSelector("#" + resu[u][0])
    for j in sel(document):
        j.set("style", "fill: hsl(%.2d, 100%%, 40%%);" % resu[u][1]*10)
        #ABBA" + str(u ** u))
        # Remove styling from children
        for i in j.iterfind("{http://www.w3.org/2000/svg}path"):
            i.attrib.pop("class", "")

with open("highlighted.svg", "w") as fh:
    fh.write(etree.tostring(document))
print("('The map has been coloured.')")

rest = readlog.users.items()
rest.sort(key = lambda item:item[1], reverse=True)
for t in range(10):
	print(rest[t])

res = readlog.ips.items()
res.sort(key = lambda item:item[1], reverse=True)
for o in range(5):
    print("Top ips ", o+1, res[o])

env = Environment(loader=FileSystemLoader(os.path.dirname(__file__)), trim_blocks=True)
with codecs.open("output.html", "w", encoding="utf-8") as fh:
	fh.write(env.get_template("report.html").render(locals())) #locals is a dict with all locally defined variables

#print(env.get_template("report.html").render(variable="blah"))
