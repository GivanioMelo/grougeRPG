import pygame
import engine.sprites as sprites

class Button:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.texture = sprites.defaultButton
		self.pressedTexture = sprites.defaultButton_pressed
		self.pressed = False
		self.wasPressed = False
		self.justPressed = False
		self.justReleased = False
		self.visible = True

	def update(self):
		self.wasPressed = self.pressed

		mouseButtons = pygame.mouse.get_pressed()
		if mouseButtons[0] == True:
			mx,my = pygame.mouse.get_pos()
			if mx >= self.x and mx <= self.x + 12 and my >= self.y and my <= self.y +12:
				self.pressed = True
		else:
			if self.pressed == True: self.pressed = False
				
		self.justPressed = (self.pressed and not self.wasPressed)
		self.justReleased = (self.wasPressed and not self.pressed)

	def draw(self, screen):
		if self.pressed: screen.blit(self.pressedTexture,(self.x,self.y))
		else: screen.blit(self.texture,(self.x,self.y))

class ToggleButton(Button):
	def __init__(self, x, y, toggled=False):
		super().__init__(x, y)
		self.toggled = toggled
	
	def update(self):
		super().update()
		if self.justPressed: self.toggled = not self.toggled

	def draw(self,screen):
		if self.toggled: screen.blit(self.pressedTexture,(self.x,self.y))
		else: screen.blit(self.texture,(self.x,self.y))


