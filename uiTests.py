import pygame
pygame.init()

from engine.ui.pannel import Pannel
from engine.ui.window import InventoryWindow, Window,TextWindow
from engine.ui.button import Button
from engine.ui.button import ToggleButton
from engine.ui.scrollBar import ScrollBar,HORIZONTAL,VERTICAL

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Quests")

WHITE = (255, 255, 255)
YELLOW = (255, 215, 0)
GRAY = (100, 100, 100)
BLACK = (0, 0, 0)

pannels = []
pannels.append(Pannel(10,10,150,50))
pannels.append(Pannel(10,70,70,50))
pannels.append(Pannel(90,70,70,50))
pannels.append(Pannel(10,130,150,70))

windows = []
windows.append(Window(450,450,50,50))
windows.append(Window(450,10,150,150,True,True))
windows.append(Window(450,180,90,70,False,True))
windows.append(Window(600,180,50,90,True,False))

windows.append(TextWindow(170,10,text="Hello\nWelcome to Quests\nThis is my very first game...", title="Message"))
windows.append(InventoryWindow(170,90,4,4, title="Chest"))
windows.append(InventoryWindow(170,260,1,4, title="Parcel"))
windows.append(InventoryWindow(170,330,2,4, title="Bag"))

buttons = []
buttons.append(Button(700,10))
buttons.append(Button(700,30))
buttons.append(Button(700,50))
buttons.append(Button(700,70))

buttons.append(ToggleButton(720,10))
buttons.append(ToggleButton(720,30))
buttons.append(ToggleButton(720,50))
buttons.append(ToggleButton(720,70))

hsb = ScrollBar(10,550,700,HORIZONTAL)
vsb = ScrollBar(750,10,500,VERTICAL)

mouseButtons = pygame.mouse.get_pressed()

def update():
	running = True
	events = pygame.event.get() 
	for event in events:
		# if event.type == pygame.MOUSEBUTTONDOWN:
		if event.type == pygame.QUIT: running = False

	for w in windows: w.update()
	for b in buttons: b.update()
	hsb.update()
	vsb.update()
	# global mouseButtons
	# if (not mouseButtons[0]):
	# 	mouseButtons = pygame.mouse.get_pressed()
	# 	if(mouseButtons[0]):
	# 		mousePosition = pygame.mouse.get_pos()
	# 		mouseMovement = pygame.mouse.get_rel()
	# 		print(f"mousePosition:({mousePosition})\t mouse moviment:({mouseMovement})")
	# else:
	# 	mouseButtons = pygame.mouse.get_pressed()

	return running

def draw():
	SCREEN.fill(BLACK)
	for w in windows: w.draw(SCREEN)
	for p in pannels: p.draw(SCREEN)
	for b in buttons: b.draw(SCREEN)
	hsb.draw(SCREEN)
	vsb.draw(SCREEN)
	pygame.display.update()

running = True
while running:
	running = update()
	draw()