import asyncio
from typing import Self

import pygame
from random import randint, randrange

from menu_manager import MenuManager
from musicManager import MusicManager
from sheep import Sheep


class Game:
    
    def __init__(self, screen, background, flock, music_path ):
        self.screen = screen
        self.background = background
        self.flock = flock
        self.musicManager = MusicManager(music_path)
        self.menuManager = MenuManager(self.screen)
        self.level = 1
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.score = 0
        self.player_lost_sheep_strike = 0
    
    def game_init(self, level= 1):
        self.musicManager.play_music()
        self.flock.clear()
        # create sheep
        for i in range((level -1) * 3 + 5):
            pos = self.get_random_sheep_pos()
            self.flock.append(Sheep(pos, blaa_sounds=["Hidden/blaa1.ogg", "Hidden/blaa2.ogg", "Hidden/blaa3.ogg"]))


    
    def get_random_sheep_pos(self):
        while True:
            pos = randrange((self.width - 40)), randrange((self.height-40))
            if 400 < pos[0] < 500 and 100 < pos[1] < 300:
                continue
            else:
                return pos
    
    
    async def run(self):
        print("Game class running")
        running = True
        while running:
    
            # Draw the self.background
            if self.background is None:
                self.screen.fill((0, 0, 0))
            else:
                self.screen.blit(self.background, (0, 0))
    
            for event in pygame.event.get():
    
                if event.type == pygame.QUIT:
                    running = False
    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key== pygame.K_m:
                        self.musicManager.toggle_music()
    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    for sheep in self.flock:
                        self.score += sheep.handle_click(pos)
    
            # if running is false exit application
            if not running:
                break
    
            self.menuManager.draw_score(self.score)

    
            # Apply sickness to sheep
            if pygame.time.get_ticks() - start_ticks > next_sick_timer:
                next_sick_timer = pygame.time.get_ticks() +  NEXT_SICK_SHEEP_DELAY
                lost_sheep_not_sick = []
                lost_sheep_sick = []
                for sheep in self.flock:
                    if sheep.isFound or sheep.isDead:
                        continue
                    if sheep.isSick:
                        lost_sheep_sick.append(sheep)
                    lost_sheep_not_sick.append(sheep)
    
                for sheep in lost_sheep_sick:
                    sheep.die()
                    self.player_lost_sheep_strike += len(lost_sheep_sick)
    
    
    
                if len(lost_sheep_not_sick) > 1:
                    lost_sheep_not_sick[randint(0, len(lost_sheep_not_sick) - 1)].make_sick()
    
    
            for sheep in self.flock:
                sheep.draw(self.screen)
    
    
    
            # Check if all sheep are found
            all_found = all(sheep.isFound or sheep.isDead for sheep in self.flock)
            if all_found:
                # Draw end level self.screen and get continue button rect
                continue_rect = Self.menuManager.show_end_level(self.score, self.level)
                self.musicManager.stop_music()
                pygame.display.flip()
    
                # Wait up to 3 seconds, but allow player to click Continue to skip the wait
                clicked = False
                wait_start = pygame.time.get_ticks()
                timeout_ms = 8000
                while not clicked and (pygame.time.get_ticks() - wait_start) < timeout_ms and running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            break
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                running = False
                                break
                            else:
                                # any key press also continues
                                clicked = True
                                break
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            if continue_rect.collidepoint(event.pos):
                                clicked = True
                                break
    
                    # keep showing the self.screen
                    pygame.display.flip()
                    await asyncio.sleep(0.05)
    
                pygame.display.flip()
    
                # Advance to next level
                if not running:
                    break
                # increase the level
                self.level += 1
                # reset the level
                self.init_game(self.level)
                # Reset the sick timers
    
                NEXT_SICK_SHEEP_DELAY = randint(800, 2500)
                start_ticks = pygame.time.get_ticks()
                next_sick_timer = start_ticks + NEXT_SICK_SHEEP_DELAY
                continue
    
            # Draw countdown timer at top center
            remaining = self.menuManager.draw_timer(start_ticks)
    
            # If time's up, show final self.screen then quit
            game_status = await check_game_over(remaining, self.score, self.player_lost_sheep_strike)
            
            return game_status

def check_game_over(self, remaining: int, score: int, player_lost_sheep_strike: int) -> str:
    """
    Checks if a game is over
    @param game_over: bool
    @param remaining: int
    @param score: int
    @return: bool, true if game is over, false otherwise
    """
    if remaining <= 0 or player_lost_sheep_strike > 3 :
        self.menuManager.show_end_screen(score)
        self.musicManager.stop_music()
        pygame.display.flip()
        return "game_over"
    return "start_game" 