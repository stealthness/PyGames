import random

from config import (
    FOX_BOTTOM_OFFSET,
    FOX_HITBOX_INSET_X,
    FOX_HITBOX_INSET_Y,
    FOX_MAX_SPEED,
    FOX_RIDING_FRAME_MS,
    FOX_SPEED,
    FOX_SPAWN_INTERVAL_DECREASE_MS,
    FOX_SPAWN_INTERVAL_MIN_MS,
    FOX_SPAWN_INTERVAL_START_MS,
    FOX_SPAWN_INTERVAL_VARIATION_MS,
    FOX_START_X,
    SCREEN_HEIGHT,
    fox_image,
    #fox_riding_frames,
)

class Fox:

    """
    fox is an enemy that will move from the right or left across the screen
    if fox touches a person it will double in speed and player life is taken off
    """
    def __init__(self):
        # Image
        self.image = fox_image
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN_HEIGHT - FOX_BOTTOM_OFFSET
        self.rect.x = FOX_START_X
        # Animation
        #self.riding_frames = fox_riding_frames
        self.riding_frame_index = 0
        self.riding_frame_elapsed_ms = 0
        # Movement
        self.base_speed = FOX_SPEED
        self.max_speed = FOX_MAX_SPEED
        self.speed_x = -self.base_speed
        self.active = True
        # Hit Box
        self.hitbox = self.rect.inflate(-FOX_HITBOX_INSET_X, -FOX_HITBOX_INSET_Y)
        self.hitbox.midbottom = self.rect.midbottom

    def update(self, dt_ms=0):
        self.move()
        #self._update_animation(dt_ms)

    def move(self):
        """Move fox in one direction and finish when off-screen."""
        if not self.active:
            return

        self.rect.x += self.speed_x

        if self.rect.right < 0:
            self.active = False


    def draw(self, screen):
        if not self.active:
            return
        screen.blit(self.image, self.rect)

    def is_finished(self):
        return not self.active

    def _sync_hitbox(self):
        self.hitbox.midbottom = self.rect.midbottom

    def _update_animation(self, dt_ms):
        if not self.active:
            return

        self.riding_frame_elapsed_ms += dt_ms
        while self.riding_frame_elapsed_ms >= FOX_RIDING_FRAME_MS:
            self.riding_frame_elapsed_ms -= FOX_RIDING_FRAME_MS
            self.riding_frame_index = (self.riding_frame_index + 1) % len(self.riding_frames)

            anchor = self.rect.midbottom
            self.image = self.riding_frames[self.riding_frame_index]
            self.rect = self.image.get_rect()
            self.rect.midbottom = anchor
            self._sync_hitbox()


        self._sync_hitbox()

    def on_player_collision(self):
        """Increase fox speed after hitting the player."""
        if not self.active:
            return
        current_magnitude = min(abs(self.speed_x) * 2, self.max_speed)
        self.speed_x = current_magnitude if self.speed_x >= 0 else -current_magnitude

    def reset_speed(self):
        """Reset fox speed to base pace."""
        self.speed_x = self.base_speed if self.speed_x >= 0 else -self.base_speed

    def get_collision_rect(self):
        if not self.active:
            return None
        return self.hitbox.copy()
    
class FoxGenerator:
    """
    Manages the fox generation
    foxes will begin generating a fox every 3 secs, and will shorten to increase difficulty 
    """
    
    def __init__(self):
        self.foxes = []
        self.spawn_interval_ms = max(FOX_SPAWN_INTERVAL_START_MS, FOX_SPAWN_INTERVAL_MIN_MS)
        self.minimum_spawn_interval_ms = min(FOX_SPAWN_INTERVAL_START_MS, FOX_SPAWN_INTERVAL_MIN_MS)
        self.spawn_interval_decrease_ms = FOX_SPAWN_INTERVAL_DECREASE_MS
        self.spawn_variation_ms = FOX_SPAWN_INTERVAL_VARIATION_MS
        self.time_until_spawn_ms = self._get_next_spawn_interval_ms()
        self.total_spawned = 0

    def _get_next_spawn_interval_ms(self):
        variation = random.randint(-self.spawn_variation_ms, self.spawn_variation_ms)
        return max(self.minimum_spawn_interval_ms, self.spawn_interval_ms + variation)

    def _decrease_spawn_interval_ms(self):
        self.spawn_interval_ms = max(
            self.minimum_spawn_interval_ms,
            self.spawn_interval_ms - self.spawn_interval_decrease_ms,
        )

    def add_fox(self, fox):
        self.foxes.append(fox)
        self.total_spawned += 1

    def remove_fox(self, fox):
        if fox in self.foxes:
            self.foxes.remove(fox)

    def update(self, dt_ms=0):
        self.time_until_spawn_ms -= dt_ms
        while self.time_until_spawn_ms <= 0:
            self.add_fox(Fox())
            self._decrease_spawn_interval_ms()
            self.time_until_spawn_ms += self._get_next_spawn_interval_ms()

        for fox in self.foxes:
            fox.update(dt_ms)

        self.foxes = [fox for fox in self.foxes if not fox.is_finished()]

    def get_all_foxes(self):
        return self.foxes

    def draw_all(self, screen):
        for fox in self.foxes:
            fox.draw(screen)
    
    