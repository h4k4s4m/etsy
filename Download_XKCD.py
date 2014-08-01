import urllib
import re
x=0
live_comics=[]
while 1:
    x+=1
    html=str(urllib.urlopen('http://xkcd.com/%s/' % x).read())
    if x==404:
        continue
    if '404 - Not Found' in html:
        break
    else:
        try:
            live_comics.append(re.findall(r'http://imgs.xkcd.com/comics/.+?\....?', html)[0])
        except:
            pass
    print(x),
    
y=0
print "saving %d" % (int(y)+1)
for n in live_comics:
    print n
    y+=1
    urllib.urlretrieve(n,"%s.%s" % (y,n[-3:]))

