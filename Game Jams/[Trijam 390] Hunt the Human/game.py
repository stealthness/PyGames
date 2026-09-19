from enum import Enum

import pygame

from background_controller import BackgroundController
from config import (
    TEST_MODE_DEFAULT,
    TEST_MODE_HITBOX_COLOR,
    TEST_MODE_HITBOX_WIDTH,
    TEST_MODE_TOGGLE_KEY,
)
from fox import FoxGenerator
from game_ui_manager import GameUIManager
from human import Human
from wall import WallGenerator


class Game:
    """
    This is the main game class.
    the game is a vertical runner game.
    
    """
    
    def __init__(self, screen):
        self.screen = screen
        self.background_controller = BackgroundController()
        self.game_ui_manager = GameUIManager()
        self.human = Human()
        self.fox_generator = FoxGenerator()
        self.wall_generator = WallGenerator()
        self.game_objects = [self.human]
        self.test_mode = TEST_MODE_DEFAULT
        self.quit_requested = False
        
        
    def run(self, dt_ms=0):
        # Run one frame and report whether the game should continue.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_requested = True
                return False
            if event.type == pygame.KEYDOWN and event.key == TEST_MODE_TOGGLE_KEY:
                self.test_mode = not self.test_mode

        self.update(dt_ms)
        if not self.human.is_alive():
            return False
        self.draw()
        return True
        
        
    def update(self, dt_ms=0):
        """
        this function update all game objects connect to the game class
        :return: 
        """
        self.background_controller.update()
        self.fox_generator.update(dt_ms)
        self.wall_generator.update(dt_ms)
        self.wall_generator.move_all()
        for game_object in self.game_objects:
            game_object.update(dt_ms)
        self.check_collisions()
        self.wall_generator.cleanup()
        self.check_fox_collisions()
        self.game_ui_manager.update_health(self.human.lives)

    def check_fox_collisions(self):
        """Handle fox collisions with the player."""
        player_hitbox = self.human.get_collision_rect()
        for fox in self.fox_generator.get_all_foxes():
            fox_hitbox = fox.get_collision_rect()
            if fox_hitbox and player_hitbox.colliderect(fox_hitbox):
                self.human.take_damage(1)
                fox.on_player_collision()
                break

    def check_collisions(self):
        """Resolve wall collisions: safe top-landings, damaging side impacts."""
        landed_on_wall = False
        player_collision_rect = self.human.get_collision_rect()

        for wall in self.wall_generator.get_all_walls():
            wall_collision_rect = wall.get_collision_rect()

            if not player_collision_rect.colliderect(wall_collision_rect):
                continue

            is_descending = self.human.velocity_y >= 0
            was_above_wall = (
                self.human.previous_hitbox.bottom
                <= wall_collision_rect.top + self.human.platform_land_tolerance
            )

            if is_descending and was_above_wall:
                self.human.land_on_surface(wall_collision_rect.top)
                landed_on_wall = True
                continue

            if player_collision_rect.colliderect(wall_collision_rect):
                self.human.take_damage(1)
                break

        if not landed_on_wall and self.human.hitbox.bottom < self.human.ground_hitbox_bottom:
            self.human.on_ground = False
    
    def draw(self):
        """
        The function will draw all the game objects connect to the game class
        :return: 
        """
        self.background_controller.draw(self.screen)
        self.wall_generator.draw_all(self.screen)
        self.fox_generator.draw_all(self.screen)
        for game_object in self.game_objects:
            game_object.draw(self.screen)
        if self.test_mode:
            self.draw_collision_hitboxes()
        self.game_ui_manager.draw(self.screen)
        pygame.display.flip()

    def draw_collision_hitboxes(self):
        """Draw debug hitboxes for all collidable game objects."""
        collidables = (
            list(self.game_objects)
            + self.wall_generator.get_all_walls()
            + self.fox_generator.get_all_foxes()
        )
        for game_object in collidables:
            if hasattr(game_object, "get_collision_rect"):
                hitbox = game_object.get_collision_rect()
                if hitbox is None:
                    continue
                pygame.draw.rect(
                    self.screen,
                    TEST_MODE_HITBOX_COLOR,
                    hitbox,
                    TEST_MODE_HITBOX_WIDTH,
                )
        
class GameStatus(Enum):
    
    Splash = 0,
    Menu = 1,
    Game = 2,
    EndGame = 3,