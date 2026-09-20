import pygame


class MusicManager:
    """
    The purpose of  this class is to manage the music
    """
    
    def __init__(self, music_path):
        self.music = music_path
        self.load_music()
        self.is_toggled_on = True
        
        
        
    def load_music(self):
        pygame.mixer.music.load(self.music)
        pygame.mixer.init(44100, -16, 2, 2048)
        
        
    def play_music(self):
        if self.is_toggled_on:
            pygame.mixer.music.play()
        
    def stop_music(self):
        pygame.mixer.music.stop()

    def toggle_music(self):

        self.is_toggled_on = not self.is_toggled_on
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            
            