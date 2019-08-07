import globals
import configLoader
from timeKeeper import *
import time
import datetime
import sys, os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import pyqtSignal
from pygame import mixer

mixer.init()
LowTone = mixer.Sound(os.path.join(__location__, "Resources", "Sounds" , "LowTone.ogg"))
HighTone = mixer.Sound(os.path.join(__location__, "Resources", "Sounds" , "HighTone.ogg"))
FalseStart = mixer.Sound(os.path.join(__location__, "Resources", "Sounds" , "FalseStart.ogg"))
PacerTone = mixer.Sound(os.path.join(__location__, "Resources", "Sounds" , "PacerTone.ogg"))

class Run(QtCore.QThread):
	aTime = pyqtSignal(str)
	aColour = pyqtSignal(str)
	bTime = pyqtSignal(str)
	bColour = pyqtSignal(str)
	textStatus = pyqtSignal(str)

	def __init__(self, parent=None):
		QtCore.QThread.__init__(self, parent)
	
	def run(self):
		currentBeep = 0
		if configLoader.PacerBeeps > 0:
			currentBeep = 1
		globals.controlState = 0
		globals.runthreadrunning = True
		if configLoader.TimeAEnabled == True:
			self.aTime.emit("00:00.00")
		
		else:
			self.aColour.emit(str((255,255,255)))
			self.aTime.emit("Offline")

		if configLoader.TimeBEnabled == True:
			self.bTime.emit("00:00.00")

		else:
			self.bColour.emit(str((255,255,255)))
			self.bTime.emit("Offline")

		sleep(1)
		if int(configLoader.delayStage) > 0:
			globals.controlState = -1 #Hold start
			globals.timePoint = time.time()
			self.textStatus.emit("Delay set for\n" + str(configLoader.delayStage) + " seconds")
			while globals.runthreadrunning == True:
				if timeKeeper.timeCheck(globals.timePoint, int(configLoader.delayStage), time.time()) == True:
					globals.controlState = 0
					globals.timePoint = 0
					break
				else:
					sleep(0.01)
					self.textStatus.emit(str(timeKeeper.counter(globals.timePoint, time.time(), int(configLoader.delayStage))))
				

		playState = 0
		played = False
		while globals.runthreadrunning == True and globals.controlState > -1:
			if globals.controlState == 0: #Countdown
				if globals.timePoint == 0:
					self.textStatus.emit("Countdown\nRunning")
					globals.timePoint = time.time()

				if configLoader.TimeAEnabled == True:
					self.aColour.emit(str((0,89,255)))
					self.aTime.emit("00:00.00")

				if configLoader.TimeBEnabled == True:
					self.bColour.emit(str((0,89,255)))
					self.bTime.emit("00:00.00")

				if timeKeeper.timeCheck(globals.timePoint, 1.00, time.time()) == True and playState == 0:
					playState = 1 
					LowTone.play()
					print("Tone 1")
			
				if timeKeeper.timeCheck(globals.timePoint, 2.00, time.time()) == True and playState == 1:
					playState = 2 
					LowTone.play()
					print("Tone 2")
		
				if timeKeeper.timeCheck(globals.timePoint, 3.00, time.time()) == True and playState == 2:
					playState = 3
					HighTone.play()
					print("Tone 3")
					played = True

				if played == True and mixer.get_busy() != 1:
					globals.controlState = 1
					globals.timePoint = 0
					if configLoader.TimeAEnabled == True:
						globals.timeAactive = True
					if configLoader.TimeBEnabled == True:
						globals.timeBactive = True

			if globals.controlState == 1: #Timers Running
				if globals.timePoint == 0:
					globals.timePoint = time.time()
					self.textStatus.emit("Timer Active")
					if globals.timeAactive == True:
						self.aColour.emit(str((16,220,2)))
					if globals.timeBactive == True:
						self.bColour.emit(str((16,220,2)))
					
				if currentBeep > 0 and currentBeep <= configLoader.PacerBeeps:
					if timeKeeper.timeCheck(globals.timePoint, currentBeep, time.time()) == True:
						if currentBeep == configLoader.PacerBeeps:
							FalseStart.play()
						else:
							PacerTone.play()
						currentBeep += 1
				#if InputCheck.getLeftShiftPressed() == True and globals.timeAactive == True:
				#	globals.timeAactive = False
				#	FalseStart.play()
		
				#if InputCheck.getRightShiftPressed() == True and globals.timeBactive == True:
				#	globals.timeBactive = False
				#
				if globals.timeAactive == True:
					self.aTime.emit(str(timeKeeper.timeDif(globals.timePoint, time.time())))
				if globals.timeBactive == True:
					self.bTime.emit(str(timeKeeper.timeDif(globals.timePoint, time.time())))

				if globals.timeAactive == False and globals.timeBactive == False:
					self.textStatus.emit("Both Timers\nStopped!")
				
			if globals.controlState == 2: #Timers Stopped
				print("")
			
			sleep(0.016)
				
		print("Run Thread Exited")
		globals.controlState = 0
		globals.timePoint = 0