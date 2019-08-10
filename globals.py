import datetime
import time
def initialize():
	global fontSize
	fontSize = 60
	global timeStart
	timeStart = time.time()
	global timePoint
	timePoint = 0
	global timeEnd
	timeEnd = 0

	global lTime
	lTime = 0
	global rTime
	rTime = 0

	global lUse
	lUse = 0
	global rUse
	rUse = 0

	global waitAferStage
	waitAfterStage = 10