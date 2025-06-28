import sys
import os
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

# Path where save files would be
SAVE_PATH = "saves"

def get_save_files():
    if not os.path.exists(SAVE_PATH):
        os.makedirs(SAVE_PATH)
    return [f for f in os.listdir(SAVE_PATH) if f.endswith(".sav")]

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

def load_game_menu():
    save_files = get_save_files()
    selected_index = 0
    running = True

    while running:
        SCREEN.fill(BLACK)
        draw_text("Carregar Jogo", font_large, YELLOW, SCREEN, WIDTH // 2, 50)

        if save_files:
            for i, filename in enumerate(save_files):
                color = YELLOW if i == selected_index else WHITE
                draw_text(filename, font_medium, color, SCREEN, WIDTH // 2, 150 + i * 50)
        else:
            draw_text("Nenhum jogo salvo encontrado.", font_medium, WHITE, SCREEN, WIDTH // 2, HEIGHT // 2)

        draw_text("Pressione ESC para voltar", font_medium, WHITE, SCREEN, WIDTH // 2, HEIGHT - 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if save_files:
                    if event.key == pygame.K_UP:
                        selected_index = (selected_index - 1) % len(save_files)
                    if event.key == pygame.K_DOWN:
                        selected_index = (selected_index + 1) % len(save_files)
                    if event.key == pygame.K_RETURN:
                        selected_save = save_files[selected_index]
                        print(f"Jogo {selected_save} carregado!")
                        # TODO: Implementar o carregamento do jogo de verdade
                        running = False
