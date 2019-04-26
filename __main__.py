#-----------Speed Timer - NO CONTROLLER V1.5------------#
#-------------Written By Benjamin MacDonald-------------#
#														#
#-------------------------Usage-------------------------#
#														#
#Below are some varibles that can be set. Refer to the	#
#descriptors beside each value for reference on what	#
#they all do.											#
#														#
#Then run 'Speed.bat' 									#
#														#
#NOTE: For optimal results, set priority to REALTIME	#
#														#
#														#
#-------------------------------------------------------#

#------------------Variable Assignment------------------#

in_delayCheck = 2		    #How long the system waits in seconds before starting countdown
in_cooldown = 2			    #Time Lock in seconds after pedal is released
delayAfterStage = input("Delay After Staging? ")  #Should the system wait after the a start is staged (useful for when you need to start the countdown and then get on the wall)


if delayAfterStage == "yes" or delayAfterStage == "y" or delayAfterStage == "true":
	delayAfterStage = True
else:
	delayAfterStage = False
#-------------------------------------------------------#
#Control Variables
controlState = 0
framerate = 60
counter = 0
fontChange = 0
postcount = 0
done = False
stage2 = False

#Per Lane Variables
lTime = 0
rTime = 0
lStop = False
rStop = False
#Text Display Varibles
postout = 0

#Audio Control Varbiable
played = False

cooldown = in_cooldown * framerate + framerate
delayCheck = in_delayCheck * framerate
#-------------------------------------------------------#

import pygame
pygame.init()
import time
import datetime
from time import sleep
sleep(1)
import sys, os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

from Submodules.controlChecks import *
from Submodules.textPrint import TextPrint
from Submodules.GUI import *
from Submodules.timeKeeper import *
import globals

globals.lUse = input("Use Left Timer? ") #Should the left timer be displayed?
globals.rUse = input("Use Right Timer? ") # Should the right timer be displayed?
if globals.lUse == "yes" or globals.lUse == "y" or globals.lUse == "true":
	globals.lUse = True
else:
	globals.lUse = False

if globals.rUse == "yes" or globals.rUse == "y" or globals.rUse == "true":
	globals.rUse = True
else:
	globals.rUse = False
print(globals.lUse)
print(globals.rUse)


#Load Icon
icon = pygame.image.load(os.path.join(__location__, '.\Resources\Icon.jpg'))
pygame.display.set_icon(icon)

 #PreLoad Audio Playback
pygame.mixer.pre_init(22050, -16, 2, 2048)
	
#GUI Setup
BACKGROUNDDefault = (255,255,255)
ENDCOLOUR = (16, 220, 2)

size = [800,600]
#size = [1600,600]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Start System")

#Framerate Controller
clock = pygame.time.Clock()

#End GUI Setup

print("""
														
-----------Speed Timer - NO CONTROLLER V1.5------------
-------------Written By Benjamin MacDonald-------------
															  
-------------------------Usage-------------------------

Press "space" on your keyboard to to trigger
a start sequence.

Because controller events are not necessary, this code
will not detect false starts, it will only play start tones

-------------------------------------------------------

""")

#MAIN LOOP

#--Control States:--
#--   0: Waiting for Input --
#--   1: Input Detected, fufilling delay --
#--   2: Staged
#--	  3: Timer Running / Waiting for Time Stop
#--   4: Cooldown / Waiting for Restart

while not done:
	#EVENT HANDELER
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done=True
	#END EVENT HANDELER
	
	#Waiting For Input
	if controlState == 0 or controlState == 1:
		if buttonChecks.getSpacePressed() == True:
			if counter == 0:
				print("Counter Started")
				controlState = 1
			counter += 1
			GUIRecolour = [255,255,255]
			GUIRecolour[0] = 255 - (int(255/delayCheck*counter))
			GUIRecolour[1] = 255 - (int(166/delayCheck*counter))
		
		if buttonChecks.getSpacePressed() == False and controlState == 1:
			counter = 0
			print("Counter Reset")
			controlState = 0
		
		if counter == delayCheck:
			print("Delay Satisfied!")
			if delayAfterStage == True:
				globals.timePoint = time.time()
				print("Setting Stage Delay")
			else:
				stage2 = True
			counter = 0
			fontSize = 60
			fontChange = 0
			playState = 0
			controlState = 2
	
	#Staged
	if controlState == 2 and delayAfterStage == True:
		if timeKeeper.timeCheck(globals.timePoint, 10, time.time()):
			stage2 = True
			globals.timePoint = 0
			print("Delay after Stage Satisfied! Starting Countdown")

	if controlState == 2 and buttonChecks.waitForSpace(False) == True and stage2 == True:
		if globals.timePoint == 0:
			globals.timePoint = time.time()
			#print(globals.timePoint)

		#AUDIO LOAD
		pygame.mixer.init()
		LowTone = pygame.mixer.Sound(os.path.join(__location__, '.\Resources\Sounds\LowTone.ogg'))
		HighTone = pygame.mixer.Sound(os.path.join(__location__, '.\Resources\Sounds\HighTone.ogg'))
		FalseStart = pygame.mixer.Sound(os.path.join(__location__, '.\Resources\Sounds\FalseStart.ogg'))
		pygame.mixer.init()	
		
		#Font Shrink
		if fontChange < framerate:
			fontChange += 1
		if fontChange >= (framerate / 2) and fontChange <= (framerate):
			globals.fontSize = 60 - (int(59/(int(framerate/2))*fontChange) - int(framerate/2))

		GUI.changeFont()
		#End Font Shrink

		if timeKeeper.timeCheck(globals.timePoint, 1.00, time.time()) == True and playState == 0:
			LowTone.play()
			playState = 1 
			print("Tone 1")
			
		if timeKeeper.timeCheck(globals.timePoint, 2.00, time.time()) == True and playState == 1:
			LowTone.play()
			playState = 2 
			print("Tone 2")
		
		if timeKeeper.timeCheck(globals.timePoint, 3.00, time.time()) == True and playState == 2:
			HighTone.play()
			playState = 3
			print("Tone 3")
			played = True
			
		if played == True and pygame.mixer.get_busy() != 1:
			controlState = 3
			globals.timePoint = 0
			fontChange = 0
			lFalse = False
			rFalse = False
						
	#Timer Running / Waiting For Time Stop
	if controlState == 3:

		if globals.timePoint == 0:
			globals.timePoint = time.time()
			#print(globals.timePoint)

		#Font Size Reset
		if fontChange != framerate:
			fontChange += 1
		if fontChange >= (framerate/2) and fontChange <= framerate and globals.fontSize != 60:
			globals.fontSize = 1 + (int(50/(int(framerate/2))*fontChange)- int(framerate/2))
		GUI.changeFont()
		#End Font Size Reset
		
		#Manual False Indicator
		if buttonChecks.getLeftShiftPressed() == True and lStop == False:
			lStop = True
			lFalse = True
			FalseStart.play()
		
		if buttonChecks.getRightShiftPressed() == True and rStop == False:
			rStop = True
			rFalse = True
			FalseStart.play()
		#END Manual False Indicator

		#Time Updater
		if lStop == False:
			globals.lTime = timeKeeper.timeDif(globals.timePoint, time.time())
		if rStop == False:
			globals.rTime = timeKeeper.timeDif(globals.timePoint, time.time())
		#END Time Updater

		#Regular Stop Time
		if lStop == False:
			if buttonChecks.getLeftPressed() == True and lFalse == False:
				lStop = True
		if rStop == False:
			if buttonChecks.getRightPressed() == True and rFalse == False:
				rStop = True
		#END Regular Stop Time

		#Moving On
		if lStop == True and rStop == True and fontChange == framerate:
			controlState = 4
		
		#Text Out
		if lFalse == False:
			leftDisplayTime = str(float(globals.lTime))
		else:
			leftDisplayTime = "False Start"
		if rFalse == False:
			rightDisplayTime = str(float(globals.rTime))
		else:
			rightDisplayTime = "False Start"

	#Both Timers Stopped / Waiting For Reset
	if controlState == 4:
		if buttonChecks.waitForSpace(False) == True:
			if cooldown > 0:
				cooldown -= 1
				postout = str(int(cooldown / framerate))
		else:
			postout = "Release Spacebar!"
			

		#Reset
		if cooldown == 0:
			if buttonChecks.getSpacePressed() == True:
				#Variable Reset
				cooldown = in_cooldown * framerate + framerate
				postcount = 0
				postout = 0
				counter = 0
				played = False
				lStop = False
				rStop = False
				lTime = 0
				rTime = 0
				fontChange = 0
				fontSize = 60
				textPrint.changeFont()
				controlState = 1
				stage2 = False
				globals.timePoint = 0
				print("Reset")
		
	#GUI
	if controlState == 0:
		GUI.GUI0(screen, BACKGROUNDDefault)
		
	if controlState == 1:
		GUI.GUI1(screen, GUIRecolour, counter, framerate)

	if controlState == 2:
		GUI.GUI2(screen, GUIRecolour, counter, framerate, controlState)

	if controlState == 3:
		GUI.GUI3(screen, ENDCOLOUR, leftDisplayTime, rightDisplayTime)

	if controlState == 4:
		GUI.GUI4(screen, ENDCOLOUR, leftDisplayTime, rightDisplayTime, cooldown, in_cooldown, postout, framerate)

	pygame.display.flip()

	clock.tick_busy_loop(framerate)

#END MAIN LOOP
print("Exited Loop!")	
pygame.quit()
