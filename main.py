import sys
import pygame
from screens.character_creation import character_creation
from screens.settings_menu import settings_menu
from screens.load_game_menu import load_game_menu

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quests")

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 215, 0)
GRAY = (100, 100, 100)
BLACK = (0, 0, 0)

# Font
font_large = pygame.font.SysFont("serif", 48)
font_medium = pygame.font.SysFont("serif", 36)

# Button settings
button_width = 300
button_height = 60
button_spacing = 20

# Menu options
menu_options = ["Novo Jogo", "Carregar Jogo", "Configurações", "Sair"]
selected_index = 0

# Helper functions
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

def draw_menu():
    SCREEN.fill(BLACK)
    draw_text("Quests", font_large, YELLOW, SCREEN, WIDTH // 2, 100)
    
    for i, option in enumerate(menu_options):
        color = YELLOW if i == selected_index else WHITE
        x = WIDTH // 2 - button_width // 2
        y = 200 + i * (button_height + button_spacing)
        
        pygame.draw.rect(SCREEN, GRAY, (x, y, button_width, button_height))
        draw_text(option, font_medium, color, SCREEN, WIDTH // 2, y + button_height // 2)

    pygame.display.flip()

def main_menu():
    global selected_index
    running = True

    while running:
        draw_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_index = (selected_index - 1) % len(menu_options)
                if event.key == pygame.K_DOWN:
                    selected_index = (selected_index + 1) % len(menu_options)
                if event.key == pygame.K_RETURN:
                    if selected_index == 0:
                        character_creation()
                    elif selected_index == 1:
                        load_game_menu()
                    elif selected_index == 2:
                        settings_menu()
                    elif selected_index == 3:
                        pygame.quit()
                        sys.exit()

if __name__ == "__main__":
    main_menu()
