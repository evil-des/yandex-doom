import math
import pygame
from map import *
from settings import *

def raycast(screen, pl_pos, pl_ang):
    curr_ang = pl_ang - FOV / 2
    plx, ply = pl_pos
    for ray in range(RAYS_C):
        cos_a = math.cos(curr_ang)
        sin_a = math.sin(curr_ang)
        for depth in range(DEPTH):
            x = plx + depth * cos_a
            y = ply + depth * sin_a
            if depth > 0:
                if (x // TILE_SIZE * TILE_SIZE, y // TILE_SIZE * TILE_SIZE) in walls:
                    depth *= math.cos(pl_ang - curr_ang)
                    proj_height = PROJ_COEFF / depth
                    c = 255 * ((DEPTH - depth) / DEPTH)
                    color = (c, c, c)
                    pygame.draw.rect(screen, color, (ray * SCALE, HEIGHT / 2 - proj_height // 2, SCALE + 1, proj_height))
                    break
        # pygame.draw.line(screen, WHITE, pl_pos, (x, y), 1)
        curr_ang += DELTA_ANG