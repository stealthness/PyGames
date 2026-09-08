
import pygame
from menu_manager_class import MenuManager, MenuAction


class Game:

    def __init__(self, _screen):
        self.screen = _screen
        self.state = GameState.Menu
        self.background_color = (20, 20, 20)
        self.update_background()
        self.menu = MenuManager(self.screen)
        
    def handle_events(self):
        """
        Handle events, return False if need to exit the application, True otherwise
        :return True if game continues, or False if the Game is to exit application
        """
        
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                return False
        
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_SPACE:
                    self.state = GameState((self.state.value + 1) % 4)
                    self.update_background()
                    
        return True

    def update(self, dt):
        #set background
        # fill the background each frame so old frames are cleared
        self.screen.fill(self.background_color)
        
        action = True
        if self.state == GameState.Menu:
            # let the menu handle its own input
            result = self.menu.handle_event()
            # draw the menu every frame
            self.menu.draw()

            # menu returns "play" or "quit" (or None). If quit -> stop,
            # otherwise keep running (Play or None both continue)
            if result == MenuAction.QuitAction:
                action = False
            else:
                if result == MenuAction.PlayAction:
                    self.state = GameState.Playing
                    self.update_background()
                action = True
        else:
            action = self.handle_events()

        

        
        # display the screen
        pygame.display.flip()
        
        return action

    def update_background(self):
        match self.state:
            case GameState.Menu:
                self.background_color = (20, 20, 20)
            case GameState.Playing:
                self.background_color = (120, 20, 20)
            case GameState.Finished:
                self.background_color = (20, 20, 120)
            case GameState.Paused:
                self.background_color = (20, 120, 20)


from enum import Enum

class GameState(Enum):
    Menu = 0
    Playing = 1
    Paused = 2
    Finished = 3
    
