import os
import sys
from time import sleep

import modules.LogGUI
import modules.configLoader
import modules.globals
import modules.GUI
import modules.keepGoProAlive
import modules.run
from modules.goPro import goPro
from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, QTimer, pyqtSignal

globals = modules.globals

run = modules.run
keepGoProAlive = modules.keepGoProAlive
configLoader = modules.configLoader

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


_translate = QtCore.QCoreApplication.translate
def initMainUI(appWindow):
	appWindow.ui = modules.GUI.Ui_MainWindow()
	appWindow.ui.setupUi(appWindow)

	appWindow.ui.pushController.clicked.connect(appWindow.onStart)
	appWindow.ui.checkATimerEnable.stateChanged.connect(appWindow.TimerASetting)
	appWindow.ui.checkBTimerEnable.stateChanged.connect(appWindow.TimerBSetting)
	appWindow.ui.checkGoProCommands.stateChanged.connect(appWindow.goProSetting)
	appWindow.ui.GoProWarningBeeps.stateChanged.connect(appWindow.goProWarningSetting)
	appWindow.ui.RecordSpin.valueChanged.connect(appWindow.autoRecordStopSetting)
	appWindow.ui.StageDelaySpin.valueChanged.connect(appWindow.StageDelaySetting)
	appWindow.ui.PacerBeepsSpin.valueChanged.connect(appWindow.PacerBeepsSetting)
	appWindow.ui.AStopTime.clicked.connect(appWindow.AStopTime)
	appWindow.ui.BStopTime.clicked.connect(appWindow.BStopTime)
	appWindow.ui.OpenLogPush.clicked.connect(appWindow.openLogWindow)

	appWindow.ui.GoProWarningBeeps.setEnabled(False)
	appWindow.ui.RecordSpin.setEnabled(False)

	#Temp because I can't be bothered to do keyboard stuff
	#appWindow.ui.AStopTime.setEnabled(False)
	#appWindow.ui.AStopTime.setText(_translate("MainWindow", "Disabled"))
	appWindow.ui.AStopTime.setText(_translate("MainWindow", "Stop Time"))
	#appWindow.ui.BStopTime.setEnabled(False)
	#appWindow.ui.BStopTime.setText(_translate("MainWindow", "Disabled"))
	appWindow.ui.BStopTime.setText(_translate("MainWindow", "Stop Time"))
	appWindow.ui.AFalseStart.setEnabled(False)
	appWindow.ui.AFalseStart.setText(_translate("MainWindow", "Disabled"))
	appWindow.ui.BFalseStart.setEnabled(False)
	appWindow.ui.BFalseStart.setText(_translate("MainWindow", "Disabled"))

	#appWindow.ui.AFalseStart.clicked.connect(appWindow.AFalseStart)
	#appWindow.ui.BFalseStart.clicked.connect(appWindow.BFalseStart)

	qssFile = "modules\style.qss"
	with open(qssFile, "r") as ss:
		appWindow.setStyleSheet(ss.read())

	appWindow.setWindowTitle(_translate("MainWindow", "Speed Controller"))
	appWindow.setWindowIcon(QtGui.QIcon(os.path.join(__location__, "Resources", "Icon2.jpg")))

class ApplicationWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(ApplicationWindow, self).__init__()
		initMainUI(self)
		
		globals.StartEnabled = True

	def changeButtonText(self, text):
		self.ui.pushController.setText(_translate("MainWindow", text))
	
	def changeStatusText(self, text):
		self.ui.textStatus.setText(_translate("MainWindow", text))
	
	def setPushControllerState(self, state):
		if state == True:
			self.ui.pushController.setEnabled(True)
			self.ui.pushController.setStyleSheet("font: 25pt \"MS Shell Dlg 2\";\nborder: 3px solid green;")

		if state == False:
			self.ui.pushController.setEnabled(False)
			self.ui.pushController.setStyleSheet("font: 25pt \"MS Shell Dlg 2\";\nborder: 3px solid red;")

	def setGoProOptionsState(self, state):
		"""State: 0-All Disabled, 1-Just Main Disabled, 2-All But Main Enabled, 3-All Enabled"""
		if state == 3: #Enable All GoPro Options
			self.ui.GoProWarningBeeps.setEnabled(True)
			self.ui.RecordSpin.setEnabled(True)
			self.ui.checkGoProCommands.setEnabled(True)

		if state == 2: #Enable All but main, Disable Main
			self.ui.GoProWarningBeeps.setEnabled(True)
			self.ui.RecordSpin.setEnabled(True)
			self.ui.checkGoProCommands.setEnabled(False)
			
		if state == 1: #Disable All but main, reset main
			self.ui.checkGoProCommands.setEnabled(True)
			self.ui.checkGoProCommands.setChecked(False)
			self.ui.GoProWarningBeeps.setEnabled(False)
			self.ui.GoProWarningBeeps.setChecked(False)
			self.ui.RecordSpin.setEnabled(False)
			self.ui.RecordSpin.setValue(0)

		if state == 0: #Disable All GoPro Options
			self.ui.GoProWarningBeeps.setEnabled(False)
			self.ui.RecordSpin.setEnabled(False)
			self.ui.GoProWarningBeeps.setChecked(False)
			self.ui.RecordSpin.setValue(0)
			self.ui.checkGoProCommands.setEnabled(False)
			self.ui.checkGoProCommands.setChecked(False)

	def setOptionsState(self, state):
		if state == True: #Enable All (Selectively With GoPro)
			self.ui.checkATimerEnable.setEnabled(True)
			self.ui.checkBTimerEnable.setEnabled(True)
			self.ui.StageDelaySpin.setEnabled(True)
			self.ui.PacerBeepsSpin.setEnabled(True)
			self.ui.checkGoProCommands.setEnabled(True)
			if self.ui.checkGoProCommands.isChecked() == True:
				self.ui.RecordSpin.setEnabled(True)
				self.ui.GoProWarningBeeps.setEnabled(True)
		if state == False: #Disble All
			self.ui.checkATimerEnable.setEnabled(False)
			self.ui.checkBTimerEnable.setEnabled(False)
			self.ui.checkGoProCommands.setEnabled(False)
			self.ui.GoProWarningBeeps.setEnabled(False)
			self.ui.RecordSpin.setEnabled(False)
			self.ui.StageDelaySpin.setEnabled(False)
			self.ui.PacerBeepsSpin.setEnabled(False)

	def TimerASetting(self):
		if self.ui.checkATimerEnable.isChecked():
			self.addToLogWindow("[Option] Timer A Checked", 'purple')
			print("[Option] Timer A Checked")
			configLoader.TimeAEnabled = True
		else:
			self.addToLogWindow("[Option] Timer A Unchecked", 'purple')
			print("[Option] Timer A Unchecked")
			configLoader.TimeAEnabled = False

	def TimerBSetting(self):
		if self.ui.checkBTimerEnable.isChecked():
			self.addToLogWindow("[Option] Timer B Checked", 'purple')
			print("[Option] Timer B Checked")
			configLoader.TimeBEnabled = True
		else:
			self.addToLogWindow("[Option] Timer B Unchecked", 'purple')
			print("[Option] Timer B Unchecked")
			configLoader.TimeBEnabled = False

	def goProSetting(self):
		if self.ui.checkGoProCommands.isChecked():
			def callback():
				self.goProKeepAlive()
			
			print("[Option] GoPro Checked")
			self.addToLogWindow("[Option] GoPro Checked", 'purple')
			globals.goPro = True
			globals.keepaliverunning = True
			globals.goProFirstConnect = 1
			
			self.setPushControllerState(False)
			self.setGoProOptionsState(2)
			self.changeButtonText("Working")
			self.changeStatusText("Connecting to\nGoPro...")
			self.ui.GoProWarningBeeps.setEnabled(True)

			timer = QTimer(self)
			timer.timeout.connect(callback)
			timer.setSingleShot(True)
			timer.start(200)

		else:
			print("[Option] GoPro UnChecked")
			self.addToLogWindow("[Option] GoPro UnChecked", 'purple')
			globals.goPro = False
			self.addToLogWindow("[MAIN] Keep Alive Thread Termination Cued", 'orange')
			globals.keepaliverunning = False
			self.setGoProOptionsState(1)
			globals.goProWarnings = False
			globals.goProFirstConnect = 0

	def firstReply(self):
		globals.goProFirstConnect = 0
		self.setPushControllerState(True)
		self.setGoProOptionsState(3)
		self.changeButtonText("Start")
		self.changeStatusText("Ready...")

	def goProWarningSetting(self):
		if self.ui.GoProWarningBeeps.isChecked():
			print("[Option] Camera Warnings Checked")
			self.addToLogWindow("[Option] Camera Warnings Checked", 'purple')
			globals.goProWarnings = True
		else:
			print("[Option] Warnings UnChecked")
			self.addToLogWindow("[Option] Camera Warnings Unchecked", 'purple')
			globals.goProWarnings = False

	def autoRecordStopSetting(self, value):
		if value == 1:
			self.ui.RecordSpin.setSuffix("    Second")
		else:
			self.ui.RecordSpin.setSuffix("   Seconds")
		print("[Option] Auto Record Stop Value Changed: {}".format(str(value)))
		self.addToLogWindow("[Option] Auto Record Stop Value Changed{}".format(str(value)), 'purple')
		configLoader.autoRecordStop = value

	def StageDelaySetting(self, value): #Pre
		if value == 1:
			self.ui.StageDelaySpin.setSuffix("    Second")
		else:
			self.ui.StageDelaySpin.setSuffix("   Seconds")
		print("[Option] Stage Delay Value Changed: {}".format(str(value)))
		self.addToLogWindow("[Option] Stage Delay Value Changed{}".format(str(value)), 'purple')
		configLoader.delayStage = value

	def PacerBeepsSetting(self, value): #Pacer Beeps
		if value == 1:
			self.ui.PacerBeepsSpin.setSuffix("    Second")
		else:
			self.ui.PacerBeepsSpin.setSuffix("   Seconds")
		print("[Option] Pacer Beeps Value Changed: {}".format(str(value)))
		self.addToLogWindow("[Option] Pacer Beeps Value Changed{}".format(str(value)), 'purple')
		configLoader.PacerBeeps = value

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
			if globals.keepaliverunning == True:
				print("[MAIN] Keep Alive Thread Termination Cued")
				self.addToLogWindow("[MAIN] Keep Alive Thread Termination Cued", 'orange')
				globals.keepaliverunning = False #Disable keep alive thread for gopro
			globals.StartEnabled = False
			globals.abort = False
			globals.error = False
			self.setOptionsState(False)
			self.changeStatusText("Initializing")
			self.changeButtonText("Abort")

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
			self.worker.autoRecordStop.connect(self.autoRecordStop)
			self.worker.addToLogWindow.connect(self.addToLogWindow)

			self.addToLogWindow("[MAIN] Booting Run Thread", 'green')
			timer = QTimer(self)
			timer.timeout.connect(callback)
			timer.setSingleShot(True)
			timer.start(500)
			return

		if globals.StartEnabled == False:
			print("[MAIN] Run Thread Termination Cued")
			self.addToLogWindow("[MAIN] Run Thread Termination Cued", 'orange')
			globals.runthreadrunning = False
			globals.abort = True
			if globals.recording == False:
				def callback():
					self.endThreadReset()
					return
				
				self.changeStatusText("Aborting...")
				self.changeButtonText("Working")
				self.setPushControllerState(False)
				
				timer = QTimer(self)
				timer.timeout.connect(callback)
				timer.setSingleShot(True)
				timer.start(200)	
				return

			if globals.recording == True:
				def callback():
					self.changeStatusText("Restarting\nCamera...")
					sleep(0.2)
					if goPro.cameraCheck() == True:
						goPro.forceToVideoMode()
						self.endThreadReset()
						globals.keepaliverunning = True
						self.goProKeepAlive()
					else:
						pass #Maybe do something in the future?

					self.endThreadReset()

				self.addToLogWindow("[MAIN] Stopping Recording ", 'orange')
				self.changeStatusText("Stopping\nRecording...")
				self.changeButtonText("Working")
				self.setPushControllerState(False)

				goPro.stopShutter()
				globals.recording = False #Incase GoPro accidentally entered phantom record state
				timer = QTimer(self)
				timer.timeout.connect(callback)
				timer.setSingleShot(True)
				timer.start(5000)		
				return			
	
	def autoRecordStop(self):
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

		self.addToLogWindow("[MAIN] Stopping Recording ", 'orange')
		self.changeStatusText("Stopping\nRecording...")
		self.changeButtonText("Working")
		self.setPushControllerState(False)

		goPro.stopShutter()
		timer = QTimer(self)
		timer.timeout.connect(callback)
		timer.setSingleShot(True)
		timer.start(5000)		
		return			
	
	def aTimeUpdate(self, text):
		self.ui.TimerATime.setText(_translate("MainWindow", text))

	def aColourUpdate(self, colour):
		self.ui.AColourDisplay.setStyleSheet("background-color: rgb" + colour +";")

	def bTimeUpdate(self, text):
		self.ui.TimerBTime.setText(_translate("MainWindow", text))

	def bColourUpdate(self, colour):
		self.ui.BColourDisplay.setStyleSheet("background-color: rgb" + colour +";")

	def keyPressEvent(self, e):
		if e.key() == QtCore.Qt.Key_Escape:
			print("Escape!")
			sys.exit()

	def goProKeepAlive(self):		
		self.keepAlive = keepGoProAlive.Run()
		self.keepAlive.sendWOL.connect(self.WOLdialog)
		self.keepAlive.firstReply.connect(self.firstReply)
		self.keepAlive.toLog.connect(self.addToLogWindow)
		return self.keepAlive.start()

	def goProFail(self):
		error_dialog = QtWidgets.QMessageBox()
		error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
		error_dialog.setText("GoPro connection failed!\nCheck your Wifi Connection")
		error_dialog.setWindowTitle("Error")
		error_dialog.exec_()

	def goProRecover(self):
		pass_dialog = QtWidgets.QMessageBox()
		if globals.goProFirstConnect == 1:
			pass_dialog.setText("GoPro connection established!")
		else:
			pass_dialog.setText("GoPro connection re-established!")
		pass_dialog.setWindowTitle("Success")
		pass_dialog.exec_()

	def goProIgnore(self):
		ignore_dialog = QtWidgets.QMessageBox()
		ignore_dialog.setText("GoPro will now be disabled to prevent further error messages")
		ignore_dialog.setWindowTitle("Disabling GoPro")
		ignore_dialog.exec_()
		self.setGoProOptionsState(1)

	def endThreadReset(self):
		def callback():
			globals.StartEnabled = True
			self.setPushControllerState(True)
			self.setOptionsState(True)
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
					self.addToLogWindow("[KEEP ALIVE] Connection Established", 'green')
					print("[KEEP ALIVE] Connection Established")
					self.goProRecover()
					self.setPushControllerState(True)
					self.changeButtonText("Start")
					self.changeStatusText("Ready...")
					if globals.goProFirstConnect == 1:
						self.firstReply()
					keepGoProAlive.Run.loopHold = False
				else:
					print("KEEP ALIVE] Connection Failed")
					self.addToLogWindow("[KEEP ALIVE] Connection Failed", 'red')
					keepGoProAlive.Run.loopHold = False
					self.goProFail()
					self.setPushControllerState(True)
					self.setGoProOptionsState(1)
					self.changeButtonText("Start")
					self.changeStatusText("Ready...")
				return 

			self.addToLogWindow("[KEEP ALIVE] Sending WOL command", 'orange')
			print("[KEEP ALIVE] Sending WOL command")
			self.changeStatusText("Attempting to\nwake camera...")
			self.changeButtonText("Working")
			self.setPushControllerState(False)
			
			timer = QTimer(self)
			timer.timeout.connect(callback)
			timer.setSingleShot(True)
			timer.start(200)
		else:
			keepGoProAlive.Run.loopHold = False
			self.goProIgnore()
			self.setPushControllerState(True)
			self.setGoProOptionsState(1)
			self.changeButtonText("Start")
			self.changeStatusText("Ready...")


	def openLogWindow(self):
		if globals.logOpen == False:
			globals.logOpen = True
			self.logWindow = LogWindow()
			self.logWindow.show()

	def addToLogWindow(self, text, colour = None):
		if globals.logOpen == True:
			if colour == None:
				addItemToLogList(self.logWindow, text)
			else:
				addItemToLogList(self.logWindow, text, colour)
		
		else:
			pass #Don't add to log ui as it isn't open

	def closeEvent(self, event):
		if globals.logOpen == True:
			self.logWindow.close()
			
		event.accept()

#Log Window Specific

def addItemToLogList(LogWindowClass, text, colour = None):
	newItem = QtWidgets.QListWidgetItem()
	newItem.setText(text)
	if colour != None:
		colours = dict(
			green = '#11dc02', 
			blue = '#0059ff', 
			lightblue = '#00aaff', 
			orange = '#ffbf00', 
			red = '#dc1102',
			purple = '#a600a3'
		)
		if colour in colours.keys():
			colour = colours[colour]
		else:
			colour = "#ffffff"
		brush = QtGui.QBrush(QtGui.QColor(colour))
		brush.setStyle(QtCore.Qt.SolidPattern)
		newItem.setBackground(brush)

	LogWindowClass.ui.LogList.addItem(newItem)

class LogWindow(QtWidgets.QMainWindow):  # Class for Log Window
	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self, parent=parent)
		self.ui = modules.LogGUI.Ui_MainWindow()
		self.ui.setupUi(self)

		self.setWindowTitle(_translate("MainWindow", "Speed Controller Log"))
		self.setWindowIcon(QtGui.QIcon(os.path.join(__location__, "Resources", "Icon2.jpg")))

		self.ui.LogList.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n")
		#addItemToLogList(self, "Beginning of Log")

	def closeEvent(self, event):
		event.accept()
		globals.logOpen = False

