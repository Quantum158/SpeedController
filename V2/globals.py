def init():
	global StartEnabled
	StartEnabled = True

	global LControlEnabled
	LControlEnabled = True
	
	global RControlEnabled
	RControlEnabled = True

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