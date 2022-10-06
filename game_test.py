import pygame
import Player
import CameraGroup

pygame.init()

clock = pygame.time.Clock()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

#game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Noname")
run_game = True


camera_group = CameraGroup.CameraGroup()
player = Player.Player(camera_group)

while run_game:

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player.left_click = True

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_f] or keys[pygame.K_r]:
                player.set_attack(event.key)
        if keys[pygame.K_SPACE]:
            camera_group.center_target_camera(player)


        #if event.type == pygame.MOUSEWHEEL:
        #    camera_group.zoom_scale += event.y * 0.5

    screen.fill('#71ddee')

    player.update()
    camera_group.custom_draw(player)

    pygame.display.update()
    clock.tick(144)
pygame.quit()
