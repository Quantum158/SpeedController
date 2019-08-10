import modules.config
config = modules.config
def init():
	#Timers
	global TimeAEnabled 
	TimeAEnabled = config.enabledTimers['TimerA']
	global TimeBEnabled 
	TimeBEnabled = config.enabledTimers['TimerB']
	#QOL
	global delayStage 
	delayStage = config.delays['Delay_After_Staging'] #How long the app waits until beginning tone sequence
	global PacerBeeps
	PacerBeeps = config.delays['PacerBeeps'] #Pacer Beeps
	global autoRecordStop
	autoRecordStop = config.delays['Auto_Record_Stop']
	print("[SYS] Config Initialized!")