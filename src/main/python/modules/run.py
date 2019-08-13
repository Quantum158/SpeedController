import os
import sys
import time
from time import sleep

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from pygame import mixer
from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, QTimer, pyqtSignal

import modules.configLoader
import modules.globals
import modules.resources
from modules.goPro import *
from modules.timeKeeper import *

globals = modules.globals
configLoader = modules.configLoader
resources = modules.resources

mixer.init()
LowTone = mixer.Sound(resources.lowTone)
HighTone = mixer.Sound(resources.highTone)
FalseStart = mixer.Sound(resources.falseStart)
PacerTone = mixer.Sound(resources.pacerTone)

def isNotBoolean(value):
	"""Returns a boolean if the inputted value is not a boolean (I promise this is useful)"""
	if str(value) == str(False) or str(value) == str(True):
		return False
	else:
		return True

def finishedFunctions(runClass, pacerCurrent, stopThreadholdPassed):
	passedChecks = 0
	requiredPass = -1
	if globals.goPro == 1:
		requiredPass = 3
	else:
		requiredPass = 2
	if globals.timeAactive == False and globals.timeBactive == False:
		runClass.textStatus.emit("Both Timers\nStopped!")
		passedChecks = passedChecks + 1

	if isNotBoolean(pacerCurrent) == False:
		passedChecks = passedChecks + 1
	
	if stopThreadholdPassed == True:
		passedChecks = passedChecks + 1

	
	if passedChecks == requiredPass:
		return True
	else:
		return False

def changeUIColour(runClass, rgb):
	runClass.aColour.emit(str(rgb))
	runClass.bColour.emit(str(rgb))

def goProCheckConnection(runClass):
	runClass.textStatus.emit("Checking GoPro\nConnection")

	if goPro.cameraCheck() == True:
		goPro.forceToVideoMode()
		changeUIColour(runClass, (255, 255, 255))
		pass
	else:
		runClass.textStatus.emit("GoPro Connection\nFailed!")
		changeUIColour(runClass, (220,16,2))
		runClass.goProFail.emit()
		globals.runthreadrunning = False
		globals.controlState = -1
		globals.error = True

def goProStartRecording(runClass):	
	if globals.recording == False:
		runClass.textStatus.emit("Starting Recording")
		sleep(0.25)
		goPro.triggerShutter()
		globals.recording = True
		runClass.buttonText.emit("Stop Record")		
		sleep(0.25)
	else:
		print("[RUN] [WARN] Attempted to start recording but camera reports it already is!")	

def timerDisplayReset(runClass):
	if configLoader.TimeAEnabled == True:
		runClass.aTime.emit("00:00.00")
	
	else:
		runClass.aColour.emit(str((255,255,255)))
		runClass.aTime.emit("Offline")

	if configLoader.TimeBEnabled == True:
		runClass.bTime.emit("00:00.00")

	else:
		runClass.bColour.emit(str((255,255,255)))
		runClass.bTime.emit("Offline")
	sleep(1)

class Run(QThread):
	aTime = pyqtSignal(str)
	aColour = pyqtSignal(str)
	bTime = pyqtSignal(str)
	bColour = pyqtSignal(str)
	textStatus = pyqtSignal(str)
	buttonText = pyqtSignal(str)
	goProFail = pyqtSignal()
	endThreadReset = pyqtSignal()
	keepalivethread = pyqtSignal()
	autoRecordStop = pyqtSignal()
	addToLogWindow = pyqtSignal(str, str)

	def __init__(self, parent=None):
		QtCore.QThread.__init__(self, parent)
		
	def run(self):
		print("[RUN] Thread Initiated")
		self.addToLogWindow.emit("[RUN] Thread Initiated", 'green')
		stopThreadholdPassed = False

		pacerCurrent = False
		if configLoader.PacerBeeps > 0:
			pacerCurrent = 1
		globals.controlState = 0
		globals.runthreadrunning = True

		if globals.goPro == True:
			goProCheckConnection(self)

		timerDisplayReset(self)

		if int(configLoader.delayStage) > 0:
			globals.controlState = -1 #Hold start
			globals.timePoint = time.time()
			changeUIColour(self, (255, 191, 0))
			#self.textStatus.emit("Delay set for\n" + str(configLoader.delayStage) + " seconds")
			if globals.goPro == True and globals.goProWarnings == True: #Camera Beeps to alert people to get away from the lens
				goPro.enableLocate()

			while globals.runthreadrunning == True:
				if timeKeeper.timeCheck(globals.timePoint, int(configLoader.delayStage), time.time()) == True:
					globals.controlState = 0
					globals.timePoint = 0
					if globals.goPro == True:
						goPro.disableLocate()
					break
				else:
					sleep(0.01)
					self.textStatus.emit("Starting in\n" + str(timeKeeper.counter(globals.timePoint, time.time(), int(configLoader.delayStage))))
				

				
		if globals.goPro == True and globals.error == False and globals.abort == False: #Start Recording on Camera
			goProStartRecording(self)

		#Setup for tone countdown
		playState = 0
		played = False
		while globals.runthreadrunning == True and globals.controlState > -1 and globals.abort == False and globals.error == False:
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
					print("[RUN] Tone 1")
					self.addToLogWindow.emit("[RUN] Tone 1", 'blue')
			
				if timeKeeper.timeCheck(globals.timePoint, 2.00, time.time()) == True and playState == 1:
					playState = 2 
					LowTone.play()
					print("[RUN] Tone 2")
					self.addToLogWindow.emit("[RUN] Tone 2", 'blue')
		
				if timeKeeper.timeCheck(globals.timePoint, 3.00, time.time()) == True and playState == 2:
					playState = 3
					HighTone.play()
					print("[RUN] Tone 3")
					self.addToLogWindow.emit("[RUN] Tone 3", 'blue')
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
					
				if isNotBoolean(pacerCurrent) == True and pacerCurrent <= configLoader.PacerBeeps:
					#isNotBoolean because false means no pacers enabled and true means pacers finished
					if timeKeeper.timeCheck(globals.timePoint, pacerCurrent, time.time()) == True:
						if pacerCurrent == configLoader.PacerBeeps:
							pacerCurrent = True
							FalseStart.play()
						else:
							PacerTone.play()
							pacerCurrent += 1
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

				
				if finishedFunctions(self, pacerCurrent, stopThreadholdPassed) == True:
					globals.controlState = 2			
				
			if globals.controlState == 2: #Functions stopped (pacers, timers)				
				globals.runthreadrunning = False #MachineSuicide
			
			if configLoader.autoRecordStop > 0 and stopThreadholdPassed == False and globals.controlState < 2: # autoRecordStop > 0 means the user wants the camera to stop automatically
				if timeKeeper.timeCheck(globals.timePoint, int(configLoader.autoRecordStop), time.time()) == True:
					if globals.recording == True:
						stopThreadholdPassed = True


			sleep(0.016) #60 clock cycles per second

		#End of Loop
		
		if globals.error == False:
			if globals.goPro == True:
				goPro.disableLocate()

			if globals.abort == False:
				if globals.goPro == False:
					self.endThreadReset.emit()

				if globals.goPro == True:
					if configLoader.autoRecordStop > 1:
						self.autoRecordStop.emit()

			
		else:
			changeUIColour(self, (220, 16, 2))
			
			self.endThreadReset.emit()

			if globals.goPro == True:
				goPro.disableLocate()

			if globals.recording == True:
				goPro.stopShutter()
				sleep(2)
				goPro.WOL()
				self.keepalivethread.emit()

		print("[RUN] Thread Terminated")
		self.addToLogWindow.emit("[RUN] Thread Terminated", 'red')
