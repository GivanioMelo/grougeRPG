import pygame

import engine.sprites as sprites

from engine.ui.Component import Component
from engine.ui.Buttons import Button

_v_scroll_texture_ = pygame.image.load("assets/ui/v_scroll.png")
_h_scroll_texture_ = pygame.image.load("assets/ui/h_scroll.png")

VERTICAL = 0
HORIZONTAL = 1

class v_ScrollBarStartButton(Button):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.texture = sprites.verticalScrollBar_StartButton
        self.pressedTexture = sprites.verticalScrollBar_StartButton_pressed

class v_ScrollBarEndButton(Button):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.texture = sprites.verticalScrollBar_EndButton
        self.pressedTexture = sprites.verticalScrollBar_EndButton_pressed

class h_ScrollBarStartButton(Button):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.texture = sprites.horizontalScrollBar_StartButton
        self.pressedTexture = sprites.horizontalScrollBar_StartButton_pressed

class h_ScrollBarEndButton(Button):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.texture = sprites.horizontalScrollBar_EndButton
        self.pressedTexture = sprites.horizontalScrollBar_EndButton_pressed

class ScrollBarCursorButton(Button):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.texture = sprites.scrollBarCursorButton
        self.pressedTexture = sprites.scrollBarCursorButton_pressed
        
class ScrollBar(Component):
    """
    Custom scroll bar.

    Initialization parameters:
        x (int, optional): X position of the scroll bar. Default: 0.
        y (int, optional): Y position of the scroll bar. Default: 0.
        lenght (int, optional): Length of the scroll bar (height if vertical, width if horizontal). Default: 100.
        minValue (int/float, optional): Minimum scroll value. Default: 0.
        maxValue (int/float, optional): Maximum scroll value. Default: 100.
        value (int/float, optional): Initial scroll value. Default: 0.
        orientation (int, optional): Bar orientation (VERTICAL=0, HORIZONTAL=1). Default: VERTICAL.
    """
    def __init__(self,x=0, y=0, lenght=100, minValue=0, maxValue=100, value=0, orientation=VERTICAL):
        super().__init__(x=x, y=y, width=12, height=12)
        self.lenght = lenght -12

        self.minValue = minValue
        self.maxValue = maxValue
        self.value = value

        if self.value < self.minValue: self.value = self.minValue
        if self.value > self.maxValue: self.value = self.maxValue

        self.orientation = orientation
        self.cursorButton = ScrollBarCursorButton(self.x,self.y)

        if self.orientation == VERTICAL:
            self.width = 12
            self.height = self.lenght+12
            self.startButton = v_ScrollBarStartButton(self.x, self.y)
            self.endButton = v_ScrollBarEndButton(self.x, self.y + self.lenght)
            self.backGroundTexture = _v_scroll_texture_
        else:
            self.height = 12
            self.width = self.lenght+12
            self.startButton = h_ScrollBarStartButton(self.x, self.y)
            self.endButton = h_ScrollBarEndButton(self.x + self.lenght, self.y)
            self.backGroundTexture = _h_scroll_texture_
    
    def setLenght(self, lenght):
        self.lenght = lenght - 12
        if self.orientation == VERTICAL:
            self.width = 12
            self.height = self.lenght+12
            self.startButton.x = self.x
            self.startButton.y = self.y
            self.endButton.x = self.x
            self.endButton.y = self.y + self.lenght
        else:
            self.height = 12
            self.width = self.lenght+12
            self.startButton.x = self.x
            self.startButton.y = self.y
            self.endButton.x = self.x + self.lenght
            self.endButton.y = self.y

    def set_height(self, value):
        if value < 12: value = 12
        self.height = value
        if self.orientation == VERTICAL:
            self.endButton.y = self.y + self.lenght
    
    def set_width(self, value):
        if value < 12: value = 12
        self.width = value
        if self.orientation == HORIZONTAL:
            self.endButton.x = self.x + self.lenght

    def update(self):
        self.startButton.update()
        self.endButton.update()
        self.cursorButton.update()

        if (self.startButton.justPressed): self.value -= 1
        if (self.endButton.justPressed): self.value += 1
        
        if self.cursorButton.pressed:
            mdx,mdy = pygame.mouse.get_rel()
            if self.cursorButton.wasPressed:
                if self.orientation == VERTICAL: self.value += (mdy / self.height) * (self.maxValue - self.minValue)
                if self.orientation == HORIZONTAL: self.value += (mdx / self.width) * (self.maxValue - self.minValue)

        if self.value < self.minValue: self.value = self.minValue
        if self.value > self.maxValue: self.value = self.maxValue
        
    def draw(self, surface:pygame.Surface):
        if self.lenght < 12: return

        surface.blit(pygame.transform.scale(self.backGroundTexture, (self.width,self.height)),(self.x,self.y))
        
        cursorOffset = (((self.value - self.minValue) / self.maxValue) * (self.lenght - 24)) + 12
        self.cursorButton.x = self.x
        self.cursorButton.y = self.y

        if self.orientation == VERTICAL: self.cursorButton.y += cursorOffset
        if self.orientation == HORIZONTAL: self.cursorButton.x += cursorOffset

        self.cursorButton.draw(surface)
        self.startButton.draw(surface)
        self.endButton.draw(surface)

