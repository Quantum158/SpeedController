#TESTING GIT


#														#
#-------------------Speed Timer  V1.0-------------------#
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

in_delayCheck = 2  #How long the system waits in seconds before starting countdown
in_cooldown = 3    #Time Lock in seconds after pedal is released

#-------------------------------------------------------#
#Global Variables
controlState = 0
framerate = 60
counter = 0
fontChange = 0
postcount = 0
done = False

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
from time import sleep
sleep(1)
import sys, os, datetime
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

from Submodules.controlChecks import *
from Submodules.textPrint import TextPrint
from Submodules.GUI import *
import globals

#Load Icon
icon = pygame.image.load(os.path.join(__location__, '.\Resources\Icon.jpg'))
pygame.display.set_icon(icon)

 #PreLoad Audio Playback
pygame.mixer.pre_init(22050, -16, 2, 2048)
	
#GUI Setup
BACKGROUNDDefault = (255,255,255)
ENDCOLOUR = (16, 220, 2)

size = [800,600]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Start System")

#Framerate Controller
clock = pygame.time.Clock()

#End GUI Setup

print("""
														
-----------Speed Timer - NO CONTROLLER V1.0------------
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
			counter = 0
			fontSize = 60
			fontChange = 0
			controlState = 2
	
	#Staged
	if controlState == 2 and buttonChecks.waitForSpace(False) == True:   #Locked in
		#AUDIO LOAD
		pygame.mixer.init()
		LowTone = pygame.mixer.Sound(os.path.join(__location__, '.\Resources\Sounds\LowTone.ogg'))
		HighTone = pygame.mixer.Sound(os.path.join(__location__, '.\Resources\Sounds\HighTone.ogg'))
		pygame.mixer.init()	
		


		if counter < ((framerate * 3) + (framerate / 2)):
			counter += 1
		
		#Font Shrink
		if counter >= (framerate / 2) and counter <= (framerate):
			globals.fontSize = 60 - (int(59/(int(framerate/2))*counter) - int(framerate/2))
		GUI.changeFont()
		#End Font Shrink

		if counter == framerate:
			#LowTone.play()
			print("Tone 1")
			
		if counter == (framerate * 2):
			#LowTone.play()
			print("Tone 2")
		
		if counter == (framerate * 3) and played == False:
			#HighTone.play()
			print("Tone 3")
			played = True
			
		if played == True and pygame.mixer.get_busy() != 1:
			controlState = 3
			counter = 0
			fontChange = 0
						
	#Timer Running / Waiting For Time Stop
	if controlState == 3:
		if pygame.mixer.get_init == 1:
			pygame.mixer.quit()
		#Font Size Reset
		if fontChange != framerate:
			fontChange += 1
			print(fontChange)
		if fontChange >= (framerate/2) and fontChange <= framerate and globals.fontSize != 60:
			globals.fontSize = 1 + (int(50/(int(framerate/2))*fontChange)- int(framerate/2))
			print(globals.fontSize)
		GUI.changeFont()
		#End Font Size Reset
		
		if lStop == False:
			lTime += 1
		if rStop == False:
			rTime += 1
		if lStop == False:
			if buttonChecks.getLeftPressed() == True:
				lStop = True
		if rStop == False:
			if buttonChecks.getRightPressed() == True:
				rStop = True
		if lStop == True and rStop == True and fontChange == framerate:
			controlState = 4
		leftDisplayTime = str(float("{0:.2f}".format(lTime / framerate)))
		rightDisplayTime = str(float("{0:.2f}".format(rTime / framerate)))

	#Both Timers Stopped / Waiting For Reset
	if controlState == 4:
		if buttonChecks.waitForSpace(False) == True:
			if cooldown > 0:
				cooldown -= 1
			postout = str(int(cooldown / framerate))

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
		GUI.GUI4(screen, ENDCOLOUR, leftDisplayTime, rightDisplayTime, cooldown, in_cooldown, postout)

	pygame.display.flip()

	clock.tick_busy_loop(framerate)

#END MAIN LOOP
print("Exited Loop!")	
pygame.quit()
