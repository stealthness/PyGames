import pygame
import random
from SimpleVerticalRunner.rock import Rock


class RockManager:

    def __init__(self, rock_count = 5):
        self.rock_count = rock_count
        self.rocks = []
        for i in range(rock_count):
            self.rocks.append(Rock(f'rock{i}'))
            self.rocks[i].active = False


    def update(self):

        if random.randint(0,100) < 5:
            for rock in self.rocks:
                if not rock.active:
                    self.activate_rock(rock)
                    break


    def is_all_active(self) -> bool:
        for rock in self.rocks:
            if not rock.active:
                return False
        return True

    @staticmethod
    def activate_rock(rock):
        rock.reset()
        rock.active = True