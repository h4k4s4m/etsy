#Another Wonderful creation by Sahm Samarghandi-The Man, The Mystery, The Legend

#I created some quick tools to record xy cordinates using set() and click using xy cordinates

#The easiest way to use it is:
#x,y = set()
#click(x,y) or double_click(x,y)

#I also added some shorthands to set shell to the whs com object and keys to sendkeys method in shell


#Quick Reminder: win32con.MOUSEEVENTF_XXXXXXX returns an interger, you can replace it as such

import win32api, win32con, time, win32com.client

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def right_click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)

def set():
  x=win32api.GetCursorPos()
  return x


def double_click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    time.sleep(.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


def set_shell():
    global shell
    global keys
    shell=win32com.client.Dispatch("WScript.Shell")
    keys=shell.SendKeys

