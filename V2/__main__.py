import sys, os
import time
from time import sleep
import globals
globals.init()
import GUI
import configLoader
configLoader.init()

time.sleep(1)

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import pyqtSignal
_translate = QtCore.QCoreApplication.translate




if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = GUI.Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())