from math import floor
import pygame
import engine.Config as config

class Camera():
	def __init__(self,x,y,w,h) -> None:
		self.x = x
		self.y = y
		self.width = w
		self.height = h

	def setPosition(self,x,y):
		self.x = x
		self.y = y
	
	def x_offset(self):
		return int(floor(self.width/2))
	def y_offset(self):
		return int(floor(self.height/2))

	def getPosition(self):
		return self.x, self.y

	def getSize(self):
		return self.width, self.height

	def getRenderSize(self):
		rw = self.width * config.TILE_SIZE
		rh = self.height * config.TILE_SIZE
		return rw,rh

	def rect(self):
		return pygame.Rect(self.x, self.y,self.width,self.height)