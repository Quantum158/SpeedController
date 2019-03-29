import sys, os
import time
from time import sleep
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

from PyQt5 import QtCore, QtGui, QtWidgets, uic

_translate = QtCore.QCoreApplication.translate
class Ui_MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(Ui_MainWindow, self).__init__()
		uic.loadUi("SpeedController.ui",self)

		self.setWindowInfo(Ui_MainWindow)
		self.pushController.clicked.connect(self.PrintMessage)

	def setWindowInfo(self, MainWindow):
		#MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		MainWindow.setWindowIcon(QtGui.QIcon(__location__ + os.path.sep + "Resources" + os.path.sep + "Icon.jpg"))

	def PrintMessage(self):
		print("Functioning")
		self.textStatus.setText(_translate("MainWindow", "Functioning"))

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = Ui_MainWindow()
	MainWindow.show()
	sys.exit(app.exec_())

