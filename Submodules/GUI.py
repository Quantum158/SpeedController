from Submodules.textPrint import TextPrint
from Submodules.controlChecks import buttonChecks
import globals
textPrint = TextPrint()

class GUI:
	def GUI0(screen, colour):
		textPrint.reset()
		screen.fill(colour)
		textPrint.print(screen, "Waiting for Spacebar...")
		
	def GUI1(screen, colour, counter, framerate):
		textPrint.reset()
		screen.fill(colour)
		dot = "."
		dots = dot * int(counter / framerate)
		textPrint.print(screen, "Detected{}".format(str(dots)))

	def GUI2(screen, colour, counter, framerate, controlState):
		textPrint.reset()
		if counter != (framerate * 3) and controlState != 5:
			screen.fill(colour)
		if buttonChecks.waitForSpace(False) == False:
			textPrint.print(screen, "Please release the Spacebar...")
		textPrint.print(screen, "Staged!")

	def GUI3(screen, colour, leftDisplayTime, rightDisplayTime):
		textPrint.reset()
		screen.fill(colour)
		if globals.lUse == True:
			textPrint.print(screen, "Left Lane Time: {}".format(leftDisplayTime))
		else:
			textPrint.print(screen, "Left Lane Time: Offline")
		if globals.rUse == True:
			textPrint.print(screen, "Right Lane Time: {}".format(rightDisplayTime))
		else:
			textPrint.print(screen, "Right Lane Time: Offline")

	def GUI4(screen, colour, leftDisplayTime, rightDisplayTime, cooldown, in_cooldown, postout, framerate):
		textPrint.reset()
		screen.fill(colour)
		if globals.lUse == True:
			textPrint.print(screen, "Left Lane Time: {}".format(leftDisplayTime))
		else:
			textPrint.print(screen, "Left Lane Time: Offline")
		if globals.rUse == True:
			textPrint.print(screen, "Right Lane Time: {}".format(rightDisplayTime))
		else:
			textPrint.print(screen, "Right Lane Time: Offline")

		if cooldown == in_cooldown * framerate + framerate:
			textPrint.print(screen, "Cooldown: Please release the Spacebar")
		if cooldown > 0 and cooldown != (in_cooldown * framerate + framerate):
			textPrint.print(screen, "Cooldown: {} Seconds".format(postout)) #I need to fix this eventually
		if cooldown == 0:
			textPrint.print(screen, "")
			textPrint.print(screen, "")
			textPrint.print(screen, "")
			textPrint.print(screen, "")
			textPrint.print(screen, "")
			textPrint.print(screen, "")
			textPrint.print(screen, "")
			textPrint.print(screen, "Waiting for Spacebar...")

	def changeFont():
		textPrint.reset()
		textPrint.changeFont()

		