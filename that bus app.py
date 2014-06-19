import urllib
import os
import webbrowser
from xml.etree.ElementTree import parse
daves_lat=41.980262



def distance(lat1, lat2):
  return 69*abs(lat1-lat2)

def monitor():
  global _lat
  global _lon
  global _dis
  u=urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
  parsed=parse(u)
  for bus in parsed.findall('bus'):
   #  if bus.findtext('id') == '4189':
                    busid=bus.findtext('id')
                    _lat=float(bus.findtext('lat'))
                    _lon=float(bus.findtext('lon'))
                    _dis=distance(_lat, daves_lat)
                    print "bus:", busid, "is", "%.5s" % str(_dis), "miles away"
                     
                    


import time
while True:
              os.system("cls")
              monitor()
              for n in range(15):
                print 15-n,
                time.sleep(1)

              print ""
   #           if _dis>2:
 #               break
webbrowser.open('maps.google.com/?q='+str(_lat)+','+str(_lon))          
