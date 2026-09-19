import random

from config import (
    BACKGROUND_SCROLL_SPEED,
    SCREEN_HEIGHT,
    WALL_SPAWN_INTERVAL_MS,
    WALL_SPAWN_X,
    WALL_VERTICAL_OFFSET,
    WALL_SPAWN_INTERVAL_VARIATION_MS,
    wall_image,
)


class Wall:
    """
    The wall is an obstacle the human player must jump over, or they will lose a life.
    The wall moves to the left like all objects in the game to give the illusion of human player movement.
    """
    def __init__(self, x=WALL_SPAWN_X):
        self.image = wall_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = SCREEN_HEIGHT - WALL_VERTICAL_OFFSET
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def update(self, dt_ms=0):
        """Placeholder for wall-specific updates (if needed)."""
        pass

    def move(self, dx):
        """Move the wall left by dx pixels (for background scroll)."""
        self.rect.x += dx

    def is_off_screen(self):
        """Return True if the wall has scrolled completely off the left edge."""
        return self.rect.right < 0

    def get_collision_rect(self):
        """Return the collision rect for this wall."""
        return self.rect.copy()
    
class WallGenerator:
    """
    The wall generator spawns walls to the right just off-screen at regular intervals.
    It manages the active wall list, removes off-screen walls, and handles scrolling.
    """

    def __init__(self):
        self.walls = []
        self.spawn_timer_ms = 0
        self.spawn_interval_ms = WALL_SPAWN_INTERVAL_MS
        self.spawn_interval_variation_ms = WALL_SPAWN_INTERVAL_VARIATION_MS
        self.next_spawn_interval_ms = self._get_next_spawn_interval_ms()

    def _get_next_spawn_interval_ms(self):
        variation = random.randint(
            -self.spawn_interval_variation_ms,
            self.spawn_interval_variation_ms,
        )
        return max(1, self.spawn_interval_ms + variation)
        
    def update(self, dt_ms=0):
        """Update spawn timer and create walls at configured intervals."""
        self.spawn_timer_ms += dt_ms
        while self.spawn_timer_ms >= self.next_spawn_interval_ms:
            self.spawn_wall()
            self.spawn_timer_ms -= self.next_spawn_interval_ms
            self.next_spawn_interval_ms = self._get_next_spawn_interval_ms()

    def spawn_wall(self):
        """Create a new wall and add it to the active list."""
        new_wall = Wall()
        self.walls.append(new_wall)

    def move_all(self):
        """Move all walls left to match background scroll."""
        scroll_offset = -BACKGROUND_SCROLL_SPEED
        for wall in self.walls:
            wall.move(scroll_offset)

    def cleanup(self):
        """Remove walls that have scrolled off-screen."""
        self.walls = [wall for wall in self.walls if not wall.is_off_screen()]

    def get_all_walls(self):
        """Return the list of active walls."""
        return self.walls

    def draw_all(self, screen):
        """Draw all active walls."""
        for wall in self.walls:
            wall.draw(screen)
