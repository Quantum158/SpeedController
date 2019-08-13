import time

class timeKeeper:
	
	def timeDif(timeStart, currentTime):
		#print(round(currentTime - timeStart, 2))
		return timeKeeper.timeConverter(currentTime - timeStart)
		

	def timeCheck(timeStart, waitTime, currentTime, exact = True):
		a = round(timeStart, 1)
		b = round(currentTime, 1)
		c = round(waitTime, 1)
		if exact == True:
			if (b - a) == c:
				#print(round(round(currentTime, 2) - round(timeStart, 2), 2))
				return True
			else:
				return False
		if exact == False:
			if (b - a) >= c:
				return True
			else:
				return False

	def counter(timeStart, currentTime, totalDelay):
		a = round(timeStart, 2)
		b = round(currentTime, 2)
		timePassed = b - a
		return round(totalDelay - timePassed, 1)

	def timeConverter(seconds):
		#f = miliseconds
		#s = seconds
		#m = minutes

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
		if len(str(f)) > 2:
			f = str(f)[:-1]
		return(str(m) + ":" + str(s) + "." + str(f))
