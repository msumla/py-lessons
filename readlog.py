class Readlog():

    def readLog(self, fh):

        import urllib
        import GeoIP
        
        gi = GeoIP.open("GeoIP.dat", GeoIP.GEOIP_MEMORY_CACHE)
        keywords = "Windows", "Linux", "Mac", "Googlebot"
        d = {"Windows":0, "Linux":0, "Mac":0, "Googlebot":0} #a dictionary aka an array
        self.users = {}
        self.ips = {}
        self.cntrs = {}
        win = 0
        total = 0
        
        for line in fh: #for each
            total = total + 1
            try:
                source_timestamp, request, response, _, _, agent, _ = line.split("\"") #split by "
                method, path, protocol = request.split(" ") #split by space and define as variables
                path = urllib.unquote(path)
                
                ip_address, _ , _, timestamp = source_timestamp.split(" ", 3)
                gef = gi.country_code_by_addr(ip_address)
                if not type(gef) == "NoneType":
                    gef = gef.lower()
                if not ":" in ip_address:
                    self.ips[ip_address] = self.ips.get(ip_address, 0) + 1
                    self.cntrs[gef] = self.cntrs.get(gef, 0) + 1
#                    print(ip_address, " @ ", gi.country_code_by_addr(ip_address).lower())
#                if path.staswith("/~"):
#                    username, remainder = path[2:].split("/", 1)
#                    try:
#                        self.users[username] += 1
#                    except:
#                        self.users[username] = 1

#                for keyword in keywords: #for each
#                    if keyword in agent: #ctrl+f
#                        d[keyword] += 1
#                        break
#                print(path)
#                 browser, osetc, _, _, _ = agent.split(";")
#                 print osetc
#                if "Windows" in agent: #ctrl+f
#                    win += 1
            except:
                pass #mandatory syntax, doesn't do anthing
              

        #print "Total requests: ", total
        #print "Windows requests: ", win
        #print "Windows requests: %.02f%%" % (win * 100.0 / total), "of total"

        totalos = d["Windows"]+d["Linux"]+d["Mac"]+d["Googlebot"] #or:
        totalos = sum(d.values())

#        for key, value in d.items():
#            print key, "==>", value, "(", value * 100 / totalos, "%)" #or:
#            print "%s ==> %d (%.02f%%)" % (key, value, value * 100.0 / totalos) # formatting
#            print "%.03s" % totalos # 3 characters displayed

