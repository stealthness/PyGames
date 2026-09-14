import pygame


class MusicManager:
    """
    The purpose of  this class is to manage the music
    """
    
    def __init__(self, music_path):
        self.music = music_path
        self.load_music()
        
        
    def load_music(self):
        pygame.mixer.music.load(self.music)
        
        
    def play_music(self):
        pygame.mixer.music.play()
        
    def stop_music(self):
        pygame.mixer.music.stop()
            