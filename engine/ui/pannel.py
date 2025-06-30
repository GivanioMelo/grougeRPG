import pygame
import engine.sprites as sprites
from engine.ui.Component import Component

_spriteSheet_= sprites.load("assets/ui/PanelTemplate.png",3,3)

class Pannel(Component):	
	_renderingBuffer_:pygame.Surface

	def __init__(self, **kwargs):
		self.x = kwargs.get('x', 0)
		self.y = kwargs.get('y', 0)
		self.width = kwargs.get('width', 100)
		self.height = kwargs.get('height', 100)
		self._renderingBuffer_ = None
		self.preRender()

	def draw(self,screen):
		if(self._renderingBuffer_ == None):
			print('no buffer rendered')
			return
		screen.blit(self._renderingBuffer_,(self.x,self.y))

	def preRender(self):
		if(_spriteSheet_ == None): print("no spritesheet"); return
		if(len(_spriteSheet_) < 3): print("no spritesheet");  return
		if(len(_spriteSheet_[0]) < 3): print("no spritesheet");  return

		self._renderingBuffer_ = pygame.Surface((self.width, self.height))

		spriteWidth = _spriteSheet_[0][0].get_width()
		spriteHeight = _spriteSheet_[0][0].get_height()

		if float(self.width / spriteWidth) < 1.5: print(float(self.width / spriteWidth)); return
		if float(self.height / spriteHeight) < 1.5: print(float(self.height / spriteHeight)); return

		tiledWidth = int(self.width / spriteWidth)
		tiledHeight = int(self.height / spriteHeight)

		if(tiledWidth < 1): print(tiledWidth);return
		if(tiledHeight < 1): print(tiledHeight);return

		for i in range(1,tiledWidth):
			for j in range(1,tiledHeight):
				self._renderingBuffer_.blit(_spriteSheet_[1][1], (i*spriteWidth,j*spriteHeight))

		for i in range(1,tiledWidth):
			self._renderingBuffer_.blit(_spriteSheet_[0][1], (i*spriteWidth,0))
			self._renderingBuffer_.blit(_spriteSheet_[2][1], (i*spriteWidth,self.height-spriteHeight))
		for j in range(1,tiledHeight):
			self._renderingBuffer_.blit(_spriteSheet_[1][0], (0,j*spriteHeight))
			self._renderingBuffer_.blit(_spriteSheet_[1][2], (self.width - spriteWidth,j*spriteHeight))

		self._renderingBuffer_.blit(_spriteSheet_[0][0], (0,0))
		self._renderingBuffer_.blit(_spriteSheet_[0][2], (self.width-spriteWidth,0))
		self._renderingBuffer_.blit(_spriteSheet_[2][0], (0,self.height-spriteHeight))
		self._renderingBuffer_.blit(_spriteSheet_[2][2], (self.width-spriteWidth,self.height-spriteHeight))