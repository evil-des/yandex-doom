import math
import pygame
from map import *
from player import *
from settings import *
from raycasting import *

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT \
            or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            exit()

    player.move()
    screen.fill(BLACK)
    
    pygame.draw.rect(screen, (135, 206, 235), (0, 0, WIDTH, HEIGHT / 2))
    pygame.draw.rect(screen, (83, 98, 103), (0, HEIGHT / 2, WIDTH, HEIGHT / 2))

    raycast(screen, player.pos(), player.angle)

    # pygame.draw.circle(screen, GREEN, player.pos(), 12)

    # for x, y in walls:
    #     pygame.draw.rect(screen, WHITE, (x, y, TILE_SIZE, TILE_SIZE), 1)

    pygame.display.flip()
    clock.tick(FPS)