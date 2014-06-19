import re
import time
import  os, psutil

search=raw_input("Enter the process to monitor:    ")
search=search+"+"
seconds=raw_input("Enter the update interval in seconds:    ")


check=False
for proc in psutil.process_iter():
  try:
    match=re.search(search.lower(), proc.name.lower())
    if match!=None:
      global datvar
      datvar=proc.exe
      check=True
    else:
      " "
  except:
    " "

x=True
while check==True:
  while x==True:
    x=False
    for proc in psutil.process_iter():
      try:
        match=re.search(search.lower(), proc.name.lower())
        if match!=None:
          x=True
        else:
          " "
      except:
       " "
    print "checking"
    time.sleep(float(seconds))
        
  print ("Process no longer found. Restarting...")
  try:
    print "trying to open", datvar, "please wait"
    os.startfile(datvar)
    #os.startfile("c:/restarter/email.vbs")
    print("Process Restarted Successfully. Waiting 20 seconds.")
    time.sleep(20)
    x=True
  except:
    print "Restart failed"
    time.sleep(20)
    #os.startfile("Enter the path to an email script here")
  
print ("\nYour process was not found at all, please run this again and \nmake sure you type the name found in process manager\n")
raw_input("press enter to continue")
