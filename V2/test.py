import sys, os
import time
from time import sleep
import globals
import run
import configLoader
from GUI2 import Ui_MainWindow

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import pyqtSignal

_translate = QtCore.QCoreApplication.translate
class ApplicationWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(ApplicationWindow, self).__init__()

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.ui.pushController.clicked.connect(self.onStart)
		self.ui.checkATimerEnable.stateChanged.connect(self.TimerASetting)
		self.ui.checkBTimerEnable.stateChanged.connect(self.TimerBSetting)
		self.ui.StageDelaySpin.valueChanged.connect(self.StageDelaySetting)
		#self.ui.CheckDelaySpin.valueChanged.connect(self.StageDelaySetting)
		self.ui.CooldownSpin.valueChanged.connect(self.CooldownDelaySetting)
		self.ui.AStopTime.clicked.connect(self.AStopTime)
		self.ui.BStopTime.clicked.connect(self.BStopTime)
		#self.ui.AFalseStart.clicked.connect(self.AFalseStart)
		#self.ui.BFalseStart.clicked.connect(self.BFalseStart)

		#QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def setWindowInfo(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "Speed Controller"))
		MainWindow.setWindowIcon(QtGui.QIcon(__location__ + os.path.sep + "Resources" + os.path.sep + "Icon.jpg"))

	def TimerASetting(self):
		if self.ui.checkATimerEnable.isChecked():
			print("Timer A Checked")
			configLoader.TimeAEnabled = True
		else:
			print("Timer A Unchecked")
			configLoader.TimeAEnabled = False

	def TimerBSetting(self):
		if self.ui.checkBTimerEnable.isChecked():
			print("Timer B Checked")
			configLoader.TimeBEnabled = True
		else:
			print("Timer B Unchecked")
			configLoader.TimeBEnabled = False

	def StageDelaySetting(self, text): #Pre
		print("Stage Delay Value Changed: " + str(text))
		configLoader.delayStage = text

	def CheckDelaySetting(self, text): #Wait
		print("Check Delay Value Changed: " + text)
		configLoader.startCheck = text

	def CooldownDelaySetting(self, text): #Post
		print("Cooldown Delay Value Changed: " + text)
		configLoader.postCooldown = text

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
			globals.StartEnabled = False
			self.ui.textStatus.setText(_translate("MainWindow", "Initializing..."))
			self.ui.pushController.setText(_translate("MainWindow", "Abort"))
			print("Running")
			self.run = run.Run()
			self.run.aTime.connect(self.aTimeUpdate)
			self.run.aColour.connect(self.aColourUpdate)
			self.run.bTime.connect(self.bTimeUpdate)
			self.run.bColour.connect(self.bColourUpdate)
			self.run.textStatus.connect(self.textStatusUpdate)
			return self.run.start()


		if globals.StartEnabled == False:
			self.ui.textStatus.setText(_translate("MainWindow", "Aborting..."))
			print("Attempting to Stop")
			globals.runthreadrunning = False
			globals.controlState = -1
			time.sleep(1)
			globals.StartEnabled = True
			self.ui.textStatus.setText(_translate("Mainwindow", "Ready..."))
			return self.ui.pushController.setText(_translate("MainWindow", "Start"))
	
	def aTimeUpdate(self, text):
		self.ui.TimerATime.setText(_translate("MainWindow", text))

	def aColourUpdate(self, colour):
		self.ui.widget.setStyleSheet("background-color: rgb" + colour +";")

	def bTimeUpdate(self, text):
		self.ui.TimerBTime.setText(_translate("MainWindow", text))

	def bColourUpdate(self, colour):
		self.ui.widget_2.setStyleSheet("background-color: rgb" + colour +";")

	def textStatusUpdate(self, text):
		self.ui.textStatus.setText(_translate("MainWindow", text))


class MainWindow(ApplicationWindow, QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self, parent=parent)
		ApplicationWindow()
					
	def keyPressEvent(self, e):
		if e.key() == QtCore.Qt.Key_Escape:
			print("Escape!")
			sys.exit()

#def main():
#	app = QtWidgets.QApplication(sys.argv)
#	application = MainWindow()
#	application.show()
#	sys.exit(app.exec_())



#if __name__ == "__main__":
#	main()