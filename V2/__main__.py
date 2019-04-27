import sys, os
import time
from time import sleep
import globals

time.sleep(1)
print(globals.thread1running)
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import pyqtSignal
_translate = QtCore.QCoreApplication.translate