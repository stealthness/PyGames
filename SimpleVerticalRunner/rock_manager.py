import pygame
import random
from SimpleVerticalRunner.rock import Rock
debug_mode = True


class RockManager:

    def __init__(self, rock_count = 5):
        self.rock_count = rock_count
        self.rocks = []
        for i in range(rock_count):
            self.rocks.append(Rock())
            self.rocks[i].active = False


    def update(self):
        if debug_mode:
            print(f'RockManager.update() called, active rocks: {self.size()}')
        if random.randint(0,100) < 2:
            for rock in self.rocks:
                if not rock.active:
                    self.activate_rock(rock)
                    return rock
                    break

        return None

    def size(self):
        count = 0
        for rock in self.rocks:
            if rock.active:
                count += 1
        return count


    def is_all_active(self) -> bool:
        for rock in self.rocks:
            if not rock.active:
                return False
        return True


    def activate_rock(self, rock):
        print('activate rock')
        rock.reset()
        rock.active = True