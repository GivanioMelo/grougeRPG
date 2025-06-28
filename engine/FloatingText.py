import pygame
import random

class FloatingText:
    def __init__(self, text, position, type='damage', duration=500):
        self.text = text
        self.position = pygame.Vector2(position)
        self.type = type
        self.duration = duration  # milissegundos
        self.timer = 0

        # Aparência baseada no tipo
        self.color, self.font = self.get_style(type)
        self.image = self.font.render(text, True, self.color)
        self.alpha = 255
        self.velocity = self.get_initial_velocity(type)
        self.gravity = 0.3 if type == 'damage' else 0  # só aplica gravidade para dano

    def get_style(self, type):
        font = pygame.font.Font(None, 24)
        if type == 'damage': return (pygame.Color('red'), font)
        elif type == 'heal': return (pygame.Color('green'), font)
        elif type == 'xp': return (pygame.Color('gold'), font)
        elif type == 'levelup': return (pygame.Color('goldenrod'), font)
        elif type == 'skill': return (pygame.Color('white'), font)
        elif type == 'status': return (pygame.Color('darkgreen'), font)
        elif type == 'death': return (pygame.Color('gray'), font)
        else: return (pygame.Color('white'), font)

    def get_initial_velocity(self, type):
        if type == 'damage':
            return pygame.Vector2(random.choice([-1.5, 1.5]), -2.5)
        elif type == 'heal':
            return pygame.Vector2(0, -1.0)
        else:
            return pygame.Vector2(0, -1.2)

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.duration:
            self.alpha = 0
        else:
            self.velocity.y += self.gravity
            self.position += self.velocity
            self.alpha = max(0, 255 - int(255 * (self.timer / self.duration)))

    def draw(self, surface):
        if self.alpha <= 0:
            return
        img = self.image.copy()
        img.set_alpha(self.alpha)
        rect = img.get_rect(center=self.position)
        surface.blit(img, rect)

    def is_alive(self):
        return self.alpha > 0
