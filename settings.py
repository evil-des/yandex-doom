import math
import ctypes

# костыль чтобы получить разрешение экрана
user = ctypes.windll.user32

# game settings
WIDTH, HEIGHT = user.GetSystemMetrics(0), user.GetSystemMetrics(1) 
FPS = 30
TILE_SIZE = 100
SENSETIVITY = 2

# raycasting settings
FOV = math.pi / 3
RAYS_C = 100
DEPTH = 1500
DELTA_ANG = FOV / RAYS_C
SCALE = WIDTH / RAYS_C
DIST = RAYS_C / (2 * math.tan(FOV / 2))
PROJ_COEFF = (HEIGHT / 50) * DIST * TILE_SIZE


# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)