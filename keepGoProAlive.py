import globals
from timeKeeper import *
from goPro import *
import time
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal


class Run(QtCore.QThread):
	lastRun = 0
	global loopHold
	loopHold = False
	sendWOL = pyqtSignal()
	firstReply = pyqtSignal()

	def __init__(self, parent=None):
		QtCore.QThread.__init__(self, parent)

	def run(self):
		Run.loopHold = False
		print("[Keep Alive] Thread Initiated")
		self.lastRun = 0
		while globals.keepaliverunning == True:
			if timeKeeper.timeCheck(self.lastRun, 25, time.time(), False) == True and Run.loopHold == False:
				print("[Keep Alive] Pinging Camera")
				Run.loopHold = True
				goPro.keepAlive()
				
				if goPro.testInternet() == True:
					if globals.goProFirstConnect == 1:
						self.firstReply.emit()
					Run.loopHold = False
					self.lastRun = time.time()
					print("[Keep Alive] Reply Recieved")
				
				else:
					print("[Keep Alive] Camera Unavailable, WOL recommended")
					self.lastRun = time.time()
					self.sendWOL.emit()
		print("[Keep Alive] Thread Terminated")
