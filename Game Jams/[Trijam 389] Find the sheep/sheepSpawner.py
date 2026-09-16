from random import randrange

from sheep import Sheep
from config import STARTING_SHEEP_COUNT, DIFFICULTY_SCALING


class SheepSpawner:
    def __init__(self, width: int, height: int, menu_exclusion_zone: tuple):
        self.width = width
        self.height = height
        self.menu_exclusion_zone = menu_exclusion_zone

    def spawn(self, level: int) -> list:
        sheep_count = (level - 1) * DIFFICULTY_SCALING + STARTING_SHEEP_COUNT
        flock = []
        for _ in range(sheep_count):
            pos = self.get_random_sheep_pos()
            flock.append(
                Sheep(
                    pos,
                    image_path="Art/Sheep1.png",
                    dead_image_path="Art/SheepDead1.png",
                    sick_image_path="Art/SickSheep1.png",
                    blaa_sounds=["Hidden/blaa1.ogg", "Hidden/blaa2.ogg", "Hidden/blaa3.ogg"],
                )
            )
        return flock

    def get_random_sheep_pos(self) -> tuple:
        x_min, x_max = self.menu_exclusion_zone[0]
        y_min, y_max = self.menu_exclusion_zone[1]

        while True:
            pos = (randrange(self.width - 40), randrange(self.height - 40))
            if x_min < pos[0] < x_max and y_min < pos[1] < y_max:
                continue
            return pos
