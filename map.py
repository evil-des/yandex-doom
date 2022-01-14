from settings import *

# W - wall, any other char - void
text_map = [
    'WWWWWWWWWWWWWWW',
    'W.............W',
    'W.............W',
    'W..WWWWW......W',
    'W..W...W......W',
    'W..W...W......W',
    'W..WW..W......W',
    'W.............W',
    'W.............W',
    'WWWWWWWWWWWWWWW',
]
# searching walls
walls = set()
for y, row in enumerate(text_map):
    for x, tile in enumerate(row):
        if tile == 'W':
            walls.add((x * TILE_SIZE, y * TILE_SIZE))