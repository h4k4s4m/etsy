import psutil
import re
import os
import time

while True:
  search="thunderbird"+"+"

  x=False
  for proc in psutil.process_iter():
    try:
      match=re.search(search, proc.name)
      if match != None:
        x=True
        print proc.name
    except:
        y=True

  if x==False:
    os.startfile(r"C:\Program Files (x86)\Mozilla Thunderbird\thunderbird.exe")
    print "Process Restarted"
    time.sleep(5)
  elif x==True:
    print "Process Found"
    
  time.sleep(5)
