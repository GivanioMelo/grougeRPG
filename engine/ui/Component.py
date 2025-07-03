import pygame

class Component:
	x:float
	y:float
	width:float
	height:float

	def __init__(self, x=0.0, y=0.0, width=100.0, height=100.0, parent=None, visible=True):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.parent = parent
		self.visible = visible
	
	def get_x(self): return self.x
	def set_x(self,value): self.x = value

	def get_y(self): return self.y
	def set_y(self, value): self.y = value

	def get_width(self): return self.width
	def set_width(self,value): self.width = value

	def get_height(self): return self.height
	def set_height(self,value): self.height = value

	def update(self):
		# This class is intended to be a base class, so it doesn't implement any specific update logic.
		# Instead, it provides a default update method that does nothing.
		# Subclasses should override this method to implement specific update behavior.
		pass

	def draw(self,surface:pygame.Surface):
		if not self.visible: return
		if self.width <= 0 or self.height <= 0: return
		# This class is intended to be a base class, so it doesn't implement any specific drawing logic.
		# Instead, it provides a default drawing method that fills the area with white.
		# Subclasses should override this method to implement specific drawing behavior.
		surface.fill((255, 255, 255), (self.x, self.y, self.width, self.height))