import asyncio
import pygame
from random import randint, randrange

from pygame.examples.cursors import image

from musicManager import MusicManager
from menuManager import MenuManager
from sheep import Sheep
from wolf import Wolf
from config import (
    TIMER_SECONDS, MAX_STRIKES, STARTING_SHEEP_COUNT, DIFFICULTY_SCALING,
    SICK_SHEEP_DELAY_MIN, SICK_SHEEP_DELAY_MAX, LEVEL_TRANSITION_TIMEOUT,
    MENU_EXCLUSION_ZONE, STARTING_WOLF_COUNT
)


class Game:
    """Main game class managing game state and logic."""
    
    def __init__(self, screen, backgrounds, flock, pack, music_path):
        self.screen = screen
        self.background = backgrounds[0]
        self.next_level_background = backgrounds[1]
        self.game_over_background = backgrounds[2]
        self.flock = flock
        self.wolf_pack = pack
        self.musicManager = MusicManager(music_path)
        self.menuManager = MenuManager(self.screen, timer_seconds=TIMER_SECONDS)
        self.level = 1
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.score = 0
        self.strikes = 0
        
        # Sick sheep timer state
        self.next_sick_delay = randint(SICK_SHEEP_DELAY_MIN, SICK_SHEEP_DELAY_MAX)
        self.start_ticks = pygame.time.get_ticks()
        self.next_sick_timer = self.start_ticks + self.next_sick_delay
    
    def game_init(self, level: int = 1):
        """Initialize a new level with sheep."""
        self.level = level
        self.musicManager.play_music()
        self.flock.clear()
        self.wolf_pack.clear()
        sheep_count = (level - 1) * DIFFICULTY_SCALING + STARTING_SHEEP_COUNT
        wolf_count = STARTING_WOLF_COUNT + ((level - 1) // 2)
        for _ in range(sheep_count):
            pos = self.get_random_sheep_pos()
            self.flock.append(Sheep(pos, image_path="Art/Sheep1.png", dead_image_path="Art/SheepDead1.png", sick_image_path="Art/SickSheep1.png",
                                    blaa_sounds=["Hidden/blaa1.ogg", "Hidden/blaa2.ogg", "Hidden/blaa3.ogg"]))
        
        min_wolf_y = 80
        max_wolf_y = max(min_wolf_y, self.height - 80)
        for i in range(wolf_count):
            y = randint(min_wolf_y, max_wolf_y)
            if i % 2 == 0:
                pos = (-120 - (i * 80), y)
                direction = 1
            else:
                pos = (self.width + (i * 80), y)
                direction = -1

            wolf = Wolf(pos, "Art/wolkf1.png")
            wolf.direction = direction
            wolf.activate(pos)
            self.wolf_pack.append(wolf)
        
        # Reset sick sheep timers
        self.next_sick_delay = randint(SICK_SHEEP_DELAY_MIN, SICK_SHEEP_DELAY_MAX)
        self.start_ticks = pygame.time.get_ticks()
        self.next_sick_timer = self.start_ticks + self.next_sick_delay

    def get_random_sheep_pos(self) -> tuple:
        """Get a random position for a sheep, avoiding exclusion zone."""
        x_min, x_max = MENU_EXCLUSION_ZONE[0]
        y_min, y_max = MENU_EXCLUSION_ZONE[1]
        
        while True:
            pos = (randrange(self.width - 40), randrange(self.height - 40))
            if x_min < pos[0] < x_max and y_min < pos[1] < y_max:
                continue
            return pos
    
    def check_game_over(self, remaining: int) -> bool:
        """Check if game should end."""
        return remaining <= 0 or self.strikes >= MAX_STRIKES
    
    def update_sick_sheep(self):
        """Apply sickness and death to sheep on timer."""
        current_ticks = pygame.time.get_ticks()
        if current_ticks >= self.next_sick_timer:
            # Set next timer: current time + random delay
            self.next_sick_timer = current_ticks + self.next_sick_delay
            
            # Find active (not found, not dead) sheep
            active_sheep = [s for s in self.flock if not (s.isFound or s.isDead)]
            sick_sheep = [s for s in active_sheep if s.isSick]
            
            # Kill sick sheep (1 strike per tick, regardless of count)
            if sick_sheep:
                for sheep in sick_sheep:
                    sheep.die()
                self.strikes += 1
            
            # Make a random healthy sheep sick provided there are 3 healthy active sheep
            if len(active_sheep) > 2:
                healthy_sheep = [s for s in active_sheep if not s.isSick]
                if healthy_sheep:
                    healthy_sheep[randint(0, len(healthy_sheep) - 1)].make_sick()

    def draw_background(self):
        """Draw the game background."""
        if self.background is None:
            self.screen.fill((0, 0, 0))
        else:
            self.screen.blit(self.background, (0, 0))

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
                for sheep in self.flock:
                    self.score += sheep.handle_click(pos)
        return "continue"

    async def run(self) -> str:
        """Main game loop. Returns game status (quit, game_over, next_level)."""
        while True:
            # Draw background
            self.draw_background()
            
            # Handle input
            status = self.handle_events()
            if status == "quit":
                return "quit"
            
            # Update sheep sickness state
            self.update_sick_sheep()
            
            # Update wolf appearance
            self.strikes += self.update_wolf_pack()
            
            # Draw all sheep and UI
            for sheep in self.flock:
                sheep.draw(self.screen)
            for wolf in self.wolf_pack:
                wolf.draw(self.screen)
            self.menuManager.draw_score(self.score)
            
            # Draw countdown timer
            remaining = self.menuManager.draw_timer(self.start_ticks)
            
            self.menuManager.draw_deaths(self.strikes)
            
            # Check if game over
            if self.check_game_over(remaining):
                self.screen.blit(self.game_over_background, (0, 0))
                self.musicManager.stop_music()
                if self.strikes >= MAX_STRIKES:
                    self.menuManager.show_end_screen(self.game_over_background, self.score, "You lost too many sheep")
                else:
                    self.menuManager.show_end_screen(self.game_over_background, self.score, "You took too long to find the Sheep")
                pygame.display.flip()
                return "game_over"
            
            # Check if all sheep found
            all_found = all(sheep.isFound or sheep.isDead for sheep in self.flock)
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
            await asyncio.sleep(0)

    def update_wolf_pack(self) -> int:
        active_pack_sheep_eaton_count = 0
        for wolf in self.wolf_pack:
            if wolf.is_active:
                wolf.update()
                active_pack_sheep_eaton_count += wolf.check_sheep_collision(self.flock)
        
        return active_pack_sheep_eaton_count
