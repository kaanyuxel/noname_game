import pygame
import Player
import CameraGroup

pygame.init()

clock = pygame.time.Clock()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 1024

#game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Noname")
run_game = True


camera_group = CameraGroup.CameraGroup()
player = Player.Player(camera_group)

while run_game:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEWHEEL:
            camera_group.zoom_scale += event.y * 0.5

    screen.fill('#71ddee')

    player.update()
    camera_group.custom_draw(player)

    pygame.display.flip()
    clock.tick(30)
pygame.quit()
