import pygame
# 00 01 02
# 10 11 12
# 20 21 22
def load(imagePath, rows, cols):
	sheetImg = pygame.image.load(imagePath)
	sheet = [[0 for _ in range(cols)] for _ in range(rows)]
	for i in range(rows):
		for j in range(cols):
			x = j*(sheetImg.get_width()/cols)
			w = sheetImg.get_width()/cols
			y = i*(sheetImg.get_height()/rows)
			h = sheetImg.get_height()/rows
			sheetImg.set_clip(pygame.Rect(x,y,w,h))
			sheet[i][j] = sheetImg.subsurface(sheetImg.get_clip())
	return sheet

_buttonSpriteSheet_ = load("assets/ui/buttons_12x12.png",6,8)
# _pannelSpriteSheet_= load("assets/ui/PanelTemplate.png",3,3)
# _windowSpriteSheet_ = load("assets/ui/windowTexture.png",3,3)

defaultButton = _buttonSpriteSheet_[0][0]
defaultButton_pressed = _buttonSpriteSheet_[1][0]

window_CloseButton = _buttonSpriteSheet_[0][3]
window_CloseButton_pressed = _buttonSpriteSheet_[1][3]

window_InventorySlot = pygame.image.load("assets/ui/inventorySlot_34x34.png")

verticalScrollBar_StartButton = _buttonSpriteSheet_[4][5]
verticalScrollBar_StartButton_pressed = _buttonSpriteSheet_[5][5]
verticalScrollBar_EndButton = _buttonSpriteSheet_[4][6]
verticalScrollBar_EndButton_pressed = _buttonSpriteSheet_[5][6]

horizontalScrollBar_StartButton = _buttonSpriteSheet_[4][3]
horizontalScrollBar_StartButton_pressed = _buttonSpriteSheet_[5][3]
horizontalScrollBar_EndButton = _buttonSpriteSheet_[4][4]
horizontalScrollBar_EndButton_pressed = _buttonSpriteSheet_[5][4]

scrollBarCursorButton = _buttonSpriteSheet_[4][7]
scrollBarCursorButton_pressed = _buttonSpriteSheet_[5][7]