import urllib.request
from wakeonlan import send_magic_packet
import globals
from time import sleep

class goPro:
    checkUrl = 'http://10.5.5.9/gp/gpControl/status'
    def cameraCheck():
        if goPro.testInternet() == True:
            return True
        else:
            print("WOL")
            if goPro.WOL() == True:
                if goPro.testInternet() == True:
                    return True
                else:
                    return False
    
    def testInternet():
        i = 0
        while True:
            try: 
                urllib.request.urlopen(goPro.checkUrl, None, 1)
                return True
            except Exception:
                pass
            i = i + 1
            if i > 3:
                return False
            sleep(1)
    
    def WOL():
        send_magic_packet("06416950834e", 
        ip_address='10.5.5.9',
        port=9
        )
        i = 0
        while True:
            try:
                urllib.request.urlopen(goPro.checkUrl, None, 2)
                return True
            except Exception:
                pass
            
            i = i + 1
            if i > 5:
                return False
            sleep(1)
        
    def forceToVideoMode(): #Prevents gopro from timing out when connected through wifi
        urls = ['http://10.5.5.9/gp/gpControl/command/mode?p=0', 'http://10.5.5.9/gp/gpControl/command/mode?p=1'] #Swap to picture mode, and back to video mode, will prevent camera from going into standby
        try:
            urllib.request.urlopen(urls[1], None, 3)
            sleep(2)
            urllib.request.urlopen(urls[0], None, 3)
        except Exception:
            print("Force to Video Error")
            globals.error = True

    def enableLocate():
        try:
            urllib.request.urlopen('http://10.5.5.9/gp/gpControl/command/system/locate?p=1')
        except Exception:
            print("Enable Locate Error")
            globals.error = True

    def disableLocate():
        try:
            urllib.request.urlopen('http://10.5.5.9/gp/gpControl/command/system/locate?p=0')
        except Exception:
            print("Disable Locate Error")
            globals.error = True

    def triggerShutter():
        try:
            urllib.request.urlopen('http://10.5.5.9/gp/gpControl/command/shutter?p=1')
            globals.recording = 1
        except Exception:
            print("Trigger Shutter Error")
            globals.error = True

    def stopShutter():
        try:
            urllib.request.urlopen('http://10.5.5.9/gp/gpControl/command/shutter?p=0')
            globals.recording = 0
        except Exception:
            print("Stop Shutter Error")
            globals.error = True