import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela e tiles
TILE_SIZE = 32
GRID_WIDTH = 25   # 25 tiles * 32px = 800px
GRID_HEIGHT = 18  # 18 tiles * 32px = 576px

SCREEN_WIDTH = TILE_SIZE * GRID_WIDTH
SCREEN_HEIGHT = TILE_SIZE * GRID_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Teste de Grid de Tiles 32x32")

# Cores
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
DARK_GREEN = (34, 139, 34)

# Loop principal
def main():
    clock = pygame.time.Clock()

    while True:
        screen.fill(DARK_GREEN)

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Desenha o grid
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(screen, GRAY, rect, 1)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
