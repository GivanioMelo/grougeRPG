from math import floor
import os
import tkinter
import numpy as np
import pygame

from engine.Camera import Camera

import engine.Config as config

map = np.zeros((100,100))
camera = Camera(0,0,20,15)

tiles = []
for file in os.listdir("sprites/tiles"):
	img = pygame.image.load(f"sprites/tiles/{file}")
	img = pygame.transform.scale(img, (64,64))
	tiles.append(img)

brush = 0

def update(brush):
	running = True
	events = pygame.event.get() 
	for event in events:
		if event.type == pygame.KEYDOWN:
			if pygame.key.get_pressed()[pygame.K_LEFT]: camera.x -= 1
			elif pygame.key.get_pressed()[pygame.K_RIGHT]: camera.x += 1
			elif pygame.key.get_pressed()[pygame.K_UP]: camera.y -= 1
			elif pygame.key.get_pressed()[pygame.K_DOWN]: camera.y += 1

			elif pygame.key.get_pressed()[pygame.K_KP_PLUS]:
				brush += 1
				if brush >= len(tiles): brush = 0
				print(f"brush is now: {brush}")
			elif pygame.key.get_pressed()[pygame.K_KP_MINUS]:
				brush -= 1
				if brush < 0: brush = len(tiles) -1
				print(f"brush is now: {brush}")
		if event.type == pygame.MOUSEWHEEL:
			pass
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mx, my = pygame.mouse.get_pos()
			ix = floor((mx / config.TILE_SIZE) + camera.x - camera.x_offset())
			iy = floor((my / config.TILE_SIZE) + camera.y - camera.y_offset())
			try:
				print(f"{(ix,iy)} = {brush}")
				map[ix,iy] = brush
			except:
				print((ix,iy))
		if event.type == pygame.QUIT:
			running = False

	return running, brush

screen = pygame.display.set_mode(camera.getRenderSize())
w, h = camera.getSize()
x_offset = camera.x_offset()
y_offset = camera.y_offset()
def draw():
	screen.fill(pygame.Color(0,0,0))
	cx = camera.x
	cy = camera.y

	for x in range(w):
		for y in range(h):

			ix = int(cx + x - x_offset)
			iy = int(cy + y - y_offset)

			rx = x * config.TILE_SIZE
			ry = y * config.TILE_SIZE

			if ix >= 0 and iy >= 0 and ix < map.shape[0] and iy < map.shape[1]:
				v= int (map[ix,iy])
				rect = pygame.Rect(rx,ry,config.TILE_SIZE,config.TILE_SIZE)
				if(v < len(tiles)):
					screen.blit(tiles[v],rect)
	pygame.display.update()

running = True
while running:
	running , brush= update(brush)
	draw()