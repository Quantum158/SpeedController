import pygame
from pygame.locals import *
class buttonChecks:
	#Keyboard button checks

	def getFocus():
		"""Function that returns a Boolean regarding if the window is focussed or not"""
		if pygame.key.get_focused == True:
			return True
		else:
			return False

	def getSpacePressed():
		"""Function that returns a Boolean based on whether or not the spacebar is pressed"""
		if pygame.key.get_pressed()[K_SPACE] == True:
			return True
		else: 
			return False

	def getLeftPressed():
		"""Function that returns a Boolean regarding if the left arrow key is pressed (and not left shift)"""
		leftShift = False
		mods = pygame.key.get_mods()
		if mods & KMOD_LSHIFT:
			leftShift = True
		if pygame.key.get_pressed()[K_LEFT] == True and leftShift == False:
			return True
		else: 
			return False

	def getRightPressed():
		"""Function that returns a Boolean regarding if the right arrow key is pressed (and not left shift)"""
		leftShift = False
		mods = pygame.key.get_mods()
		if mods & KMOD_LSHIFT:
			leftShift = True
		if pygame.key.get_pressed()[K_RIGHT] == True and leftShift == False:
			return True
		else: 
			return False

	def getLeftShiftPressed():
		"""Function that returns a Boolean regarding if the left arrow key and left shift are pressed at the same time"""
		leftShift = False
		mods = pygame.key.get_mods()
		if mods & KMOD_LSHIFT:
			leftShift = True
		if pygame.key.get_pressed()[K_LEFT] == True and leftShift == True:
			return True
		else: 
			return False

	def getRightShiftPressed():
		"""Function that returns a Boolean regarding if the right arrow key and left shift are pressed at the same time"""
		leftShift = False
		mods = pygame.key.get_mods()
		if mods & KMOD_LSHIFT:
			leftShift = True
		if pygame.key.get_pressed()[K_RIGHT] == True and leftShift == True:
			return True
		else: 
			return False

	def waitForSpace(waitState):
		"""Function that returns a Boolean based on the spacebar a required state"""
		if buttonChecks.getSpacePressed() == waitState:
			return True
		else:
			return False

class controllerChecks:
	#Controller/Joystick Tests

	def hatCheck(target, requirement):
		"""Function that returns a Boolean based on a target hat and a required state for that button"""
		if Controller.get_hat(target) == requirement:
			return True	
		else:
			return False
	
	def buttonCheck(target, requirement):
		"""Function that returns a Boolean based on a target button and a required state for that button"""
		if Controller.get_button(target) == requirement:
			return True	
		else:
			return False