import win32api
import win32com.client

shell = win32com.client.Dispatch("WScript.Shell")

sleep1=1500
sleep2=sleep1*2

while True:
  shell.SendKeys("%{Esc}")
  win32api.Sleep(sleep2)
  
  
