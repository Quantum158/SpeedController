import urllib.request
from wakeonlan import send_magic_packet
import globals
from time import sleep
import socket
import sys
import json

class goPro:

    #For keepAlive
    def get_command_msg(id):
        return "_GPHD_:%u:%u:%d:%1lf\n" % (0, 0, 2, 0)
    HOME_IP = "10.5.5.9"
    HOME_PORT = 8554
    KEEP_ALIVE_CMD = 2
    MESSAGE = get_command_msg(2)
    if sys.version_info.major >= 3:
        MESSAGE = bytes(MESSAGE, "utf-8")
    
    checkUrl = 'http://10.5.5.9/gp/gpControl/status'
    def cameraCheck():
        if goPro.testInternet() == True:
            return True
        else:
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
                #res = urllib.request.urlopen(goPro.checkUrl, None, 1)
                #data = res.read()
                #encoding = res.info().get_content_charset("utf-8")
                #json_data = json.loads(data.decode(encoding))
                #print(json_data)
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
            if globals.recording == True:
                print("[WARN] Trigger Shutter command recieved but camera is already recording! Ignored")
            else:
                urllib.request.urlopen('http://10.5.5.9/gp/gpControl/command/shutter?p=1')
                globals.recording = True
        except Exception:
            print("Trigger Shutter Error")
            globals.error = True

    def stopShutter():
        try:
            if globals.recording == False:
                print("[WARN] Stop Shutter command recieved but camera is not recording! Ignored")
            else:
                urllib.request.urlopen('http://10.5.5.9/gp/gpControl/command/shutter?p=0')
                globals.recording = False
        except Exception:
            print("Stop Shutter Error")
            globals.error = True

    def keepAlive():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            sock.sendto(goPro.MESSAGE, (goPro.HOME_IP, goPro.HOME_PORT))
        except Exception:
            print("Keep Alive Error")
            globals.error = True

