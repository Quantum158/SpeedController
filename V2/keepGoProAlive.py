import globals
from timeKeeper import *
from goPro import *
import time
from PyQt5 import QtCore

class Run(QtCore.QThread):
    def __init__(self, parent=None):
		QtCore.QThread.__init__(self, parent)
    
    def run(self):
        while globals.keepaliverunning == True:
            
            if timeKeeper.timeCheck(lastRun, 180, time.time()) == True:
                goPro.testInternet()
                lastRun = time.time()
            