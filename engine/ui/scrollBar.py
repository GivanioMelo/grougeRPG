import pygame

import engine.sprites as sprites

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
        
class ScrollBar:
    def __init__(self,x,y,lenght,orientation, minValue=0, maxValue=100):
        self.x = x
        self.y = y
        
        self.lenght = lenght-12

        self.cursor = minValue
        self.minValue = minValue
        self.maxValue = maxValue

        self.orientation = orientation

        self.cursorButton = ScrollBarCursorButton(x,y)

        if orientation == VERTICAL:
            self.width = 12
            self.height = lenght
            self.startButton = v_ScrollBarStartButton(x, y)
            self.endButton = v_ScrollBarEndButton(x, y + lenght-12)
            self.backGroundTexture = _v_scroll_texture_
        else:
            self.height = 12
            self.width = lenght
            self.startButton = h_ScrollBarStartButton(x, y)
            self.endButton = h_ScrollBarEndButton(x + lenght-12,y)
            self.backGroundTexture = _h_scroll_texture_
    
    def update(self):
        self.startButton.update()
        self.endButton.update()
        self.cursorButton.update()

        if (self.startButton.justPressed): self.cursor -= 1
        if (self.endButton.justPressed): self.cursor += 1
        
        if self.cursorButton.pressed:
            mdx,mdy = pygame.mouse.get_rel()
            if self.cursorButton.wasPressed:
                if self.orientation == VERTICAL: self.cursor += (mdy / self.height) * (self.maxValue - self.minValue)
                if self.orientation == HORIZONTAL: self.cursor += (mdx / self.width) * (self.maxValue - self.minValue)

        if self.cursor < self.minValue: self.cursor = self.minValue
        if self.cursor > self.maxValue: self.cursor = self.maxValue
        
        

    
    def draw(self, screen:pygame.Surface):
        if self.lenght < 12: return

        screen.blit(pygame.transform.scale(self.backGroundTexture, (self.width,self.height)),(self.x,self.y))
        
        cursorOffset = (((self.cursor - self.minValue) / self.maxValue) * (self.lenght - 24)) + 12
        self.cursorButton.x = self.x
        self.cursorButton.y = self.y

        if self.orientation == VERTICAL: self.cursorButton.y += cursorOffset
        if self.orientation == HORIZONTAL: self.cursorButton.x += cursorOffset

        self.cursorButton.draw(screen)

        self.startButton.draw(screen)
        self.endButton.draw(screen)

