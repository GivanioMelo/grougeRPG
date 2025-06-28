import pygame
import sys
import os

import engine.Config as config

from engine.Animation import Animation
from engine.FloatingText import FloatingText


# Configurações da tela e tiles
TILE_SIZE = 32
GRID_WIDTH, GRID_HEIGHT = 25, 18
SCREEN_WIDTH = TILE_SIZE * GRID_WIDTH
SCREEN_HEIGHT = TILE_SIZE * GRID_HEIGHT

# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Visualizador de Animações")
clock = pygame.time.Clock()

# Cores
DARK_GREEN = (60, 20, 60)
GRID_COLOR = (60, 60, 60)


# Carregamento de animações da pasta
def load_animations():
    animations = []
    for filename in sorted(os.listdir(config.ANIMATIONS_FOLDER)):
        animation = Animation.fromFile(filename)
        if animation: animations.append(animation)
    return animations

# Desenhar o grid
def draw_grid():
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, GRID_COLOR, rect, 1)

def createTextSamples():
    floating_texts = []
    # Posição base para a linha 5 do grid (sexta linha)
    base_y = 11 * TILE_SIZE + TILE_SIZE // 2

    x = 1 ; floating_texts.append(FloatingText("-24", ((x) * TILE_SIZE + TILE_SIZE // 2, base_y), type='damage'))
    x = x+1; floating_texts.append(FloatingText("+12", ((x) * TILE_SIZE + TILE_SIZE // 2, base_y), type='heal'))
    x = x+1; floating_texts.append(FloatingText("+15 XP", ((x) * TILE_SIZE + TILE_SIZE // 2, base_y), type='xp'))
    x = x+4; floating_texts.append(FloatingText("Bola de Fogo", ((x) * TILE_SIZE + TILE_SIZE // 2, base_y), type='skill'))
    x = x+5; floating_texts.append(FloatingText("Subiu de Nível!", ((x) * TILE_SIZE + TILE_SIZE // 2, base_y), type='levelup'))
    x = x+5; floating_texts.append(FloatingText("Envenenado", ((x) * TILE_SIZE + TILE_SIZE // 2, base_y), type='status'))

    return floating_texts

# Programa principal
def main():
    animations = load_animations()
    floating_texts = createTextSamples()

    usable_width = GRID_WIDTH - 2
    running = True

    while running:
        dt = clock.tick(30)
        screen.fill(DARK_GREEN)
        draw_grid()

        tile_x = 1
        tile_y = 1
        for index, animation in enumerate(animations):
            animation.update(dt)
            animation.draw(screen, tile_x, tile_y)
            tile_x = tile_x + 2
            if tile_x >= usable_width:
                tile_x = 1
                tile_y = tile_y + 2

        dt = clock.tick(60)
        for text in floating_texts: text.update(dt)
        for text in floating_texts: text.draw(screen)
        floating_texts = [t for t in floating_texts if t.is_alive()]
        if len(floating_texts) == 0: floating_texts=createTextSamples()


        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
