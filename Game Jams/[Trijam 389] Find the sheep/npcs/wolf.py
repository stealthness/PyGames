from random import randint, random
import pygame
from core.config import (
    START_WOLF_SPEED,
    NORMAL_WOLF_SPEED,
    VERTICAL_WOLF_SPEED,
    VERTICAL_SWITCH_PERCENTAGE,
    VERTICAL_SWITCH_CHANGE_DELAY,
)
from core.wolf_status import WolfStatus
from npcs.wolfAnimator import WolfAnimator

class Wolf:
    """
    This class represents a wolf on the screen. it starts from just outside the left or right of the screen and will move
    across horizontally and kill any sheep it touches
    """
    def __init__(self, pos = (-300, 200), wolf_frames=None):
        self.is_active = False
        self.hit_points = 3
        self.pos = pos
        self.animator = WolfAnimator(wolf_frames)
        if pos[0] > 0:
            self.direction = 1
        else:
            self.direction = -1
        self.speed = NORMAL_WOLF_SPEED
        self.slow_speed = START_WOLF_SPEED
        self.vertical_speed = VERTICAL_WOLF_SPEED
        self.vertical_direction = 0
        self.next_vertical_switch_ticks = 0
        self.set_edge_limits()
        
        
    def draw(self, screen):
        """
        Draws the wold on the screen
        :param screen: 
        :return: 
        """
        if self.is_active:
            wolf_image = self.get_current_image()
            wolf_image = pygame.transform.flip(wolf_image, self.direction < 0, False)
            screen.blit(wolf_image, (int(self.pos[0]), int(self.pos[1])))
            
    def update(self):
        """
        Moves the wolf to the next position
        :return: 
        """
        if self.is_active:
            if self.get_status() == WolfStatus.SLOW:
                self.update_slow()
            else:
                self.update_normal()

    def update_normal(self):
        if self.pos[0] >= self.right_limit:
            self.direction = -1
            self.pos = (self.pos[0], randint(100, 500))
            self.vertical_direction = 0
            self.schedule_vertical_switch()
        elif self.pos[0] <= self.left_limit:
            self.direction = 1
            self.pos = (self.pos[0], randint(100, 500))
            self.vertical_direction = 0
            self.schedule_vertical_switch()

        self.update_vertical_direction()
        self.move(self.speed)

    def update_slow(self):
        if self.pos[0] >= self.right_limit:
            self.direction = -1
            self.pos = (self.pos[0], randint(100, 500))
        elif self.pos[0] <= self.left_limit:
            self.direction = 1
            self.pos = (self.pos[0], randint(100, 500))
        self.vertical_direction = 0
        self.move(self.slow_speed)

    def move(self, movement_speed):
        x = self.direction * movement_speed + self.pos[0]
        y = self.pos[1] + (self.vertical_direction * self.vertical_speed)
        y = self.clamp_vertical_position(y)
        self.pos = (x, y)
        
    def check_sheep_collision(self, flock) -> int:
        if not self.is_active:
            return 0

        eaton_count = 0
        wolf_rect = self.get_current_image().get_rect(topleft=(int(self.pos[0]), int(self.pos[1])))
        for sheep in flock:
            if sheep.is_active() and wolf_rect.colliderect(sheep.get_rect()):
                sheep.is_attack_by_wolf()
                eaton_count += 1
        return eaton_count
                
            
                
    def activate(self, position):
        self.is_active = True
        self.pos = position
        self.schedule_vertical_switch()

    def set_edge_limits(self):
        surface = pygame.display.get_surface()
        screen_width = surface.get_width() if surface else 1000
        screen_height = surface.get_height() if surface else 1000
        self.screen_width = screen_width
        self.screen_height = screen_height
        wolf_width = self.animator.get_base_width()
        self.right_limit = screen_width + wolf_width * 2
        self.left_limit = -wolf_width * 2

    def get_current_image(self):
        return self.animator.get_current_image(self.is_slow_zone())

    def is_slowing_down(self):
        return (self.direction > 0 and self.pos[0] < 40) or (self.direction < 0 and self.pos[0] > (self.screen_width - 40))

    def is_slow_zone(self):
        return self.is_slowing_down()

    def get_status(self):
        if self.is_slow_zone():
            return WolfStatus.SLOW
        return WolfStatus.NORMAL

    def schedule_vertical_switch(self):
        delay_seconds = randint(VERTICAL_SWITCH_CHANGE_DELAY[0], VERTICAL_SWITCH_CHANGE_DELAY[1])
        self.next_vertical_switch_ticks = pygame.time.get_ticks() + (delay_seconds * 1000)

    def update_vertical_direction(self):
        current_ticks = pygame.time.get_ticks()
        if current_ticks < self.next_vertical_switch_ticks:
            return

        self.schedule_vertical_switch()
        if random() < VERTICAL_SWITCH_PERCENTAGE:
            self.vertical_direction = 0
            return

        self.vertical_direction = -1 if randint(0, 1) == 0 else 1

    def clamp_vertical_position(self, y):
        image_height = self.get_current_image().get_height()
        min_y = 0
        max_y = max(0, self.screen_height - image_height)
        if y < min_y:
            self.vertical_direction = 1
            return min_y
        if y > max_y:
            self.vertical_direction = -1
            return max_y
        return y
    
        
