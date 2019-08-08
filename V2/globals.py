def init():
	global StartEnabled
	StartEnabled = True

	global LControlEnabled
	LControlEnabled = True
	
	global RControlEnabled
	RControlEnabled = True

	global runthreadrunning
	runthreadrunning = False

	global keepaliverunning
	keepaliverunning = False

	global controlState
	controlState = 0

	global timePoint
	timePoint = 0

	global goPro
	goPro = False

	global recording
	recording = False

	global error
	error = False

	global timeAactive
	timeAactive = False
	global timeBactive
	timeBactive = False
	print("Globals Initialized!")