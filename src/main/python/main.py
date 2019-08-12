import os
import sys

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import QtWidgets

from modules import resources

resources.init()

def getResources(appctxt):
	resources.stylesheet = appctxt.get_resource("style.qss")
	resources.lowTone = appctxt.get_resource("LowTone.ogg")
	resources.highTone = appctxt.get_resource("HighTone.ogg")
	resources.falseStart = appctxt.get_resource("FalseStart.ogg")
	resources.pacerTone = appctxt.get_resource("PacerTone.ogg")

if __name__ == "__main__":
	appctxt = ApplicationContext()		# 1. Instantiate ApplicationContext
	getResources(appctxt)
	import modules.GUILoad
	ui = modules.GUILoad.ApplicationWindow()
	ui.show()
	exit_code = appctxt.app.exec_()		# 2. Invoke appctxt.app.exec_()
	sys.exit(exit_code) 
