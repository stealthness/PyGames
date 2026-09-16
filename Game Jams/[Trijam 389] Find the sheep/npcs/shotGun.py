import pygame

from core.config import SHOTGUN_COOLDOWN_MS


class ShotGun:
    def __init__(self, max_bullets=6):
        self.max_bullets = max_bullets
        self.bullets = max_bullets
        self.cooldown_ms = SHOTGUN_COOLDOWN_MS
        self.last_fire_ticks = -self.cooldown_ms

    def can_fire(self):
        current_ticks = pygame.time.get_ticks()
        return self.bullets > 0 and (current_ticks - self.last_fire_ticks) >= self.cooldown_ms

    def fire(self):
        if not self.can_fire():
            return False

        self.bullets -= 1
        self.last_fire_ticks = pygame.time.get_ticks()
        return True

    def get_bullets_text(self):
        return f"Bullets: {self.bullets}"
