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
    HUMAN_KEYS_CLIMB,
    HUMAN_KEYS_HIDE,
    HUMAN_KEYS_JUMP,
    HUMAN_MAX_FALL_SPEED,
    HUMAN_START_LIVES,
    HUMAN_WALK_FRAME_TICKS,
    human_default_image,
    human_walk_frames,
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
        self.walk_frames = human_walk_frames
        self.walk_frame_index = 0
        self.walk_frame_tick = 0

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

        # Track prior action state so toggles happen once per key press.
        self._action_key_map = {
            "jump": HUMAN_KEYS_JUMP,
            "hide": HUMAN_KEYS_HIDE,
            "climb": HUMAN_KEYS_CLIMB,
        }
        self._previous_actions = {
            "jump": False,
            "hide": False,
            "climb": False,
        }

    def _just_pressed(self, keys, action):
        pressed_now = any(keys[key_code] for key_code in self._action_key_map[action])
        was_pressed = self._previous_actions[action]
        self._previous_actions[action] = pressed_now
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

    def update_animation(self):
        if self.in_hole or self.on_tree:
            self.walk_frame_index = 0
            self.image = self.walk_frames[self.walk_frame_index]
            return

        self.walk_frame_tick += 1
        if self.walk_frame_tick < HUMAN_WALK_FRAME_TICKS:
            return

        self.walk_frame_tick = 0
        self.walk_frame_index = (self.walk_frame_index + 1) % len(self.walk_frames)

        anchor = self.rect.midbottom
        self.image = self.walk_frames[self.walk_frame_index]
        self.rect = self.image.get_rect()
        self.rect.midbottom = anchor

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

        if self._just_pressed(keys, "jump"):
            self.start_jump()
        if self._just_pressed(keys, "hide"):
            self.toggle_hole()
        if self._just_pressed(keys, "climb"):
            self.toggle_tree()

        self.apply_gravity()
        self.update_animation()

        if self.invulnerability_frames > 0:
            self.invulnerability_frames -= 1
