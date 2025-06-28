import pygame
import os
import engine.Config as config

class Animation:
	def __init__(self, frames, frame_duration=200, loop=True):
		self.frames = frames
		self.frame_duration = frame_duration
		self.loop = loop

		self.current_frame_index = 0
		self.time_accumulator = 0
		self.finished = False

	def update(self, dt):
		if self.finished:
			return

		self.time_accumulator += dt
		if self.time_accumulator >= self.frame_duration:
			self.time_accumulator -= self.frame_duration
			self.current_frame_index += 1

			if self.current_frame_index >= len(self.frames):
				if self.loop:
					self.current_frame_index = 0
				else:
					self.current_frame_index = len(self.frames) - 1
					self.finished = True

	def reset(self):
		self.current_frame_index = 0
		self.time_accumulator = 0
		self.finished = False

	def get_current_frame(self):
		return self.frames[self.current_frame_index]

	def draw(self, surface, tile_x, tile_y, tile_size=32):
		tile_center = (
			tile_x * tile_size + tile_size // 2,
			tile_y * tile_size + tile_size // 2
		)
		frame = self.get_current_frame()
		frame_rect = frame.get_rect()
		frame_rect.midbottom = tile_center
		surface.blit(frame, frame_rect)
	
	@classmethod
	def fromFile(cls, filename:str):
		if filename.endswith(".png"):
			path = os.path.join(config.ANIMATIONS_FOLDER, filename)
			image = pygame.image.load(path).convert_alpha()

			width, height = image.get_size()

			# Determina a largura do frame com base na altura
			if height == 96: frame_width = 96
			elif height == 64: frame_width = 96
			else: frame_width = 32

			num_frames = width // frame_width
			frames = [
				image.subsurface(pygame.Rect(i * frame_width, 0, frame_width, height))
				for i in range(num_frames)
			]
			animation = Animation(frames, frame_duration=30)
			return animation