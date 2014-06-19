#Author:Sahm Samarghandi

#This is a test lib to find a window and set it as the foreground window(as long as its not minimized)

def find_window(window):
	import win32gui
	import win32com.client
	shell = win32com.client.Dispatch("WScript.Shell")
	try:
		shell.SendKeys("%")
		win32gui.SetForegroundWindow(win32gui.FindWindow( None, window))
	except:
		print "Didn't find window or something went wrong"
	raw_input("Press {ENTER} to continue")
