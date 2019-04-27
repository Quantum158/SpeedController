def init():
	global controlEnabled
	controlEnabled = True
	global runthreadrunning
	runthreadrunning = False

	global controlState
	controlState = 0

	global timePoint
	timePoint = 0
	print("Globals Initialized!")

	global timeAactive
	timeAactive = False
	global timeBactive
	timeBactive = False