# import pygame
import time
import numpy as np
import pygame
from pygame.locals import *

import engine.Config as config

from engine.GameObject import Rock
from engine.character.player import Player

import cv2

pygame.init()

map = np.random.normal(0.5, 0.1, size=(100,100))
map = map / map.max()
map = cv2.blur(map, (5,5))

objects = []
objects.append(Rock(2,2))

for x in range(100):
	for y in range(100):
		if(map[x,y] > 0.65):
			objects.append(Rock(x,y))

paverTile = pygame.transform.scale(pygame.image.load("assets/tile_stone.png"),(config.TILE_SIZE,config.TILE_SIZE))

player = Player(0,0)
w, h = player.camera.getSize()

renderSize = player.camera.getRenderSize()
screen = pygame.display.set_mode(renderSize, RESIZABLE)
screenBuffer = pygame.Surface(renderSize)

x_offset = player.camera.x_offset()
y_offset = player.camera.y_offset()

running = True

def update():
	running = True
	events = pygame.event.get() 
	for event in events:
		if event.type == pygame.KEYDOWN:
			if pygame.key.get_pressed()[pygame.K_LEFT]: player.x -= 1
			elif pygame.key.get_pressed()[pygame.K_RIGHT]: player.x += 1
			elif pygame.key.get_pressed()[pygame.K_UP]: player.y -= 1
			elif pygame.key.get_pressed()[pygame.K_DOWN]: player.y += 1

			if pygame.key.get_pressed()[pygame.K_p]:
				print(player.getPosition())
				print(player.getRenderPosition())
				print(player.getRect())
				print(len(objects))
				for object in objects: print(f"position:{object.getPosition()} renderPoisition: {object.getRenderPosition(player.camera)} ({object.isVisible(player.camera)})")
		if event.type == VIDEORESIZE:
			global renderSize
			renderSize = event.dict["size"]
			print("renderSizeChanged")
		if event.type == pygame.QUIT:
			running = False
	player.update()

	for object in objects:
		object.update()

	return running

def draw():
	screenBuffer.fill(pygame.Color(0,0,0))
	cx = player.camera.x
	cy = player.camera.y

	for x in range(w):
		for y in range(h):

			ix = int(cx + x - x_offset)
			iy = int(cy + y - y_offset)

			rx = x * config.TILE_SIZE
			ry = y * config.TILE_SIZE

			if ix >= 0 and iy >= 0 and ix < map.shape[0] and iy < map.shape[1]:
				v= int(map[ix,iy] * 255)
				rect = pygame.Rect(rx,ry,config.TILE_SIZE,config.TILE_SIZE)
				paverTile.set_alpha(v)
				screenBuffer.blit(paverTile,rect)

	for object in objects:
		object.draw(screenBuffer, player.camera)

	player.draw(screenBuffer)
	screen.blit(pygame.transform.scale(screenBuffer, renderSize),(0,0))
	print(renderSize)
	pygame.display.update()
	pygame.display.flip()


while running:
	running = update()
	draw()
	time.sleep(0.03)