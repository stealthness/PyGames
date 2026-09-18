import pygame

from config import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    HUMAN_BOTTOM_OFFSET,
    HUMAN_GRAVITY,
    HUMAN_HITBOX_INSET_X,
    HUMAN_HITBOX_INSET_Y,
    HUMAN_INVULNERABILITY_FRAMES,
    HUMAN_JUMP_VELOCITY,
    HUMAN_MAX_FALL_SPEED,
    HUMAN_START_LIVES,
    human_default_image,
)

class Human:
    """
    The human class is the main player character, it positions in the center bottom screen about 50 pixel off from the bottom
    the human will always be running to the right, this is achieved by moving all other objects to the left.
    The human will be able to jump (press space) a "human_jump_height" of 100 pixels (adjustable)
    the human will also be able to hide in holes (press down), to climb trees (press up). They will remain there untill
    the reverse action is performed, climb down the tree or climb up the hole. When in a hole the play is not moving forward.
    A player will have three lives, touch a dangerous object, enemy or hitting wall or will lose one life.
    
    """

    def __init__(self):
        self.image = human_default_image
        self.rect = self.image.get_rect()
        self.rect.midbottom = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - HUMAN_BOTTOM_OFFSET)

        # Core movement tuning values.
        self.gravity = HUMAN_GRAVITY
        self.jump_velocity = HUMAN_JUMP_VELOCITY
        self.max_fall_speed = HUMAN_MAX_FALL_SPEED

        self.velocity_y = 0.0
        self.ground_y = self.rect.y

        self.lives = HUMAN_START_LIVES
        self.in_hole = False
        self.on_tree = False
        self.on_ground = True
        self.invulnerability_frames = 0

        # Track prior key state so mode toggles happen once per key press.
        self._previous_keys = {
            pygame.K_SPACE: False,
            pygame.K_UP: False,
            pygame.K_DOWN: False,
        }

    def _just_pressed(self, keys, key_code):
        pressed_now = bool(keys[key_code])
        was_pressed = self._previous_keys[key_code]
        self._previous_keys[key_code] = pressed_now
        return pressed_now and not was_pressed

    def start_jump(self):
        if self.on_ground and not self.in_hole and not self.on_tree:
            self.velocity_y = self.jump_velocity
            self.on_ground = False

    def toggle_hole(self):
        if self.on_tree:
            return
        self.in_hole = not self.in_hole

    def toggle_tree(self):
        if self.in_hole:
            return
        self.on_tree = not self.on_tree

    def apply_gravity(self):
        if self.in_hole or self.on_tree:
            return

        self.velocity_y = min(self.velocity_y + self.gravity, self.max_fall_speed)
        self.rect.y += int(self.velocity_y)

        if self.rect.y >= self.ground_y:
            self.rect.y = self.ground_y
            self.velocity_y = 0
            self.on_ground = True

    def get_collision_rect(self):
        return self.rect.inflate(-HUMAN_HITBOX_INSET_X, -HUMAN_HITBOX_INSET_Y)

    def take_damage(self, amount=1):
        if self.invulnerability_frames > 0:
            return
        self.lives = max(0, self.lives - amount)
        self.invulnerability_frames = HUMAN_INVULNERABILITY_FRAMES

    def is_alive(self):
        return self.lives > 0
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def update(self):
        keys = pygame.key.get_pressed()

        if self._just_pressed(keys, pygame.K_SPACE):
            self.start_jump()
        if self._just_pressed(keys, pygame.K_DOWN):
            self.toggle_hole()
        if self._just_pressed(keys, pygame.K_UP):
            self.toggle_tree()

        self.apply_gravity()

        if self.invulnerability_frames > 0:
            self.invulnerability_frames -= 1
