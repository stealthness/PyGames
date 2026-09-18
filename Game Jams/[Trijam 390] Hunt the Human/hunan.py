from config import human_default_image

class Human:
    def __init__(self):
        self.image = human_default_image
        
    def draw(self, screen):
        screen.blit(self.image, (0,0))
        
    def update(self):
        pass