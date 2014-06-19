while True:
    def isRunning(window_title):
        import win32gui, win32com.client
        shell = win32com.client.Dispatch("WScript.Shell")
        try:
            if win32gui.FindWindowEx( None, None, None, window_title):
                print "Found Your Window"
                shell.SendKeys('%')
                win32gui.SetForegroundWindow(win32gui.FindWindowEx( None, None, None, window_title))
                return True
        except:
            print "Find window failed "
            return False
        
    import os
    import time


    
    window="*Python 2.7.6 Shell*"
    x=isRunning(window)

    if x==True:
        print "success"
        #os.startfile("C:\\Users\\ssamarghandi\\Desktop\\Work Files and Projects\\Scripts\\mine\\convert temperature.py")
    if x==False:
        print "method returned false"
             
    time.sleep(5)


