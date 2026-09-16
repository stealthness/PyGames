import asyncio
import pygame

from core.game_status import GameStatus
from managers.musicManager import MusicManager
from managers.menuManager import MenuManager
from managers.creatureManager import CreatureManager
from core.image_store import ImageStore
from npcs.hayBaleSpawner import HayBaleSpawner
from npcs.shotGun import ShotGun
from core.config import (
    TIMER_SECONDS, MAX_STRIKES, FPS, SHOTGUN_MAX_BULLETS,
    LEVEL_TRANSITION_TIMEOUT, MENU_EXCLUSION_ZONE
)


class Game:
    """Main game class managing game state and logic."""
    
    def __init__(self, screen, images: ImageStore, music_path):
        self.screen = screen
        self.images = images
        self.background = images.backgrounds[0]
        self.next_level_background = images.backgrounds[1]
        self.game_over_background = images.backgrounds[2]
        self.creature_manager = CreatureManager(screen.get_width(), screen.get_height(), images, MENU_EXCLUSION_ZONE)
        self.hay_bale_spawner = HayBaleSpawner(images, self.creature_manager.get_random_sheep_pos)
        self.hay_bales = []
        self.shotgun = ShotGun(SHOTGUN_MAX_BULLETS)
        self.musicManager = MusicManager(music_path)
        self.menuManager = MenuManager(self.screen, timer_seconds=TIMER_SECONDS)
        self.level = 1
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.game_over_button_rect = None
        self.score = 0
        self.strikes = 0
        self.start_ticks = pygame.time.get_ticks()
    
    def game_init(self, level: int = 1):
        """Initialize a new level with sheep."""
        self.level = level
        self.musicManager.play_music()
        self.creature_manager.init_level(level)
        self.hay_bales = self.hay_bale_spawner.spawn(level)
        self.start_ticks = pygame.time.get_ticks()

    def check_game_over(self, remaining: int) -> bool:
        """Check if game should end."""
        return remaining <= 0 or self.strikes >= MAX_STRIKES
    
    def draw_background(self):
        """Draw the game background."""
        if self.background is None:
            self.screen.fill((0, 0, 0))
        else:
            self.screen.blit(self.background, (0, 0))

    def draw_ui_strip(self):
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, self.width, 64))

    def handle_events(self) -> str:
        """Handle input events and return status."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "quit"
                elif event.key == pygame.K_m:
                    self.musicManager.toggle_music()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                self.score += self.creature_manager.handle_click(pos)
        return "continue"

    async def run(self) -> GameStatus:
        """Main game loop. Returns game status (quit, game_over, next_level)."""
        while True:
            # Draw background
            self.draw_background()
            
            # Handle input
            status = self.handle_events()
            if status == "quit":
                return GameStatus.QUIT
            
            self.strikes += self.creature_manager.update()
            
            # Draw all sheep and UI
            self.creature_manager.draw(self.screen)
            self.creature_manager.draw_hover_pointer(self.screen, pygame.mouse.get_pos())
            for hay_bale in self.hay_bales:
                hay_bale.draw(self.screen)
            self.draw_ui_strip()
            self.menuManager.draw_score(self.score)
            
            # Draw countdown timer
            remaining = self.menuManager.draw_timer(self.start_ticks)
            
            self.menuManager.draw_deaths(self.strikes)
            self.menuManager.draw_bullets(self.shotgun.bullets)
            
            # Check if game over
            if self.check_game_over(remaining):
                self.screen.blit(self.game_over_background, (0, 0))
                self.musicManager.stop_music()
                if self.strikes >= MAX_STRIKES:
                    self.game_over_button_rect = self.menuManager.show_end_screen(self.game_over_background, self.score, "You lost too many sheep")
                else:
                    self.game_over_button_rect = self.menuManager.show_end_screen(self.game_over_background, self.score, "You took too long to find the Sheep")
                pygame.display.flip()
                return GameStatus.GAME_OVER
            
            # Check if all sheep found
            all_found = self.creature_manager.all_sheep_found()
            if all_found:
                continue_rect = self.menuManager.show_end_level(self.next_level_background, self.score, self.level)
                self.musicManager.stop_music()
                pygame.display.flip()
                
                # Wait for player to continue
                clicked = False
                wait_start = pygame.time.get_ticks()
                while not clicked and (pygame.time.get_ticks() - wait_start) < LEVEL_TRANSITION_TIMEOUT:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            return "quit"
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                return "quit"
                            else:
                                clicked = True
                                break
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            if continue_rect.collidepoint(event.pos):
                                clicked = True
                                break
                    pygame.display.flip()
                    await asyncio.sleep(0.05)
                
                # Prepare next level
                self.level += 1
                self.game_init(self.level)
                continue
            
            pygame.display.flip()
            await asyncio.sleep(1 / FPS)
