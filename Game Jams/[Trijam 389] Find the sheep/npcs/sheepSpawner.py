from random import randrange

from npcs.sheep import Sheep
from core.config import STARTING_SHEEP_COUNT, DIFFICULTY_SCALING
from core.path_utils import get_base_dir
import os


class SheepSpawner:
    def __init__(self, width: int, height: int, menu_exclusion_zone: tuple):
        self.width = width
        self.height = height
        self.menu_exclusion_zone = menu_exclusion_zone

    def spawn(self, level: int) -> list:
        sheep_count = (level - 1) * DIFFICULTY_SCALING + STARTING_SHEEP_COUNT
        flock = []
        base_dir = get_base_dir()
        for _ in range(sheep_count):
            pos = self.get_random_sheep_pos()
            flock.append(
                Sheep(
                    pos,
                    image_path=os.path.join(base_dir, "Art", "Sheep1.png"),
                    dead_image_path=os.path.join(base_dir, "Art", "SheepDead1.png"),
                    sick_image_path=os.path.join(base_dir, "Art", "SickSheep1.png"),
                    blaa_sounds=[
                        os.path.join(base_dir, "Hidden", "blaa1.ogg"),
                        os.path.join(base_dir, "Hidden", "blaa2.ogg"),
                        os.path.join(base_dir, "Hidden", "blaa3.ogg"),
                    ],
                )
            )
        return flock

    def get_random_sheep_pos(self) -> tuple:
        x_min, x_max = self.menu_exclusion_zone[0]
        y_min, y_max = self.menu_exclusion_zone[1]
        edge_margin = 40

        while True:
            spawn_min_x = edge_margin
            spawn_max_x = self.width - edge_margin
            spawn_min_y = edge_margin
            spawn_max_y = self.height - edge_margin

            if spawn_max_x <= spawn_min_x:
                x = self.width // 2
            else:
                x = randrange(spawn_min_x, spawn_max_x)

            if spawn_max_y <= spawn_min_y:
                y = self.height // 2
            else:
                y = randrange(spawn_min_y, spawn_max_y)

            pos = (x, y)
            if x_min < pos[0] < x_max and y_min < pos[1] < y_max:
                continue
            return pos
