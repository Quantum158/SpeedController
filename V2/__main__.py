import sys, os
import time
from time import sleep
import globals
globals.init()
import GUI
import configLoader
configLoader.init()
import test
time.sleep(1)

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import pyqtSignal
_translate = QtCore.QCoreApplication.translate




if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	#ui = GUI.MainWindow()
	ui = test.MainWindow()
	ui.show()
	sys.exit(app.exec_())