import os
from random import randint

import pygame


class ImageStore:
    def __init__(self, base_dir: str):
        self.base_dir = base_dir
        self.backgrounds = [
            self._load("Art", "background.png"),
            self._load("Art", "next_level_background.png"),
            self._load("Art", "game_over_background.png"),
            self._load("Art", "menu_background.png"),
        ]
        self.sheep_images = [
            self._load("Art", "Sheep1.png"),
            self._load("Art", "Sheep2.png"),
            self._load("Art", "Sheep3.png"),
        ]
        self.sick_sheep_images = [
            self._load("Art", "SickSheep1.png"),
            self._load("Art", "SickSheep2.png"),
            self._load("Art", "SickSheep3.png"),
        ]
        self.dead_sheep_image = self._load("Art", "SheepDead1.png")
        self.wolf_images = [
            self._load("Art", "wolkf1.png"),
            self._load("Art", "wolkf2.png"),
            self._load("Art", "wolkf3.png"),
            self._load("Art", "wolkf4.png"),
        ]
        self.hay_bale_image = self._load("Art", "HayBale1.png")
        self.music_path = os.path.join(self.base_dir, "Hidden", "geoffharvey-farmyard-fun-374610.ogg")

    def _load(self, *parts):
        path = os.path.join(self.base_dir, *parts)
        return pygame.image.load(path).convert_alpha()

    def get_backgrounds(self):
        return self.backgrounds

    def get_random_sheep_images(self):
        index = randint(0, len(self.sheep_images) - 1)
        return self.sheep_images[index], self.sick_sheep_images[index]

    def get_dead_sheep_image(self):
        return self.dead_sheep_image

    def get_random_wolf_image(self):
        return self.wolf_images[randint(0, len(self.wolf_images) - 1)]

    def get_hay_bale_image(self):
        return self.hay_bale_image
