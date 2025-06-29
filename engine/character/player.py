from math import floor
import engine.Config as config

import pygame
from engine.Animation import Animation
from engine.Camera import Camera

from engine.character.Character import Character
from engine.interactions.quest import Quest

class Player(Character):
	idleAnimation:Animation
	animation:Animation

	activeQuests:list[Quest]
	completedQuests:list[Quest]

	def __init__(self, x, y) -> None:
		super().__init__()
		self.x = x
		self.y = y
		self.camera = Camera(self.x, self.y, config.CAMERA_WIDTH, config.CAMERA_HEIGHT)
		
		self.animation = None
		self.idleAnimation = None

	def update(self):
		if not self.idleAnimation: self.idleAnimation = Animation.fromFile("archer_idle.png")
		if not self.animation: self.animation = self.idleAnimation
		
		self.camera.setPosition(self.x,self.y)
		self.animation.update(30)
	
	def getRenderPosition(self):
		x_offset = self.camera.x_offset()
		y_offset = self.camera.y_offset()
		rx= int(x_offset) * config.TILE_SIZE
		ry= int(y_offset) * config.TILE_SIZE
		return rx, ry
	
	def getRect(self):
		rx,ry = self.getRenderPosition()
		return pygame.Rect(rx, ry,48,48)
	
	def draw(self, surface:pygame.Surface):
		surface.blit(self.animation.get_current_frame(),self.getRect())

	def useSkill(skillId:str):
		pass