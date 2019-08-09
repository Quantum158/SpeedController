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

	global goProWarnings
	goProWarnings = False

	global goProFirstConnect
	goProFirstConnect = 0

	global recording
	recording = False

	global error
	error = False

	global abort
	abort = False

	global timeAactive
	timeAactive = False
	global timeBactive
	timeBactive = False
	print("Globals Initialized!")