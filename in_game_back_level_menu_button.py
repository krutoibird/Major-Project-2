import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS  

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Menu")
clock = pygame.time.Clock()

# Load button image
button_image = pygame.image.load('C:/Users/kimoj/major_project/image/back_level_menu_button.png')
button_rect = button_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))  # Button in center

# Main menu background
menu_background = pygame.image.load("major_project/image/real_background.png").convert()
menu_background = pygame.transform.scale(menu_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

button_start = pygame.image.load("major_project/image/real_start.png").convert_alpha()
button_start = pygame.transform.scale(button_start, (240, 120))
start_button_rect = button_start.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 140))
hover_start_size = (int(240 * 1.15), int(120 * 1.15))

# Level menu background
level_menu_bg = pygame.image.load("major_project/image/real_level_background.png").convert()
level_menu_bg = pygame.transform.scale(level_menu_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

level_size = (120, 120)
hover_level_size = (int(120 * 1.15), int(120 * 1.15))
button_gap = 50
total_levels = 5

# Back button
back_button = pygame.image.load("major_project/image/real_back_game start_menu_button.png").convert_alpha()
back_button_rect = back_button.get_rect(topleft=(50, SCREEN_HEIGHT // 2 - back_button.get_height() // 2))
hover_back_size = (int(back_button.get_width() * 1.15), int(back_button.get_height() * 1.15))

# Load level buttons
level1_button = pygame.transform.scale(pygame.image.load("major_project/image/1level_button.png").convert_alpha(), level_size)
level2_button = pygame.transform.scale(pygame.image.load("major_project/image/2level_button.png").convert_alpha(), level_size)
level3_button = pygame.transform.scale(pygame.image.load("major_project/image/3level_button.png").convert_alpha(), level_size)
level4_button = pygame.transform.scale(pygame.image.load("major_project/image/4level_button.png").convert_alpha(), level_size)
level5_button = pygame.transform.scale(pygame.image.load("major_project/image/5level_button.png").convert_alpha(), level_size)

# Set level positions
start_x = SCREEN_WIDTH // 2 - (level_size[0] * total_levels + button_gap * (total_levels - 1)) // 2
start_y = SCREEN_HEIGHT // 2 - 200

level1_rect = level1_button.get_rect(topleft=(start_x, start_y))
level2_rect = level2_button.get_rect(topleft=(start_x + (level_size[0] + button_gap) * 1, start_y))
level3_rect = level3_button.get_rect(topleft=(start_x + (level_size[0] + button_gap) * 2, start_y))
level4_rect = level4_button.get_rect(topleft=(start_x + (level_size[0] + button_gap) * 3, start_y))
level5_rect = level5_button.get_rect(topleft=(start_x + (level_size[0] + button_gap) * 4, start_y))

# Show button and wait for click
def show_button_and_wait_for_click():
    running = True
    while running:
        screen.fill((255, 255, 255))  # Clear screen, set background to white

        # Hover effect: enlarge button if mouse is over it
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            enlarged_button = pygame.transform.scale(button_image, (int(button_rect.width * 1.15), int(button_rect.height * 1.15)))
            enlarged_rect = enlarged_button.get_rect(center=button_rect.center)
            screen.blit(enlarged_button, enlarged_rect)
        else:
            screen.blit(button_image, button_rect)  # Display normal button

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return  # Use pygame.quit() to exit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(pygame.mouse.get_pos()):  # Check if button is clicked
                    return "level_menu"  # Go to the level menu when clicked

        pygame.display.flip()
        clock.tick(60)

# Main menu
def main_menu():
    running = True
    while running:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return  # Use pygame.quit() to exit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(mouse):
                    return "level_menu"  # Go to level menu

        screen.blit(menu_background, (0, 0))
        if start_button_rect.collidepoint(mouse):
            enlarged = pygame.transform.scale(button_start, hover_start_size)
            rect = enlarged.get_rect(center=start_button_rect.center)
            screen.blit(enlarged, rect)
        else:
            screen.blit(button_start, start_button_rect)

        pygame.display.flip()
        clock.tick(FPS)

# Level menu
def level_menu():
    running = True
    while running:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return  # Use pygame.quit() to exit
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Back button
                if back_button_rect.collidepoint(mouse):
                    return "main_menu"  # Return to the main menu when the back button is clicked

                # Level button
                if level1_rect.collidepoint(mouse):
                    run_level(1, (20, 20, 20))
                if level2_rect.collidepoint(mouse):
                    run_level(2, (40, 40, 40))
                if level3_rect.collidepoint(mouse):
                    run_level(3, (60, 60, 60))
                if level4_rect.collidepoint(mouse):
                    run_level(4, (80, 80, 80))
                if level5_rect.collidepoint(mouse):
                    run_level(5, (100, 100, 100))

        screen.blit(level_menu_bg, (0, 0))

        # Draw level buttons with hover effect
        if level1_rect.collidepoint(mouse):
            enlarged = pygame.transform.scale(level1_button, hover_level_size)
            rect = enlarged.get_rect(center=level1_rect.center)
            screen.blit(enlarged, rect)
        else:
            screen.blit(level1_button, level1_rect)

        if level2_rect.collidepoint(mouse):
            enlarged = pygame.transform.scale(level2_button, hover_level_size)
            rect = enlarged.get_rect(center=level2_rect.center)
            screen.blit(enlarged, rect)
        else:
            screen.blit(level2_button, level2_rect)

        if level3_rect.collidepoint(mouse):
            enlarged = pygame.transform.scale(level3_button, hover_level_size)
            rect = enlarged.get_rect(center=level3_rect.center)
            screen.blit(enlarged, rect)
        else:
            screen.blit(level3_button, level3_rect)

        if level4_rect.collidepoint(mouse):
            enlarged = pygame.transform.scale(level4_button, hover_level_size)
            rect = enlarged.get_rect(center=level4_rect.center)
            screen.blit(enlarged, rect)
        else:
            screen.blit(level4_button, level4_rect)

        if level5_rect.collidepoint(mouse):
            enlarged = pygame.transform.scale(level5_button, hover_level_size)
            rect = enlarged.get_rect(center=level5_rect.center)
            screen.blit(enlarged, rect)
        else:
            screen.blit(level5_button, level5_rect)

        # Back button hover effect
        if back_button_rect.collidepoint(mouse):
            enlarged = pygame.transform.scale(back_button, hover_back_size)
            rect = enlarged.get_rect(center=back_button_rect.center)
            screen.blit(enlarged, rect)
        else:
            screen.blit(back_button, back_button_rect)

        pygame.display.flip()
        clock.tick(FPS)

# Run level
def run_level(level_number, color):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return  # Use pygame.quit() to exit
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
        screen.fill(color)
        pygame.display.flip()
        clock.tick(FPS)

# Main game loop
current_menu = "show_button_and_wait_for_click"  # Start with button menu

while True:
    if current_menu == "show_button_and_wait_for_click":
        result = show_button_and_wait_for_click()  # Go to level_menu after button click
        if result == "level_menu":
            current_menu = "level_menu"
    elif current_menu == "main_menu":
        result = main_menu()  # Go to level_menu quit
        if result == "level_menu":
            current_menu = "level_menu"
    elif current_menu == "level_menu":
        result = level_menu()  # Go to main_menu quit
        if result == "main_menu":
            current_menu = "main_menu"

pygame.quit()  # Exit Pygame cleanly
