from typing import Any

import pygame

import engine.Config as config

from engine.Animation import Animation
from engine.Camera import Camera

class GameObject(pygame.sprite.Sprite):
	def __init__(self) -> None:
		super().__init__()

class GridGameObject(GameObject):
	def __init__(self,x=0,y=0) -> None:
		self.x = x
		self.y = y
	
	def getPosition(self):
		return self.x, self.y
	
	def getRenderPosition(self,camera:Camera):
		x_offset = camera.x_offset()
		y_offset = camera.y_offset()

		rx= (self.x + x_offset - camera.x) * config.TILE_SIZE
		ry= (self.y + y_offset - camera.y) * config.TILE_SIZE
		return rx, ry
	
	def getRect(self, camera:Camera):
		rx,ry = self.getRenderPosition(camera)
		return pygame.Rect(rx, ry,config.TILE_SIZE,config.TILE_SIZE)

	def update(self, *args: Any, **kwargs: Any) -> None:
		return super().update(*args, **kwargs)

	def isVisible(self, camera:Camera):
		x, y = self.getRenderPosition(camera)
		if x < 0: return False
		if y < 0: return False
		if x > camera.width*config.TILE_SIZE: return False
		if y > camera.height*config.TILE_SIZE: return False
		return True

	def draw(self, screen: pygame.Surface, camera:Camera):
		if self.isVisible(camera):
			screen.blit(self.image, self.getRect(camera))

class Rock(GridGameObject):
	def __init__(self,x=0,y=0) -> None:
		self.x = x
		self.y = y
		self.image = pygame.image.load('assets/objects/rock.png')