import pygame

class Component:
	__x:float
	__y:float
	__width:float
	__height:float

	def __init__(self, **kwargs):
		self.__x = kwargs.get('x', 0.0)
		self.__y = kwargs.get('y', 0.0)
		self.__width = kwargs.get('width', 100.0)
		self.__height = kwargs.get('height', 100.0)
		self.parent = kwargs.get('parent', None)
		self.visible = kwargs.get('visible', True)
	
	def get_x(self): return self.__x
	def set_x(self,value): self.__x = value

	def get_y(self): return self.__y
	def set_y(self, value): self.__y = value

	def get_width(self): return self.__width
	def set_width(self,value): self.__width = value

	def get_height(self): return self.__height
	def set_height(self,value): self.__height = value

	def update(self):
		# This class is intended to be a base class, so it doesn't implement any specific update logic.
		# Instead, it provides a default update method that does nothing.
		# Subclasses should override this method to implement specific update behavior.
		pass

	def draw(self,surface:pygame.Surface):
		if not self.visible: return
		if self.__width <= 0 or self.__height <= 0: return
		# This class is intended to be a base class, so it doesn't implement any specific drawing logic.
		# Instead, it provides a default drawing method that fills the area with white.
		# Subclasses should override this method to implement specific drawing behavior.
		surface.fill((255, 255, 255), (self.__x, self.__y, self.__width, self.__height))