import pygame

class Component:
	__x:float
	__y:float
	__width:float
	__height:float

	def __init__(self, x:float = 0, y:float=0, width:float=0, height:float=0):
		self.__x = x
		self.__y = y
		self.__width = width
		self.__height = height

		self.parent = None
	
	def get_x(self): return self.__x
	def set_x(self,value): self.__x = value

	def get_y(self): return self.__y
	def set_y(self, value): self.__y = value

	def get_width(self): return self.__width
	def set_width(self,value): self.__width = value

	def get_height(self): return self.__height
	def set_height(self,value): self.__height = value

	def update(self):
		pass

	def draw(self,screen:pygame.Surface):
		pass