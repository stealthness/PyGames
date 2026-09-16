import pygame
from random import randint

from core.config import SICK_SHEEP_DELAY_MIN, SICK_SHEEP_DELAY_MAX
from npcs.sheepSpawner import SheepSpawner
from npcs.wolfSpawner import WolfSpawner


class CreatureManager:
    def __init__(self, width: int, height: int, images, menu_exclusion_zone: tuple):
        self.width = width
        self.height = height
        self.images = images
        self.sheep_spawner = SheepSpawner(width, height, menu_exclusion_zone, images)
        self.wolf_spawner = WolfSpawner(width, height, images)
        self.flock = []
        self.wolf_pack = []
        self.next_sick_delay = randint(SICK_SHEEP_DELAY_MIN, SICK_SHEEP_DELAY_MAX)
        self.next_sick_timer = pygame.time.get_ticks() + self.next_sick_delay

    def init_level(self, level: int):
        self.flock.clear()
        self.wolf_pack.clear()
        self.flock.extend(self.sheep_spawner.spawn(level))
        self.wolf_pack.extend(self.wolf_spawner.spawn(level))
        self.reset_sick_timers()

    def reset_sick_timers(self):
        self.next_sick_delay = randint(SICK_SHEEP_DELAY_MIN, SICK_SHEEP_DELAY_MAX)
        self.next_sick_timer = pygame.time.get_ticks() + self.next_sick_delay

    def handle_click(self, pos) -> int:
        score = 0
        for sheep in self.flock:
            score += sheep.handle_click(pos)
        return score

    def update_sick_sheep(self) -> int:
        current_ticks = pygame.time.get_ticks()
        strikes_added = 0
        if current_ticks >= self.next_sick_timer:
            self.next_sick_timer = current_ticks + self.next_sick_delay

            active_sheep = [s for s in self.flock if not (s.isFound or s.isDead)]
            sick_sheep = [s for s in active_sheep if s.isSick]

            if sick_sheep:
                for sheep in sick_sheep:
                    sheep.die()
                strikes_added += 1

            if len(active_sheep) > 2:
                healthy_sheep = [s for s in active_sheep if not s.isSick]
                if healthy_sheep:
                    healthy_sheep[randint(0, len(healthy_sheep) - 1)].make_sick()

        return strikes_added

    def update_wolves(self) -> int:
        strikes_added = 0
        for wolf in self.wolf_pack:
            if wolf.is_active:
                wolf.update()
                strikes_added += wolf.check_sheep_collision(self.flock)
        return strikes_added

    def update(self) -> int:
        return self.update_sick_sheep() + self.update_wolves()

    def draw(self, screen):
        for sheep in self.flock:
            sheep.draw(screen)
        for wolf in self.wolf_pack:
            wolf.draw(screen)

    def all_sheep_found(self) -> bool:
        return all(sheep.isFound or sheep.isDead for sheep in self.flock)

    def get_random_sheep_pos(self):
        return self.sheep_spawner.get_random_sheep_pos()
