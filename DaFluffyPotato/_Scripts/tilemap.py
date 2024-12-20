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
            self.tilemap[f'{3 + i}; 10'] = {'type': 'grass', 'varient': 1, 'pos': (3 + i, 10)}
            self.tilemap[f'10; {5 + i}'] = {'type': 'stone', 'varient': 1, 'pos': (10, 5 + i)}
            
    def render(self, surface):
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            surface.blit(self.game.assets[tile['type']][tile['varient']],
                         (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))

        for tile in self.offgrid_tiles:
            surface.blit(self.game.assets[tile['type']][tile['varient']], tile['pos'])