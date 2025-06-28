import sys
import pygame

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 215, 0)
GRAY = (100, 100, 100)
BLACK = (0, 0, 0)

# Font
font_large = pygame.font.SysFont("serif", 48)
font_medium = pygame.font.SysFont("serif", 36)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

def settings_menu():
    running = True

    while running:
        SCREEN.fill(BLACK)
        draw_text("Configurações", font_large, YELLOW, SCREEN, WIDTH // 2, 100)
        draw_text("Pressione ESC para voltar", font_medium, WHITE, SCREEN, WIDTH // 2, HEIGHT - 100)

        # Futuro: adicionar opções de volume, resolução, etc.

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
