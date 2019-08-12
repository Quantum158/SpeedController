import time

import modules.globals
from modules.goPro import *
from modules.timeKeeper import *
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal

globals = modules.globals


class Run(QtCore.QThread):
	lastRun = 0
	global loopHold
	loopHold = False
	sendWOL = pyqtSignal()
	firstReply = pyqtSignal()
	toLog = pyqtSignal(str, str)

	def __init__(self, parent=None):
		QtCore.QThread.__init__(self, parent)

	def run(self):
		Run.loopHold = False
		print("[Keep Alive] Thread Initiated")
		self.toLog.emit("[Keep Alive] Thread Initiated", "green")
		self.lastRun = 0
		while globals.keepaliverunning == True:
			if timeKeeper.timeCheck(self.lastRun, 25, time.time(), False) == True and Run.loopHold == False:
				print("[Keep Alive] Pinging Camera")
				self.toLog.emit("[Keep Alive] Pinging Camera", "orange")
				Run.loopHold = True
				goPro.keepAlive()
				
				if goPro.testInternet() == True:
					if globals.goProFirstConnect == 1:
						self.firstReply.emit()
					Run.loopHold = False
					self.lastRun = time.time()
					print("[Keep Alive] Reply Recieved")
					self.toLog.emit("[Keep Alive] Reply Recieved", "green")
				
				else:
					print("[Keep Alive] Camera Unavailable, WOL recommended")
					self.toLog.emit("[Keep Alive] Camera Unavailable, WOL recommended", "orange")
					self.lastRun = time.time()
					self.sendWOL.emit()
		print("[Keep Alive] Thread Terminated")
		self.toLog.emit("[Keep Alive] Thread Terminated", "red")
