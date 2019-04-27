import config
def init():
	#Timers
	global TimeAEnabled 
	TimeAEnabled = config.enabledTimers['TimerA']
	global TimeBEnabled 
	TimeBEnabled = config.enabledTimers['TimerB']
	#QOL
	global delayStage 
	delayStage = config.delays['Delay_After_Staging'] #How long the app waits until beginning tone sequence
	global startCheck 
	startCheck = config.delays['Start_Check_Delay'] #How long the user must hold spacebar before locking in (likely deprecated)
	global postCooldown 
	postCooldown = config.delays['Post_Sequence_Cooldown'] #How long the app waits after a sequence has been completed