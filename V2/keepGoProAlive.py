import globals
from timeKeeper import *
from goPro import *
import time
from PyQt5 import QtCore

class Run(QtCore.QThread):
	lastRun = 0
	def __init__(self, parent=None):
		QtCore.QThread.__init__(self, parent)
    
	def run(self):
		print("Run")
		while globals.keepaliverunning == True:
			if timeKeeper.timeCheck(self.lastRun, 180, time.time(), False) == True:
				goPro.testInternet()
				self.lastRun = time.time()
				print("Keep Alive")
            