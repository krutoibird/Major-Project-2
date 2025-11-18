# Major-Project-2

import pygame

pygame.init()


pygame.mixer.music.load("music/CHAINSAW.mp3")
pygame.mixer.music.play(loops=-1)


screen1 = pygame.display.set_mode((720, 360))
ground2_surface = pygame.image.load("Image/ground2.png").convert()
player_surface = pygame.image.load("Image/character.png").convert()
player_surface = pygame.transform.scale(player_surface, (60, 70))
target_surface = pygame.image.load("Image/char.png").convert()
game_active = True


player_rect = player_surface.get_rect(center=(200, 180))
target_rect = target_surface.get_rect(center=(600, 180))



x_velocity = 0
y_velocity = 0
gravity = 0.3
floor = 310


while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y_velocity = y_velocity-3.5
            elif event.key == pygame.K_a:
                x_velocity = x_velocity-1
            elif event.key == pygame.K_s:
                y_velocity = y_velocity+1
            elif event.key == pygame.K_d:
                x_velocity = x_velocity+1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                y_velocity = y_velocity+3.5
            elif event.key == pygame.K_a:
                x_velocity = x_velocity+1
            elif event.key == pygame.K_s:
                y_velocity = y_velocity-1
            elif event.key == pygame.K_d:
                x_velocity = x_velocity-1
        if event.type == pygame.MOUSEMOTION:
            if event.rel[0] > 0:
                print("The mouse is moving to the right.")
            elif event.rel[0] < 0:
                print("The mouse is moving to the left.")
            elif event.rel[1] > 0:
                print("The mouse is moving down.")
            elif event.rel[1] < 0:
                print("The mouse is moving up.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                print("The right mouse button has been pressed.")
            elif event.button == 1:
                print("The left mouse button has been pressed.")

        y_velocity += gravity
        player_rect.move_ip(x_velocity, y_velocity)

    if player_rect.bottom >= floor:
        player_rect.bottom = floor
        y_velocity = 0

    player_rect.move_ip(x_velocity, y_velocity)
    screen1.blit(ground2_surface, (0, 0))
    screen1.blit(player_surface, (player_rect.centerx, player_rect.centery))
    screen1.blit(target_surface, target_rect)
    if player_rect.colliderect(target_rect):
        game_active = False

    pygame.display.update()
    pygame.time.Clock().tick(60)

