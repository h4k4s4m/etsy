import psutil
import re
search="bird"+"+"

for proc in psutil.process_iter():
  try:
    if proc.name=="chrome.exe":
      print proc.pid
      print proc.name
  except :
    """"""""
x=raw_input("Press Enter to continue")

for proc in psutil.process_iter():
  try:
    match=re.search(search, proc.name)
    if match != None:
      print proc.name
  except:
      x=False
