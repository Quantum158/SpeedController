import globals
globals.init()
import configLoader
configLoader.init()

from time import sleep
import GUILoad
sleep(1)

import sys, os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import pyqtSignal





if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	ui = GUILoad.ApplicationWindow()
	ui.show()
	sys.exit(app.exec_())