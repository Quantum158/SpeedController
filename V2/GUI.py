import sys, os
import time
from time import sleep
import globals
import run
import configLoader

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import pyqtSignal
_translate = QtCore.QCoreApplication.translate

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		globals.controlEnabled = True

		sig = pyqtSignal(str)
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(800, 600)
		MainWindow.setMinimumSize(QtCore.QSize(800, 600))
		MainWindow.setMaximumSize(QtCore.QSize(800, 600))
		MainWindow.setMouseTracking(False)
		MainWindow.setTabletTracking(False)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setEnabled(True)
		self.centralwidget.setMinimumSize(QtCore.QSize(800, 600))
		self.centralwidget.setMaximumSize(QtCore.QSize(800, 600))
		self.centralwidget.setObjectName("centralwidget")
		self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
		self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 621))
		self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
		self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")

		#Timer A Label
		self.widget = QtWidgets.QWidget(self.horizontalLayoutWidget)
		self.widget.setStyleSheet("background-color: rgb(0, 0, 255);")
#		self.widget.setStyleSheet("background-color: rgb(0, 0, 0);")
		self.widget.setObjectName("widget")
		self.TimerALabel = QtWidgets.QLabel(self.widget)
		self.TimerALabel.setGeometry(QtCore.QRect(0, 0, 261, 51))
		self.TimerALabel.setStyleSheet("font: 40pt \"Calibri\";\n"
"text-decoration: underline;")
		self.TimerALabel.setAlignment(QtCore.Qt.AlignCenter)
		self.TimerALabel.setObjectName("TimerALabel")
		
		#Timer A Timer
		self.TimerATime = QtWidgets.QLabel(self.widget)
		self.TimerATime.setGeometry(QtCore.QRect(0, 530, 261, 51))
		self.TimerATime.setStyleSheet("font: 40pt \"Calibri\";")
		self.TimerATime.setAlignment(QtCore.Qt.AlignCenter)
		self.TimerATime.setObjectName("TimerATime")

		
		#Status Label
		self.horizontalLayout_3.addWidget(self.widget)
		self.widget_3 = QtWidgets.QWidget(self.horizontalLayoutWidget)
		self.widget_3.setObjectName("widget_3")
		self.StatusLabel = QtWidgets.QLabel(self.widget_3)
		self.StatusLabel.setGeometry(QtCore.QRect(0, 0, 261, 51))
		self.StatusLabel.setStyleSheet("font: 40pt \"Calibri\";\n"
"text-decoration: underline;")
		self.StatusLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.StatusLabel.setObjectName("StatusLabel")
		
		#Status Text
		self.textStatus = QtWidgets.QLabel(self.widget_3)
		self.textStatus.setGeometry(QtCore.QRect(10, 60, 241, 81))
		self.textStatus.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
		self.textStatus.setAlignment(QtCore.Qt.AlignCenter)
		self.textStatus.setObjectName("textStatus")
		self.line = QtWidgets.QFrame(self.widget_3)
		self.line.setGeometry(QtCore.QRect(0, 140, 261, 21))
		self.line.setMinimumSize(QtCore.QSize(0, 0))
		self.line.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
		self.line.setLineWidth(7)
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		
		#Control Button
		self.pushController = QtWidgets.QPushButton(self.widget_3)
		self.pushController.setGeometry(QtCore.QRect(30, 190, 201, 61))
		self.pushController.setStyleSheet("font: 25pt \"MS Shell Dlg 2\";")
		self.pushController.setObjectName("pushController")
		self.line_2 = QtWidgets.QFrame(self.widget_3)
		self.line_2.setGeometry(QtCore.QRect(0, 290, 261, 21))
		self.line_2.setMinimumSize(QtCore.QSize(0, 0))
		self.line_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
		self.line_2.setLineWidth(7)
		self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		
		#Options Label
		self.OptionsLabel = QtWidgets.QLabel(self.widget_3)
		self.OptionsLabel.setGeometry(QtCore.QRect(0, 320, 261, 51))
		self.OptionsLabel.setStyleSheet("font: 40pt \"Calibri\";\n"
"text-decoration: underline;")
		self.OptionsLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.OptionsLabel.setObjectName("OptionsLabel")
		self.formLayoutWidget_2 = QtWidgets.QWidget(self.widget_3)
		self.formLayoutWidget_2.setGeometry(QtCore.QRect(0, 380, 261, 151))
		self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
		self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
		self.formLayout_2.setContentsMargins(0, 0, 0, 0)
		self.formLayout_2.setObjectName("formLayout_2")
		
		#Options
		#-------

		#A Time Enable
		self.checkATimerEnable = QtWidgets.QCheckBox(self.formLayoutWidget_2)
		self.checkATimerEnable.setObjectName("checkATimerEnable")
		self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.checkATimerEnable)
		self.checkATimerEnable.stateChanged.connect(self.TimerASetting)

		#B Time Enable
		self.checkBTimerEnable = QtWidgets.QCheckBox(self.formLayoutWidget_2)
		self.checkBTimerEnable.setObjectName("checkBTimerEnable")
		self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkBTimerEnable)
		self.checkBTimerEnable.stateChanged.connect(self.TimerBSetting)

		#Delay After Staging
		self.delayAfterStagingLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
		self.delayAfterStagingLabel.setObjectName("delayAfterStagingLabel")
		self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.delayAfterStagingLabel)
		self.textStageDelay = QtWidgets.QLineEdit(self.formLayoutWidget_2)
		self.textStageDelay.setObjectName("textStageDelay")
		self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textStageDelay)
		self.line_3 = QtWidgets.QFrame(self.formLayoutWidget_2)
		self.line_3.setMinimumSize(QtCore.QSize(15, 15))
		self.line_3.setLineWidth(100)
		self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_3.setObjectName("line_3")
		self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.line_3)
		self.textStageDelay.textChanged.connect(self.StageDelaySetting)

		#Check Delay
		#self.checkDelayLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
		#self.checkDelayLabel.setObjectName("checkDelayLabel")
		#self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.checkDelayLabel)
		#self.textCheckDelay = QtWidgets.QLineEdit(self.formLayoutWidget_2)
		#self.textCheckDelay.setObjectName("textCheckDelay")
		#self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.textCheckDelay)
		#self.textCheckDelay.textChanged.connect(self.CheckDelaySetting)

		#Cooldown
		self.cooldownDelayLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
		self.cooldownDelayLabel.setObjectName("cooldownDelayLabel")
		self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.cooldownDelayLabel)
		self.textCooldown = QtWidgets.QLineEdit(self.formLayoutWidget_2)
		self.textCooldown.setObjectName("textCooldown")
		self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.textCooldown)
		self.horizontalLayout_3.addWidget(self.widget_3)
		self.textCooldown.textChanged.connect(self.CooldownDelaySetting)
		
		#----

		#Timer B Label
		self.widget_2 = QtWidgets.QWidget(self.horizontalLayoutWidget)
#		self.widget_2.setStyleSheet("background-color: rgb(0, 0, 255);")
		self.widget_2.setStyleSheet("background-color: rgb(0, 0, 0);")
		self.widget_2.setObjectName("widget_2")
		self.TimerBLabel = QtWidgets.QLabel(self.widget_2)
		self.TimerBLabel.setGeometry(QtCore.QRect(0, 0, 261, 51))
		self.TimerBLabel.setStyleSheet("font: 40pt \"Calibri\";\n"
"text-decoration: underline;")
		self.TimerBLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.TimerBLabel.setObjectName("TimerBLabel")
		
		#Timer B Timer
		self.TimerBTime = QtWidgets.QLabel(self.widget_2)
		self.TimerBTime.setGeometry(QtCore.QRect(0, 530, 261, 51))
		self.TimerBTime.setStyleSheet("font: 40pt \"Calibri\";")
		self.TimerBTime.setAlignment(QtCore.Qt.AlignCenter)
		self.TimerBTime.setObjectName("TimerBTime")
		self.horizontalLayout_3.addWidget(self.widget_2)
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		self.setWindowInfo(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		self.pushController.clicked.connect(self.onStart)

	def retranslateUi(self, MainWindow):
		self.TimerALabel.setText(_translate("MainWindow", "Timer A"))
		self.TimerATime.setText(_translate("MainWindow", "0:00.00"))
		self.StatusLabel.setText(_translate("MainWindow", "Status"))
		self.textStatus.setText(_translate("MainWindow", "Ready..."))
		self.pushController.setText(_translate("MainWindow", "Start"))
		self.OptionsLabel.setText(_translate("MainWindow", "Options"))
		self.checkATimerEnable.setText(_translate("MainWindow", "Timer A Enabled"))
		self.checkBTimerEnable.setText(_translate("MainWindow", "Timer B Enabled"))
		self.delayAfterStagingLabel.setText(_translate("MainWindow", "Delay After Staging"))
		self.textStageDelay.setText(_translate("MainWindow", str(configLoader.delayStage)))
	#	self.checkDelayLabel.setText(_translate("MainWindow", "Start Check Delay"))
	#	self.textCheckDelay.setText(_translate("MainWindow", str(configLoader.startCheck)))
		self.cooldownDelayLabel.setText(_translate("MainWindow", "Cooldown Delay"))
		self.textCooldown.setText(_translate("MainWindow", str(configLoader.postCooldown)))
		self.TimerBLabel.setText(_translate("MainWindow", "Timer B"))
		self.TimerBTime.setText(_translate("MainWindow", "0:00.00"))

	def setWindowInfo(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "Speed Controller"))
		MainWindow.setWindowIcon(QtGui.QIcon(__location__ + os.path.sep + "Resources" + os.path.sep + "Icon.jpg"))
	
	#---
	def TimerASetting(self):
		if self.checkATimerEnable.isChecked():
			print("Timer A Checked")
			configLoader.TimeAEnabled = True
		else:
			print("Timer A Unchecked")
			configLoader.TimeAEnabled = False

	def TimerBSetting(self):
		if self.checkBTimerEnable.isChecked():
			print("Timer B Checked")
			configLoader.TimeBEnabled = True
		else:
			print("Timer B Unchecked")
			configLoader.TimeBEnabled = False

	def StageDelaySetting(self, text): #Pre
		print("Stage Delay Value Changed: " + text)
		configLoader.delayStage = text

	def CheckDelaySetting(self, text): #Wait
		print("Check Delay Value Changed: " + text)
		configLoader.startCheck = text

	def CooldownDelaySetting(self, text): #Post
		print("Cooldown Delay Value Changed: " + text)
		configLoader.postCooldown = text
	#---

	def onStart(self):
		if globals.controlEnabled == True:
			globals.controlEnabled = False
			self.textStatus.setText(_translate("MainWindow", "Initializing..."))
			self.pushController.setText(_translate("MainWindow", "Abort"))
			print("Running")
			self.run = run.Run()
			self.run.aTime.connect(self.aTimeUpdate)
			self.run.aColour.connect(self.aColourUpdate)
			self.run.bTime.connect(self.bTimeUpdate)
			self.run.bColour.connect(self.bColourUpdate)
			self.run.textStatus.connect(self.textStatusUpdate)
			return self.run.start()


		if globals.controlEnabled == False:
			print("Attempting to Stop")
			globals.runthreadrunning = False
			globals.controlState = -1
			time.sleep(1)
			globals.controlEnabled = True
			return self.pushController.setText(_translate("MainWindow", "Start"))
	
	def aTimeUpdate(self, text):
		self.TimerATime.setText(_translate("MainWindow", text))

	def aColourUpdate(self, colour):
		self.widget.setStyleSheet("background-color: rgb" + colour +";")

	def bTimeUpdate(self, text):
		self.TimerBTime.setText(_translate("MainWindow", text))

	def bColourUpdate(self, colour):
		self.widget_2.setStyleSheet("background-color: rgb" + colour +";")

	def textStatusUpdate(self, text):
		self.textStatus.setText(_translate("MainWindow", text))