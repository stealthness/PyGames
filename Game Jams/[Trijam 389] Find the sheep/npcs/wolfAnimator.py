from random import randint

import pygame

from core.config import WOLF_ANIMATION_RATE_MS, WOLF_SLOW_ANIMATION_RATE_MS


class WolfAnimator:
    def __init__(self, wolf_frames):
        self.wolf_frames = wolf_frames or []
        self.animation_rate_ms = WOLF_ANIMATION_RATE_MS
        self.slow_animation_rate_ms = WOLF_SLOW_ANIMATION_RATE_MS
        self.animation_start_ticks = pygame.time.get_ticks()
        self.animation_frame_offset = randint(0, len(self.wolf_frames) - 1) if self.wolf_frames else 0

    def get_current_image(self, is_slow_zone: bool):
        if not self.wolf_frames:
            return pygame.Surface((1, 1), pygame.SRCALPHA)

        elapsed = pygame.time.get_ticks() - self.animation_start_ticks
        rate = self.slow_animation_rate_ms if is_slow_zone else self.animation_rate_ms
        frame_index = ((elapsed // rate) + self.animation_frame_offset) % len(self.wolf_frames)
        return self.wolf_frames[frame_index]

    def get_base_width(self):
        return self.get_current_image(False).get_width()
