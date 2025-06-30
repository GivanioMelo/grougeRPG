import pygame
import engine.sprites as sprites

from engine.ui.Buttons import Button
from engine.ui.Container import Container
from engine.ui.ScrollBar import ScrollBar, HORIZONTAL,VERTICAL

_windowSpriteSheet_ = sprites.load("assets/ui/windowTexture.png",3,3)
_titleFont = pygame.font.SysFont("Consolas", 12,bold=True)

class _WindowCloseButton(Button):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.texture = sprites.window_CloseButton
		self.pressedTexture = sprites.window_CloseButton_pressed

class Window(Container):
	visible:bool
	title:str

	x:float
	y:float
	width:float
	height:float

	closeButton: _WindowCloseButton

	hasVerticalScrollBar:bool
	verticalScrollBar:ScrollBar

	hasHorizontalScrollBar:bool
	horizontalScrollBar:ScrollBar

	_renderingBuffer_:pygame.Surface

	_isPressed_:bool
	_wasPressed_:bool

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.title = kwargs.get('title', "")
		self.visible = kwargs.get('visible', True)
		# self.x = kwargs.get('x', 0)
		# self.y = kwargs.get('y', 0)
		# self.width = kwargs.get('width', 100)
		# self.height = kwargs.get('height', 100)

		self._isPressed_ = False
		self._wasPressed_= False

		self.hasVerticalScrollBar = kwargs.get('vScrollBar', False)
		self.hasHorizontalScrollBar = kwargs.get('hScrollBar', False)
		self.hasCloseButton = kwargs.get('hasCloseButton', True)

		self.verticalScrollBar = None
		self.horizontalScrollBar = None
		self.closeButton = None

		self.placeComponents()
		self.preRender()

	def placeComponents(self):
		self.getChildren().clear()
		if(self.hasVerticalScrollBar):
			self.verticalScrollBar = ScrollBar(self.width-16,16,self.height-20,VERTICAL)
			self.addChild(self.verticalScrollBar)
		if(self.hasHorizontalScrollBar):
			self.horizontalScrollBar = ScrollBar(4,self.height-16,self.width-8,HORIZONTAL)
			self.addChild(self.horizontalScrollBar)
			if(self.verticalScrollBar):
				self.verticalScrollBar.set_height(self.height-32)
		if self.hasCloseButton:
			self.closeButton = _WindowCloseButton(self.width-16, 2)
			self.addChild(self.closeButton)

	def update(self):
		if not self.visible: return
		super().update()
		if(self.closeButton):
			if(self.closeButton.justReleased): self.visible = False
		
		self._wasPressed_ = self._isPressed_
		mouseButtons= pygame.mouse.get_pressed()
		
		if(mouseButtons[0]):
			mx,my = pygame.mouse.get_pos()
			if (mx > self.x and mx < self.x + self.width -16 and my > self.y and my < self.y + 16):
				self._isPressed_ = True
		else:
			if self._isPressed_ == True: self._isPressed_ = False
		if(self._isPressed_):
			mdx,mdy = pygame.mouse.get_rel()
			if(self._wasPressed_):
				self.x += mdx
				self.y += mdy
				self.placeComponents()

	def draw(self,surface:pygame.Surface):
		if not self.visible: return
		if(self._renderingBuffer_ == None):
			print('no buffer rendered')
			return
		surface.blit(self._renderingBuffer_,(self.x,self.y))
		super().draw(surface)
		# self.closeButton.draw(surface)
		# if(self.verticalScrollBar):self.verticalScrollBar.draw(surface)
		# if(self.horizontalScrollBar):self.horizontalScrollBar.draw(surface)


	def preRender(self):
		self._renderingBuffer_ = None
		if(_windowSpriteSheet_ == None): print("no spritesheet"); return
		if(len(_windowSpriteSheet_) < 3): print("no spritesheet");  return
		if(len(_windowSpriteSheet_[0]) < 3): print("no spritesheet");  return

		self._renderingBuffer_ = pygame.Surface((self.width, self.height))

		spriteWidth = 16
		spriteHeight = 16

		if float(self.width / spriteWidth) < 1.5: print(float(self.width / spriteWidth)); return
		if float(self.height / spriteHeight) < 1.5: print(float(self.height / spriteHeight)); return

		tiledWidth = int(self.width / spriteWidth)
		tiledHeight = int(self.height / spriteHeight)

		if(tiledWidth < 1): print(tiledWidth);return
		if(tiledHeight < 1): print(tiledHeight);return

		for i in range(1,tiledWidth):
			for j in range(1,tiledHeight):
				self._renderingBuffer_.blit(_windowSpriteSheet_[1][1], (i*spriteWidth,j*spriteHeight))

		for i in range(1,tiledWidth):
			self._renderingBuffer_.blit(_windowSpriteSheet_[0][1], (i*spriteWidth,0))
			self._renderingBuffer_.blit(_windowSpriteSheet_[2][1], (i*spriteWidth,self.height-spriteHeight))
		for j in range(1,tiledHeight):
			self._renderingBuffer_.blit(_windowSpriteSheet_[1][0], (0,j*spriteHeight))
			self._renderingBuffer_.blit(_windowSpriteSheet_[1][2], (self.width - spriteWidth,j*spriteHeight))

		self._renderingBuffer_.blit(_windowSpriteSheet_[0][0], (0,0))
		self._renderingBuffer_.blit(_windowSpriteSheet_[0][2], (self.width-spriteWidth,0))
		self._renderingBuffer_.blit(_windowSpriteSheet_[2][0], (0,self.height-spriteHeight))
		self._renderingBuffer_.blit(_windowSpriteSheet_[2][2], (self.width-spriteWidth,self.height-spriteHeight))

		self._renderingBuffer_.blit(_titleFont.render(self.title,True,(255,255,255)),(4,4))

_contentFont = pygame.font.SysFont("Consolas", 12)
class TextWindow(Window):
	def __init__(self, x = 0, y = 0, hasCloseButton=True, text:str = "", textColor = (255,255,255), title:str=""):
		textPosition = (8, 20)
		lines = text.split("\n")
		textSurfaces = []
		width = 32
		height = 32
		for line in lines:
			textSurface = _contentFont.render(line, True, textColor)
			textSurfaces.append(textSurface)
			if (textSurface.get_width()+32) > width: width = textSurface.get_width()+32
			height += textSurface.get_height()
	
		super().__init__(x, y, width, height, False, False, hasCloseButton, title=title)

		for textSurface in textSurfaces:
			self._renderingBuffer_.blit(textSurface, textPosition)
			textPosition = (textPosition[0], textPosition[1] + textSurface.get_height())

class InventoryWindow(Window):
	def __init__(self, x = 0, y = 0, rows = 1, cols = 4,title:str = ""):
		width = 8 + (cols*34) + 8
		height = 20 + (rows*34) + 8
		
		vScrollBar=False
		hScrollBar=False
		hasCloseButton=True
		super().__init__(x, y, width, height, vScrollBar, hScrollBar, hasCloseButton,title=title)

		for i in range(rows):
			for j in range(cols):
				slotX = 8 + (j*34)
				slotY = 20 + (i*34)
				self._renderingBuffer_.blit(sprites.window_InventorySlot, (slotX,slotY))