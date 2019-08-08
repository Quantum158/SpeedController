import pygame
import globals
globals.initialize()
DISPLAY = (0,0,0)
class TextPrint():
	"""Very Basic GUI render stuff"""
	def __init__(self):
		self.reset()
		self.font = pygame.font.Font(None, globals.fontSize)
	
	def changeFont(self):
		self.reset()
		self.font = pygame.font.Font(None, globals.fontSize)
	
	def print(self, screen, textString):
		textBitmap = self.font.render(textString, True, DISPLAY)
		screen.blit(textBitmap, [self.x, self.y])
		self.y += self.line_height

	def reset(self):
		self.x = 10
		self.y = 10
		self.line_height = 60