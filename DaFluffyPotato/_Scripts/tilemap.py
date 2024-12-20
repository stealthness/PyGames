import pygame

NEIGHBORHOOD_OFFSETS = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]
PHYSICS_TILES = {'grass', 'stone'}


class Tilemap:
    """
    A class to represent a tilemap.
    tile_size: int - The size of each tile in pixels.
    tilemap: dict - A dictionary containing the tiles.
    """

    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        for i in range(0, 10):
            self.tilemap[f'{3 + i};10'] = {'type': 'grass', 'varient': 1, 'pos': (3 + i, 10)}
            self.tilemap[f'10;{5 + i}'] = {'type': 'stone', 'varient': 1, 'pos': (10, 5 + i)}

    def __str__(self):
        return f'Tilemap: {self.tilemap}'

    def render(self, surface):
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            surface.blit(self.game.assets[tile['type']][tile['varient']],
                         (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))

    def tiles_around(self, pos):
        tiles = []
        tile_locs = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        
        for offset in NEIGHBORHOOD_OFFSETS:
            check_loc = f'{tile_locs[0] + offset[0]};{tile_locs[1] + offset[1]}'
            if check_loc in self.tilemap:
                tiles.append(self.tilemap[check_loc])

        return tiles

    def physics_rects_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            if tile['type'] in PHYSICS_TILES:
                rects.append(pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size,
                                         self.tile_size, self.tile_size))

        return rects
