import globals
from timeKeeper import *
from goPro import *
import time
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal


class Run(QtCore.QThread):
	lastRun = 0
	sendWOL = pyqtSignal()
	firstReply = pyqtSignal()

	def __init__(self, parent=None):
		QtCore.QThread.__init__(self, parent)

	def run(self):
		print("[Keep Alive] Thread Initiated")
		self.lastRun = 0
		while globals.keepaliverunning == True:
			if timeKeeper.timeCheck(self.lastRun, 180, time.time(), False) == True:
				print("[Keep Alive] Pinging Camera")
				goPro.keepAlive()
				self.lastRun = time.time()
				if goPro.testInternet() == True:
					if globals.goProFirstConnect == 1:
						self.firstReply.emit()
					print("[Keep Alive] Reply Recieved")
				else:
					print("[Keep Alive] Camera Unavailable, WOL recommended")
					self.sendWOL.emit()
		print("[Keep Alive] Thread Terminated")
