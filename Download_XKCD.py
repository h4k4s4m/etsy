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
            live_comics.append(re.findall(r'http://imgs.xkcd.com/comics/.+png', html)[0])
        except:
            try:
                live_comics.append(re.findall(r'http://imgs.xkcd.com/comics/.+jpg', html)[0])
            except:
                try:
                    live_comics.append(re.findall(r'http://imgs.xkcd.com/comics/.+gif', html)[0])
                except:
                    pass
    print(x),
    
y=1
print "saving"
for n in live_comics:
    urllib.urlretrieve(n,"%s.%s" % (y,n[-3:]))
    y+=1
