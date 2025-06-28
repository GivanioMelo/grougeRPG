import sys
import pygame

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reino de Eldoria - Criação de Personagem")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 215, 0)
GRAY = (128, 128, 128)

# Fonts
font_large = pygame.font.SysFont("serif", 36)
font_medium = pygame.font.SysFont("serif", 28)
font_small = pygame.font.SysFont("serif", 24)

# Load icons
icon_human = pygame.image.load("assets/icons/human.png")
icon_elf = pygame.image.load("assets/icons/elf.png")
icon_dwarf = pygame.image.load("assets/icons/dwarf.png")
icon_warrior = pygame.image.load("assets/icons/warrior.png")
icon_mage = pygame.image.load("assets/icons/mage.png")
icon_archer = pygame.image.load("assets/icons/archer.png")
icon_male = pygame.image.load("assets/icons/male.png")
icon_female = pygame.image.load("assets/icons/female.png")

# Resize images to fit inside selection boxes
def resize_image(image, size=(40, 40)):
    return pygame.transform.scale(image, size)

# Resizing all icons
icon_human = resize_image(icon_human)
icon_elf = resize_image(icon_elf)
icon_dwarf = resize_image(icon_dwarf)
icon_warrior = resize_image(icon_warrior)
icon_mage = resize_image(icon_mage)
icon_archer = resize_image(icon_archer)
icon_male = resize_image(icon_male)
icon_female = resize_image(icon_female)

# Mapping options to icons
race_icons = [icon_human, icon_elf, icon_dwarf]
class_icons = [icon_warrior, icon_mage, icon_archer]
gender_icons = [icon_male, icon_female]

# Helper functions
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def draw_steps(surface, steps, current_step):
    spacing = WIDTH // len(steps)
    for i, step in enumerate(steps):
        color = YELLOW if step == current_step else GRAY
        draw_text(step, font_small, color, surface, spacing * i + spacing // 2, 30)

def draw_option_box(text, icon, x, y, width, height, selected=False):
    border_color = YELLOW if selected else GRAY
    background_color = (50, 50, 50)
    pygame.draw.rect(SCREEN, background_color, (x, y, width, height))
    pygame.draw.rect(SCREEN, border_color, (x, y, width, height), 3)
    SCREEN.blit(icon, (x + 10, y + 5))  # Draw the icon to the left
    draw_text(text, font_medium, WHITE, SCREEN, x + 123 + width // 2 - width // 2, y + height // 2)

def character_creation():
    player_name = ""
    races = ["Humano", "Elfo", "Anão"]
    classes = ["Guerreiro", "Mago", "Arqueiro"]
    genders = ["Masculino", "Feminino"]

    creation_steps = ["Nome", "Raça", "Classe", "Sexo", "Confirmação"]
    current_step = "Nome"
    selected_index = 0

    running = True
    while running:
        SCREEN.fill(BLACK)

        # Draw creation steps
        draw_steps(SCREEN, creation_steps, current_step)

        if current_step == "Nome":
            draw_text("Digite o nome do seu personagem:", font_large, WHITE, SCREEN, WIDTH // 2, 100)
            draw_text(player_name + "|", font_large, YELLOW, SCREEN, WIDTH // 2, 200)

        elif current_step == "Raça":
            draw_text("Escolha a raça:", font_large, WHITE, SCREEN, WIDTH // 2, 100)
            for i, race in enumerate(races):
                draw_option_box(race, race_icons[i], 250, 200 + i * 70, 300, 50, selected_index == i)

        elif current_step == "Classe":
            draw_text("Escolha a classe:", font_large, WHITE, SCREEN, WIDTH // 2, 100)
            for i, class_name in enumerate(classes):
                draw_option_box(class_name, class_icons[i], 250, 200 + i * 70, 300, 50, selected_index == i)

        elif current_step == "Sexo":
            draw_text("Escolha o sexo:", font_large, WHITE, SCREEN, WIDTH // 2, 100)
            for i, gender in enumerate(genders):
                draw_option_box(gender, gender_icons[i], 250, 200 + i * 70, 300, 50, selected_index == i)

        elif current_step == "Confirmação":
            draw_text("Personagem criado!", font_large, YELLOW, SCREEN, WIDTH // 2, 100)
            draw_text(f"Nome: {player_name}", font_medium, WHITE, SCREEN, WIDTH // 2, 200)
            draw_text(f"Raça: {races[selected_race]}", font_medium, WHITE, SCREEN, WIDTH // 2, 250)
            draw_text(f"Classe: {classes[selected_class]}", font_medium, WHITE, SCREEN, WIDTH // 2, 300)
            draw_text(f"Sexo: {genders[selected_gender]}", font_medium, WHITE, SCREEN, WIDTH // 2, 350)
            draw_text("Pressione Enter para continuar...", font_medium, YELLOW, SCREEN, WIDTH // 2, 450)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if current_step == "Nome":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if player_name.strip() != "":
                            current_step = "Raça"
                            selected_index = 0
                    elif event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]
                    else:
                        if len(player_name) < 20:
                            player_name += event.unicode

            elif current_step in ["Raça", "Classe", "Sexo"]:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected_index = (selected_index - 1) % (3 if current_step != "Sexo" else 2)
                    if event.key == pygame.K_DOWN:
                        selected_index = (selected_index + 1) % (3 if current_step != "Sexo" else 2)
                    if event.key == pygame.K_RETURN:
                        if current_step == "Raça":
                            selected_race = selected_index
                            current_step = "Classe"
                            selected_index = 0
                        elif current_step == "Classe":
                            selected_class = selected_index
                            current_step = "Sexo"
                            selected_index = 0
                        elif current_step == "Sexo":
                            selected_gender = selected_index
                            current_step = "Confirmação"

            elif current_step == "Confirmação":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    running = False
                    print("\nPersonagem Criado:")
                    print(f"Nome: {player_name}")
                    print(f"Raça: {races[selected_race]}")
                    print(f"Classe: {classes[selected_class]}")
                    print(f"Sexo: {genders[selected_gender]}")
                    # Here you could continue to start the actual game

# Example call
if __name__ == "__main__":
    character_creation()
