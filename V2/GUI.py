# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Benja\Source\Repos\Quantum158\SpeedController\V2\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
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
        self.MainLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.MainLayout.setContentsMargins(0, 0, 0, 0)
        self.MainLayout.setObjectName("MainLayout")
        self.AHalf = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.AHalf.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AHalf.setObjectName("AHalf")
        self.TimerALabel = QtWidgets.QLabel(self.AHalf)
        self.TimerALabel.setGeometry(QtCore.QRect(0, 0, 261, 51))
        self.TimerALabel.setStyleSheet("font: 40pt \"Calibri\";\n"
"text-decoration: underline;")
        self.TimerALabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TimerALabel.setObjectName("TimerALabel")
        self.TimerATime = QtWidgets.QLabel(self.AHalf)
        self.TimerATime.setGeometry(QtCore.QRect(0, 530, 261, 51))
        self.TimerATime.setStyleSheet("font: 40pt \"Calibri\";")
        self.TimerATime.setAlignment(QtCore.Qt.AlignCenter)
        self.TimerATime.setObjectName("TimerATime")
        self.AFalseStart = QtWidgets.QPushButton(self.AHalf)
        self.AFalseStart.setGeometry(QtCore.QRect(30, 70, 201, 61))
        self.AFalseStart.setStyleSheet("font: 16pt \"MS Shell Dlg 2\"; background-color: rgb(190, 190, 190);")
        self.AFalseStart.setObjectName("AFalseStart")
        self.AStopTime = QtWidgets.QPushButton(self.AHalf)
        self.AStopTime.setGeometry(QtCore.QRect(30, 460, 201, 61))
        self.AStopTime.setStyleSheet("font: 16pt \"MS Shell Dlg 2\"; background-color: rgb(190, 190, 190);")
        self.AStopTime.setObjectName("AStopTime")
        self.MainLayout.addWidget(self.AHalf)
        self.CentralUnit = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.CentralUnit.setEnabled(True)
        self.CentralUnit.setObjectName("CentralUnit")
        self.StatusLabel = QtWidgets.QLabel(self.CentralUnit)
        self.StatusLabel.setGeometry(QtCore.QRect(0, 0, 261, 51))
        self.StatusLabel.setStyleSheet("font: 40pt \"Calibri\";\n"
"text-decoration: underline;")
        self.StatusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.StatusLabel.setObjectName("StatusLabel")
        self.textStatus = QtWidgets.QLabel(self.CentralUnit)
        self.textStatus.setGeometry(QtCore.QRect(10, 60, 241, 81))
        self.textStatus.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.textStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.textStatus.setObjectName("textStatus")
        self.StatusControlLineSep = QtWidgets.QFrame(self.CentralUnit)
        self.StatusControlLineSep.setGeometry(QtCore.QRect(0, 140, 261, 21))
        self.StatusControlLineSep.setMinimumSize(QtCore.QSize(0, 0))
        self.StatusControlLineSep.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.StatusControlLineSep.setLineWidth(7)
        self.StatusControlLineSep.setFrameShape(QtWidgets.QFrame.HLine)
        self.StatusControlLineSep.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.StatusControlLineSep.setObjectName("StatusControlLineSep")
        self.pushController = QtWidgets.QPushButton(self.CentralUnit)
        self.pushController.setGeometry(QtCore.QRect(30, 190, 201, 61))
        self.pushController.setStyleSheet("font: 25pt \"MS Shell Dlg 2\";")
        self.pushController.setObjectName("pushController")
        self.ControllOptionLineSep = QtWidgets.QFrame(self.CentralUnit)
        self.ControllOptionLineSep.setGeometry(QtCore.QRect(0, 290, 261, 21))
        self.ControllOptionLineSep.setMinimumSize(QtCore.QSize(0, 0))
        self.ControllOptionLineSep.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ControllOptionLineSep.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.ControllOptionLineSep.setLineWidth(7)
        self.ControllOptionLineSep.setMidLineWidth(0)
        self.ControllOptionLineSep.setFrameShape(QtWidgets.QFrame.HLine)
        self.ControllOptionLineSep.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ControllOptionLineSep.setObjectName("ControllOptionLineSep")
        self.OptionsLabel = QtWidgets.QLabel(self.CentralUnit)
        self.OptionsLabel.setGeometry(QtCore.QRect(0, 310, 261, 51))
        self.OptionsLabel.setStyleSheet("font: 40pt \"Calibri\";\n"
"text-decoration: underline;")
        self.OptionsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.OptionsLabel.setObjectName("OptionsLabel")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.CentralUnit)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(0, 370, 261, 211))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.OptionsLayout = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.OptionsLayout.setContentsMargins(0, 0, 0, 0)
        self.OptionsLayout.setObjectName("OptionsLayout")
        self.checkATimerEnable = QtWidgets.QCheckBox(self.formLayoutWidget_2)
        self.checkATimerEnable.setObjectName("checkATimerEnable")
        self.OptionsLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkATimerEnable)
        self.checkBTimerEnable = QtWidgets.QCheckBox(self.formLayoutWidget_2)
        self.checkBTimerEnable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBTimerEnable.setIconSize(QtCore.QSize(16, 16))
        self.checkBTimerEnable.setObjectName("checkBTimerEnable")
        self.OptionsLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.checkBTimerEnable)
        self.OptionsTopLine = QtWidgets.QFrame(self.formLayoutWidget_2)
        self.OptionsTopLine.setMinimumSize(QtCore.QSize(15, 15))
        self.OptionsTopLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.OptionsTopLine.setLineWidth(2)
        self.OptionsTopLine.setMidLineWidth(0)
        self.OptionsTopLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.OptionsTopLine.setObjectName("OptionsTopLine")
        self.OptionsLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.OptionsTopLine)
        self.checkGoProCommands = QtWidgets.QCheckBox(self.formLayoutWidget_2)
        self.checkGoProCommands.setObjectName("checkGoProCommands")
        self.OptionsLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.checkGoProCommands)
        self.GoProWarningBeeps = QtWidgets.QCheckBox(self.formLayoutWidget_2)
        self.GoProWarningBeeps.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.GoProWarningBeeps.setObjectName("GoProWarningBeeps")
        self.OptionsLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.GoProWarningBeeps)
        self.RecordStopLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.RecordStopLabel.setObjectName("RecordStopLabel")
        self.OptionsLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.RecordStopLabel)
        self.RecordLayout = QtWidgets.QHBoxLayout()
        self.RecordLayout.setObjectName("RecordLayout")
        self.RecordSpin = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.RecordSpin.setKeyboardTracking(True)
        self.RecordSpin.setDisplayIntegerBase(10)
        self.RecordSpin.setObjectName("RecordSpin")
        self.RecordLayout.addWidget(self.RecordSpin)
        self.RecordSecondsLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.RecordSecondsLabel.setObjectName("RecordSecondsLabel")
        self.RecordLayout.addWidget(self.RecordSecondsLabel)
        self.OptionsLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.RecordLayout)
        self.OptionsMiddleLine = QtWidgets.QFrame(self.formLayoutWidget_2)
        self.OptionsMiddleLine.setMinimumSize(QtCore.QSize(15, 15))
        self.OptionsMiddleLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.OptionsMiddleLine.setLineWidth(2)
        self.OptionsMiddleLine.setMidLineWidth(0)
        self.OptionsMiddleLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.OptionsMiddleLine.setObjectName("OptionsMiddleLine")
        self.OptionsLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.OptionsMiddleLine)
        self.delayAfterStagingLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.delayAfterStagingLabel.setObjectName("delayAfterStagingLabel")
        self.OptionsLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.delayAfterStagingLabel)
        self.StageDelayLayout = QtWidgets.QHBoxLayout()
        self.StageDelayLayout.setObjectName("StageDelayLayout")
        self.StageDelaySpin = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.StageDelaySpin.setSuffix("")
        self.StageDelaySpin.setPrefix("")
        self.StageDelaySpin.setObjectName("StageDelaySpin")
        self.StageDelayLayout.addWidget(self.StageDelaySpin)
        self.DelaySecondsLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.DelaySecondsLabel.setObjectName("DelaySecondsLabel")
        self.StageDelayLayout.addWidget(self.DelaySecondsLabel)
        self.OptionsLayout.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.StageDelayLayout)
        self.OptionsBottomLine = QtWidgets.QFrame(self.formLayoutWidget_2)
        self.OptionsBottomLine.setMinimumSize(QtCore.QSize(15, 15))
        self.OptionsBottomLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.OptionsBottomLine.setLineWidth(2)
        self.OptionsBottomLine.setMidLineWidth(0)
        self.OptionsBottomLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.OptionsBottomLine.setObjectName("OptionsBottomLine")
        self.OptionsLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.OptionsBottomLine)
        self.PacerLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.PacerLabel.setObjectName("PacerLabel")
        self.OptionsLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.PacerLabel)
        self.PacerLayout = QtWidgets.QHBoxLayout()
        self.PacerLayout.setObjectName("PacerLayout")
        self.PacerBeepsSpin = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.PacerBeepsSpin.setKeyboardTracking(True)
        self.PacerBeepsSpin.setObjectName("PacerBeepsSpin")
        self.PacerLayout.addWidget(self.PacerBeepsSpin)
        self.PacerSecondsLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.PacerSecondsLabel.setObjectName("PacerSecondsLabel")
        self.PacerLayout.addWidget(self.PacerSecondsLabel)
        self.OptionsLayout.setLayout(8, QtWidgets.QFormLayout.FieldRole, self.PacerLayout)
        self.ControlOutlineBottom = QtWidgets.QFrame(self.CentralUnit)
        self.ControlOutlineBottom.setGeometry(QtCore.QRect(30, 240, 201, 21))
        self.ControlOutlineBottom.setStyleSheet("color: rgb(16, 220, 2);")
        self.ControlOutlineBottom.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ControlOutlineBottom.setLineWidth(3)
        self.ControlOutlineBottom.setFrameShape(QtWidgets.QFrame.HLine)
        self.ControlOutlineBottom.setObjectName("ControlOutlineBottom")
        self.ControlOutlineTop = QtWidgets.QFrame(self.CentralUnit)
        self.ControlOutlineTop.setGeometry(QtCore.QRect(30, 180, 201, 21))
        self.ControlOutlineTop.setStyleSheet("color: rgb(16, 220, 2);")
        self.ControlOutlineTop.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ControlOutlineTop.setLineWidth(3)
        self.ControlOutlineTop.setFrameShape(QtWidgets.QFrame.HLine)
        self.ControlOutlineTop.setObjectName("ControlOutlineTop")
        self.ControlOutlineRight = QtWidgets.QFrame(self.CentralUnit)
        self.ControlOutlineRight.setGeometry(QtCore.QRect(220, 190, 21, 61))
        self.ControlOutlineRight.setStyleSheet("color: rgb(16, 220, 2);")
        self.ControlOutlineRight.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ControlOutlineRight.setLineWidth(3)
        self.ControlOutlineRight.setFrameShape(QtWidgets.QFrame.VLine)
        self.ControlOutlineRight.setObjectName("ControlOutlineRight")
        self.ControlOutlineLeft = QtWidgets.QFrame(self.CentralUnit)
        self.ControlOutlineLeft.setGeometry(QtCore.QRect(20, 190, 21, 61))
        self.ControlOutlineLeft.setStyleSheet("color: rgb(16, 220, 2);")
        self.ControlOutlineLeft.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ControlOutlineLeft.setLineWidth(3)
        self.ControlOutlineLeft.setFrameShape(QtWidgets.QFrame.VLine)
        self.ControlOutlineLeft.setObjectName("ControlOutlineLeft")
        self.pushController.raise_()
        self.StatusLabel.raise_()
        self.textStatus.raise_()
        self.StatusControlLineSep.raise_()
        self.ControllOptionLineSep.raise_()
        self.OptionsLabel.raise_()
        self.formLayoutWidget_2.raise_()
        self.ControlOutlineBottom.raise_()
        self.ControlOutlineTop.raise_()
        self.ControlOutlineRight.raise_()
        self.ControlOutlineLeft.raise_()
        self.MainLayout.addWidget(self.CentralUnit)
        self.BHalf = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.BHalf.setEnabled(True)
        self.BHalf.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BHalf.setObjectName("BHalf")
        self.TimerBLabel = QtWidgets.QLabel(self.BHalf)
        self.TimerBLabel.setGeometry(QtCore.QRect(0, 0, 261, 51))
        self.TimerBLabel.setStyleSheet("font: 40pt \"Calibri\";\n"
"text-decoration: underline;")
        self.TimerBLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TimerBLabel.setObjectName("TimerBLabel")
        self.TimerBTime = QtWidgets.QLabel(self.BHalf)
        self.TimerBTime.setGeometry(QtCore.QRect(0, 530, 261, 51))
        self.TimerBTime.setStyleSheet("font: 40pt \"Calibri\";\n"
"")
        self.TimerBTime.setAlignment(QtCore.Qt.AlignCenter)
        self.TimerBTime.setObjectName("TimerBTime")
        self.BStopTime = QtWidgets.QPushButton(self.BHalf)
        self.BStopTime.setEnabled(True)
        self.BStopTime.setGeometry(QtCore.QRect(30, 460, 201, 61))
        self.BStopTime.setAutoFillBackground(False)
        self.BStopTime.setStyleSheet("font: 16pt \"MS Shell Dlg 2\"; background-color: rgb(190, 190, 190);")
        self.BStopTime.setAutoDefault(False)
        self.BStopTime.setDefault(False)
        self.BStopTime.setFlat(False)
        self.BStopTime.setObjectName("BStopTime")
        self.BFalseStart = QtWidgets.QPushButton(self.BHalf)
        self.BFalseStart.setGeometry(QtCore.QRect(40, 70, 201, 61))
        self.BFalseStart.setStyleSheet("font: 16pt \"MS Shell Dlg 2\"; background-color: rgb(190, 190, 190);")
        self.BFalseStart.setObjectName("BFalseStart")
        self.MainLayout.addWidget(self.BHalf)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Speed Controller"))
        self.TimerALabel.setText(_translate("MainWindow", "Timer A"))
        self.TimerATime.setText(_translate("MainWindow", "0:00.00"))
        self.AFalseStart.setText(_translate("MainWindow", "False Start\n"
"(Shift+Left Arrow)"))
        self.AStopTime.setText(_translate("MainWindow", "Stop Time\n"
"(Left Arrow)"))
        self.StatusLabel.setText(_translate("MainWindow", "Status"))
        self.textStatus.setText(_translate("MainWindow", "Ready..."))
        self.pushController.setText(_translate("MainWindow", "Start"))
        self.OptionsLabel.setText(_translate("MainWindow", "Options"))
        self.checkATimerEnable.setText(_translate("MainWindow", "Timer A Enabled"))
        self.checkBTimerEnable.setText(_translate("MainWindow", "Timer B Enabled"))
        self.checkGoProCommands.setText(_translate("MainWindow", "Use GoPro"))
        self.GoProWarningBeeps.setText(_translate("MainWindow", "Warning Beeps"))
        self.RecordStopLabel.setText(_translate("MainWindow", "Automatic Record Stop"))
        self.RecordSecondsLabel.setText(_translate("MainWindow", "Second(s)"))
        self.delayAfterStagingLabel.setText(_translate("MainWindow", "Delay After Staging"))
        self.DelaySecondsLabel.setText(_translate("MainWindow", "Second(s)"))
        self.PacerLabel.setText(_translate("MainWindow", "Pacer Beeps"))
        self.PacerSecondsLabel.setText(_translate("MainWindow", "Second(s)"))
        self.TimerBLabel.setText(_translate("MainWindow", "Timer B"))
        self.TimerBTime.setText(_translate("MainWindow", "0:00.00"))
        self.BStopTime.setText(_translate("MainWindow", "Stop Time\n"
"(Right Arrow)"))
        self.BFalseStart.setText(_translate("MainWindow", "False Start\n"
"(Shift+Right Arrow)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

