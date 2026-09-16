from random import randint

from npcs.wolf import Wolf
from core.config import STARTING_WOLF_COUNT


class WolfSpawner:
    def __init__(self, width: int, height: int, images):
        self.width = width
        self.height = height
        self.images = images

    def spawn(self, level: int) -> list:
        wolf_count = STARTING_WOLF_COUNT + ((level - 1) // 2)
        pack = []

        min_wolf_y = 80
        max_wolf_y = max(min_wolf_y, self.height - 80)

        for i in range(wolf_count):
            y = randint(min_wolf_y, max_wolf_y)
            if i % 2 == 0:
                pos = (-120 - (i * 80), y)
                direction = 1
            else:
                pos = (self.width + (i * 80), y)
                direction = -1

            wolf = Wolf(pos, self.images.get_wolf_frames(), self.images.get_dead_sheep_image())
            wolf.direction = direction
            wolf.activate(pos)
            pack.append(wolf)

        return pack
