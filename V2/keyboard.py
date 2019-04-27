import pygame
from pygame import key
from pygame.locals import *
pygame.init()
class InputCheck:

	def getLeftPressed():
		"""Function that returns a Boolean regarding if the left arrow key is pressed (and not left shift)"""
		leftShift = False
		mods = key.get_mods()
		if mods & KMOD_LSHIFT:
			leftShift = True
		if key.get_pressed()[K_LEFT] == True and leftShift == False:
			return True
		else: 
			return False

	def getRightPressed():
		"""Function that returns a Boolean regarding if the right arrow key is pressed (and not left shift)"""
		leftShift = False
		mods = key.get_mods()
		if mods & KMOD_LSHIFT:
			leftShift = True
		if key.get_pressed()[K_RIGHT] == True and leftShift == False:
			return True
		else: 
			return False

	def getLeftShiftPressed():
		"""Function that returns a Boolean regarding if the left arrow key and left shift are pressed at the same time"""
		leftShift = False
		mods = key.get_mods()
		if mods & KMOD_LSHIFT:
			leftShift = True
		if key.get_pressed()[K_LEFT] == True and leftShift == True:
			return True
		else: 
			return False

	def getRightShiftPressed():
		"""Function that returns a Boolean regarding if the right arrow key and left shift are pressed at the same time"""
		leftShift = False
		mods = key.get_mods()
		if mods & KMOD_LSHIFT:
			leftShift = True
		if key.get_pressed()[K_RIGHT] == True and leftShift == True:
			return True
		else: 
			return False