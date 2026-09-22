class Animator:
    """
    A class to manage the animation of a sequence of images.
    """
    def __init__(self, images):
        self.images = images
        self.current_image = 0
        self.frame_rate = 20
        self.tick = 0

    def get_current_image(self):
        """
        Returns the current image of the animator.
        :return: 
        """
        return self.images[self.current_image]

    def next_image(self):
        """
        Returns the next image of the animator.
        :return: 
        """
        self.current_image = (self.current_image + 1) % len(self.images)
        
    def update(self):
        """
        Updates the animator.
        :return: 
        """
        self.tick += 1
        if self.tick >= self.frame_rate:
            self.tick = 0
            self.next_image()
            
    def draw(self, screen):
        """
        Draws the animation image to the screen.
        :param screen: 
        :return: 
        """
        screen.blit(self.get_current_image(), (0, 0))
        