import pygame
import Player
import CameraGroup
import Map

pygame.init()

clock = pygame.time.Clock()

SCREEN_WIDTH = 1350
SCREEN_HEIGHT = 800

#game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Noname")
run_game = True


camera_group = CameraGroup.CameraGroup()
game_map = Map.Map(camera_group)
player = Player.Player(camera_group)


while run_game:
    screen.fill('gray')
    game_map.draw(screen)
    game_map.update()

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player.left_click = True

        if event.type == pygame.QUIT:
            pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_f] or keys[pygame.K_r]:
                player.set_attack(event.key)
        if keys[pygame.K_SPACE]:
            camera_group.center_target_camera(player)


        #if event.type == pygame.MOUSEWHEEL:
        #    camera_group.zoom_scale += event.y * 0.5

    camera_group.custom_draw(player)
    player.update()
    pygame.display.update()
    clock.tick(144)
pygame.quit()
