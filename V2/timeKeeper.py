import time
import datetime

class timeKeeper:
	
	def timeDif(timeStart, currentTime):
		#print(round(currentTime - timeStart, 2))
		return timeKeeper.timeConverter(currentTime - timeStart)
		

	def timeCheck(timeStart, waitTime, currentTime):
		if (round(round(currentTime, 2) - round(timeStart, 2), 1)) == waitTime:
			#print(round(round(currentTime, 2) - round(timeStart, 2), 2))
			return True
		else:
			return False

	def timeConverter(seconds):
		s, f = divmod(seconds, 1)
		m, s = divmod(s, 60)
		m = int(m)
		if len(str(m)) < 2:
			m = str(0) + str(m)
		s = int(s)
		if len(str(s)) < 2:
			s = str(0) + str(s)
		f = int(round(f, 2)*100)
		if len(str(f)) < 2:
			f = str(0) + str(f)
		print(str(m) + ":" + str(s) + "." + str(f))
		return(str(m) + ":" + str(s) + "." + str(f))