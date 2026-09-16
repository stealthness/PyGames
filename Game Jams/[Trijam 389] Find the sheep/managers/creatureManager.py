import pygame
from random import randint

from core.config import (
    SICK_SHEEP_DELAY_MIN,
    SICK_SHEEP_DELAY_MAX,
    POINTER_CLICK_FEEDBACK_DURATION_MS,
)
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
        self.pointer_click_active_until = 0
        self.pointer_click_pos = None

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
            if sheep.get_rect().collidepoint(pos) and sheep.is_active():
                self.pointer_click_active_until = pygame.time.get_ticks() + POINTER_CLICK_FEEDBACK_DURATION_MS
                self.pointer_click_pos = sheep.get_rect().topleft
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

    def draw_hover_pointer(self, screen, mouse_pos):
        current_ticks = pygame.time.get_ticks()
        pointer_image = self.images.get_pointer_image()
        pointer_click_image = self.images.get_pointer_click_image()
        pointer_wolf_image = self.images.get_pointer_wolf_image()

        if self.pointer_click_pos is not None and current_ticks < self.pointer_click_active_until:
            screen.blit(pointer_click_image, self.pointer_click_pos)
            return

        self.pointer_click_pos = None

        hovered_wolf = self.get_hovered_wolf(mouse_pos)
        if hovered_wolf is not None:
            screen.blit(pointer_wolf_image, (int(hovered_wolf.pos[0]), int(hovered_wolf.pos[1])))
            return

        hovered_sheep = self.get_hovered_sheep(mouse_pos)
        if hovered_sheep is not None:
            screen.blit(pointer_image, hovered_sheep.get_rect().topleft)

    def get_hovered_wolf(self, mouse_pos):
        for wolf in self.wolf_pack:
            if wolf.is_active and wolf.get_current_image().get_rect(topleft=(int(wolf.pos[0]), int(wolf.pos[1]))).collidepoint(mouse_pos):
                return wolf
        return None

    def get_hovered_sheep(self, mouse_pos):
        for sheep in self.flock:
            if sheep.is_active() and sheep.get_rect().collidepoint(mouse_pos):
                return sheep
        return None

    def all_sheep_found(self) -> bool:
        return all(sheep.isFound or sheep.isDead for sheep in self.flock)

    def get_random_sheep_pos(self):
        return self.sheep_spawner.get_random_sheep_pos()
