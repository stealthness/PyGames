import pygame


class Animator:

    def __init__(self, path, time, frame_count = 1, frame_times = None):
        self.images = []
        for i in range(frame_count):
            self.images.append(pygame.image.load(f'Art/carol/carol_idle/carol_idle_{i}.png'))
        self.time = time
        self.time_last_frame = pygame.time.get_ticks()
        self.index = 0
        self.frame_times = frame_times

    def check_frame_time(self):
        time_since_last_frame = pygame.time.get_ticks() - self.time_last_frame
        time_to_next_frame = self.time * 1000
        # check if frame_times is not None, otherwise set time_to_next_frame to the given frame time
        if self.frame_times is not None:
            time_to_next_frame = self.frame_times[self.index] * 1000

        return time_since_last_frame > time_to_next_frame

    def get_image(self):

        self.index = (self.index + 1) % 4
        self.time_last_frame = pygame.time.get_ticks()
        print(f'index:{self.index}')
        return self.images[self.index]

    def get_image_at(self, index):
        return self.images[index]