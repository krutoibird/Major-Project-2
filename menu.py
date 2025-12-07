
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

def run_main_menu(screen, clock):
    menu_background = pygame.image.load("assets/menu/real_background.png").convert()
    menu_background = pygame.transform.scale(menu_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    button_start = pygame.image.load("assets/menu/real_start.png").convert_alpha()
    button_width, button_height = 240, 120
    button_start = pygame.transform.scale(button_start, (button_width, button_height))
    start_button_rect = button_start.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 140))

    hover_w = int(button_width * 1.15)
    hover_h = int(button_height * 1.15)

    menu_running = True
    while menu_running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(mouse_pos):
                    return "level_select"

        screen.blit(menu_background, (0, 0))

        if start_button_rect.collidepoint(mouse_pos):
            enlarged = pygame.transform.scale(button_start, (hover_w, hover_h))
            screen.blit(enlarged, enlarged.get_rect(center=start_button_rect.center))
        else:
            screen.blit(button_start, start_button_rect)

        pygame.display.flip()
        clock.tick(60)


def run_level_select(screen, clock):
    bg = pygame.image.load("assets/menu/real_level_background.png").convert()
    bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Load level buttons
    levels = []
    gap = 50
    btn_w, btn_h = 120, 120
    hover_w, hover_h = int(btn_w * 1.15), int(btn_h * 1.15)

    total_width = btn_w * 5 + gap * 4
    start_x = SCREEN_WIDTH // 2 - total_width // 2
    start_y = SCREEN_HEIGHT // 2 - 200

    for i in range(1, 6):
        img = pygame.image.load(f"assets/menu/{i}level_button.png").convert_alpha()
        img = pygame.transform.scale(img, (btn_w, btn_h))
        rect = img.get_rect(topleft=(start_x + (btn_w + gap) * (i - 1), start_y))
        levels.append((img, rect, i))

    # Back button
    back = pygame.image.load("assets/menu/real_back_game start_menu_button.png").convert_alpha()
    bw, bh = back.get_width(), back.get_height()
    back_rect = back.get_rect(topleft=(50, SCREEN_HEIGHT // 2 - bh // 2))
    hover_bw, hover_bh = int(bw * 1.15), int(bh * 1.15)

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(mouse_pos):
                    return "main_menu"
                for img, rect, level_id in levels:
                    if rect.collidepoint(mouse_pos):
                        return level_id  # returns 1,2,3,4,5

        screen.blit(bg, (0, 0))

        # Render level buttons
        for img, rect, _ in levels:
            if rect.collidepoint(mouse_pos):
                enlarged = pygame.transform.scale(img, (hover_w, hover_h))
                screen.blit(enlarged, enlarged.get_rect(center=rect.center))
            else:
                screen.blit(img, rect)

        # Render back button
        if back_rect.collidepoint(mouse_pos):
            enlarged = pygame.transform.scale(back, (hover_bw, hover_bh))
            screen.blit(enlarged, enlarged.get_rect(center=back_rect.center))
        else:
            screen.blit(back, back_rect)

        pygame.display.flip()
        clock.tick(60)
