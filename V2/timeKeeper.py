import time
import datetime

class timeKeeper:
	
	def timeDif(timeStart, currentTime):
		#print(round(currentTime - timeStart, 2))
		return float(round(currentTime - timeStart, 2))

	def timeCheck(timeStart, waitTime, currentTime):
		if (round(round(currentTime, 2) - round(timeStart, 2), 1)) == waitTime:
			#print(round(round(currentTime, 2) - round(timeStart, 2), 2))
			return True
		else:
			return False