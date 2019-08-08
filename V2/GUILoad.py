from time import sleep
import globals
import run
import keepGoProAlive
from goPro import goPro
import configLoader
from GUI import Ui_MainWindow

import sys, os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import pyqtSignal, QTimer, QThread

_translate = QtCore.QCoreApplication.translate
class ApplicationWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(ApplicationWindow, self).__init__()

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.ui.pushController.clicked.connect(self.onStart)
		self.ui.checkATimerEnable.stateChanged.connect(self.TimerASetting)
		self.ui.checkBTimerEnable.stateChanged.connect(self.TimerBSetting)
		self.ui.checkGoProCommands.stateChanged.connect(self.goProSetting)
		self.ui.GoProWarningBeeps.stateChanged.connect(self.goProWarningSetting)
		self.ui.StageDelaySpin.valueChanged.connect(self.StageDelaySetting)
		#self.ui.CheckDelaySpin.valueChanged.connect(self.StageDelaySetting)
		self.ui.CooldownSpin.valueChanged.connect(self.CooldownDelaySetting)
		self.ui.PacerBeepsSpin.valueChanged.connect(self.PacerBeepsSetting)
		self.ui.AStopTime.clicked.connect(self.AStopTime)
		self.ui.BStopTime.clicked.connect(self.BStopTime)
		
		self.ui.GoProWarningBeeps.setEnabled(False)
		#self.ui.AFalseStart.clicked.connect(self.AFalseStart)
		#self.ui.BFalseStart.clicked.connect(self.BFalseStart)

		#QtCore.QMetaObject.connectSlotsByName(MainWindow)
		globals.StartEnabled = True

	def changeButtonText(self, text):
		self.ui.pushController.setText(_translate("MainWindow", text))
	
	def changeStatusText(self, text):
		self.ui.textStatus.setText(_translate("MainWindow", text))
	
	def setWindowInfo(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "Speed Controller"))
		MainWindow.setWindowIcon(QtGui.QIcon(__location__ + os.path.sep + "Resources" + os.path.sep + "Icon.jpg"))

	def TimerASetting(self):
		if self.ui.checkATimerEnable.isChecked():
			print("[Option] Timer A Checked")
			configLoader.TimeAEnabled = True
		else:
			print("[Option] Timer A Unchecked")
			configLoader.TimeAEnabled = False

	def TimerBSetting(self):
		if self.ui.checkBTimerEnable.isChecked():
			print("[Option] Timer B Checked")
			configLoader.TimeBEnabled = True
		else:
			print("[Option] Timer B Unchecked")
			configLoader.TimeBEnabled = False

	def goProSetting(self):
		if self.ui.checkGoProCommands.isChecked():
			def callback():
				self.goProKeepAlive()
			
			print("[Option] GoPro Checked")
			globals.goPro = True
			globals.keepaliverunning = True
			globals.goProFirstConnect = 1
			
			self.ui.pushController.setEnabled(False)
			self.ui.checkGoProCommands.setEnabled(False)
			self.changeButtonText("Working")
			self.changeStatusText("Connecting to\nGoPro...")
			self.ui.GoProWarningBeeps.setEnabled(True)

			timer = QTimer(self)
			timer.timeout.connect(callback)
			timer.setSingleShot(True)
			timer.start(200)

		else:
			print("[Option] GoPro UnChecked")
			globals.goPro = False
			globals.keepaliverunning = False
			self.ui.GoProWarningBeeps.setEnabled(False) #Disable Other GoPro Option
			self.ui.GoProWarningBeeps.setChecked(False)
			globals.goProWarnings = False
			globals.goProFirstConnect = 0

	def firstReply(self):
		globals.goProFirstConnect = 0
		self.ui.pushController.setEnabled(True)
		self.ui.checkGoProCommands.setEnabled(True)
		self.changeButtonText("Start")
		self.changeStatusText("Ready...")

	def goProWarningSetting(self):
		if self.ui.GoProWarningBeeps.isChecked():
			print("[Option] Warnings Checked")
			globals.goProWarnings = True
		else:
			print("[Option] Warnings UnChecked")
			globals.goProWarnings = False

	def StageDelaySetting(self, text): #Pre
		print("[Option] Stage Delay Value Changed: " + str(text))
		configLoader.delayStage = text

	def CheckDelaySetting(self, text): #Wait
		print("[Option] Check Delay Value Changed: " + str(text))
		configLoader.startCheck = text

	def CooldownDelaySetting(self, text): #Post
		print("[Option] Cooldown Delay Value Changed: " + str(text))
		configLoader.postCooldown = text

	def PacerBeepsSetting(self, text): #Pacer Beeps
		print("[Option] Pacer Beeps Value Changed: " + str(text))
		configLoader.PacerBeeps = text

	def AStopTime(self):
		if globals.LControlEnabled == True:
			globals.timeAactive = False

	def BStopTime(self):
		if globals.RControlEnabled == True:
			globals.timeBactive = False

	#def AFalseStart(self):


	#def BFalseStart(self):


	#---

	def onStart(self):
		if globals.StartEnabled == True:
			def callback():
				return self.worker.start()
			globals.StartEnabled = False
			globals.error = False
			self.ui.checkGoProCommands.setEnabled(False)
			self.ui.textStatus.setText(_translate("MainWindow", "Initializing..."))
			self.ui.pushController.setText(_translate("MainWindow", "Abort"))
			print("Running")


			self.worker = run.Run()
			self.worker.aTime.connect(self.aTimeUpdate)
			self.worker.aColour.connect(self.aColourUpdate)
			self.worker.bTime.connect(self.bTimeUpdate)
			self.worker.bColour.connect(self.bColourUpdate)
			self.worker.textStatus.connect(self.changeStatusText)
			self.worker.buttonText.connect(self.changeButtonText)
			self.worker.goProFail.connect(self.goProFail)
			self.worker.endThreadReset.connect(self.endThreadReset)
			self.worker.keepalivethread.connect(self.goProKeepAlive)

			timer = QTimer(self)
			timer.timeout.connect(callback)
			timer.setSingleShot(True)
			timer.start(500)
			return

		if globals.StartEnabled == False:	
			globals.runthreadrunning = False

			if globals.recording == 0:
				def callback():
					self.endThreadReset()
					self.ui.pushController.setEnabled(True)
					return

				self.changeStatusText("Aborting...")
				self.changeButtonText("Working")
				self.ui.pushController.setEnabled(False)
				print("Attempting to Stop")
				
				timer = QTimer(self)
				timer.timeout.connect(callback)
				timer.setSingleShot(True)
				timer.start(200)	
				return

			if globals.recording == 1:
				def callback():
					self.changeStatusText("Restarting\nCamera...")
					if goPro.cameraCheck() == True:
						goPro.forceToVideoMode()
						self.endThreadReset()
						globals.keepaliverunning = True
						self.goProKeepAlive()
					else:
						pass #Maybe do something in the future?

					self.endThreadReset()
					self.ui.pushController.setEnabled(True)

				self.changeStatusText("Stopping\nRecording...")
				self.changeButtonText("Working")
				self.ui.pushController.setEnabled(False)

				goPro.stopShutter()
				timer = QTimer(self)
				timer.timeout.connect(callback)
				timer.setSingleShot(True)
				timer.start(5000)		
				return			
		
	def aTimeUpdate(self, text):
		self.ui.TimerATime.setText(_translate("MainWindow", text))

	def aColourUpdate(self, colour):
		self.ui.AHalf.setStyleSheet("background-color: rgb" + colour +";")

	def bTimeUpdate(self, text):
		self.ui.TimerBTime.setText(_translate("MainWindow", text))

	def bColourUpdate(self, colour):
		self.ui.BHalf.setStyleSheet("background-color: rgb" + colour +";")

	def keyPressEvent(self, e):
		if e.key() == QtCore.Qt.Key_Escape:
			print("Escape!")
			sys.exit()

	def goProKeepAlive(self):		
		self.keepAlive = keepGoProAlive.Run()
		self.keepAlive.sendWOL.connect(self.WOLdialog)
		self.keepAlive.firstReply.connect(self.firstReply)
		return self.keepAlive.start()

	def goProFail(self):
		error_dialog = QtWidgets.QMessageBox()
		error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
		error_dialog.setText("GoPro connection failed!\nCheck your Wifi Connection")
		error_dialog.setWindowTitle("Error")
		error_dialog.exec_()

	def goProRecover(self):
		pass_dialog = QtWidgets.QMessageBox()
		pass_dialog.setText("GoPro connection re-established!")
		pass_dialog.setWindowTitle("Success")
		pass_dialog.exec_()

	def goProIgnore(self):
		ignore_dialog = QtWidgets.QMessageBox()
		ignore_dialog.setText("GoPro will now be disabled to prevent further error messages")
		ignore_dialog.setWindowTitle("Disabling GoPro")
		ignore_dialog.exec_()
		self.ui.checkGoProCommands.setChecked(False)

	def endThreadReset(self):
		def callback():
			globals.StartEnabled = True
			self.ui.checkGoProCommands.setEnabled(True)
			self.changeButtonText("Start")
			self.changeStatusText("Ready...")
			
		globals.timePoint = 0
		globals.error = False
		globals.runthreadrunning = False
		globals.controlState = -1

		timer = QTimer(self)
		timer.timeout.connect(callback)
		timer.setSingleShot(True)
		timer.start(1000)
	
	def WOLdialog(self):
		WOL_dialog = QtWidgets.QMessageBox()
		buttonReply = QtWidgets.QMessageBox.question(
			self, "GoPro Connection Lost", "Would you like to attempt to re-establish connection by sending a WOL command?")
		if buttonReply == QtWidgets.QMessageBox.Yes:
			def callback():
				if goPro.WOL() == True:
					self.goProRecover()
					self.ui.pushController.setEnabled(True)
					self.changeButtonText("Start")
					self.changeStatusText("Ready...")
					if globals.goProFirstConnect == 1:
						self.firstReply()
				else:
					self.goProFail()
					self.ui.pushController.setEnabled(True)
					self.ui.checkGoProCommands.setEnabled(True)
					self.ui.checkGoProCommands.setChecked(False)
					self.changeButtonText("Start")
					self.changeStatusText("Ready...")
				return 

			self.changeStatusText("Attempting to\nwake camera...")
			self.changeButtonText("Working")
			self.ui.pushController.setEnabled(False)
			
			timer = QTimer(self)
			timer.timeout.connect(callback)
			timer.setSingleShot(True)
			timer.start(200)
		else:
			self.goProIgnore()
			self.ui.pushController.setEnabled(True)
			self.ui.checkGoProCommands.setEnabled(True)
			self.changeButtonText("Start")
			self.changeStatusText("Ready...")
		


class MainWindow(ApplicationWindow, QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self, parent=parent)
		ApplicationWindow()
					

