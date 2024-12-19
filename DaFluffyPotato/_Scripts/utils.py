import pygame

BASE_IMG_PATH = 'data\\Art\\'


def load_img(path):
    """
    Load an image from the BASE_IMG_PATH
    :param path: str: location of the image
    :return: pygame.Surface: the image
    """
    print(BASE_IMG_PATH + path)
    return pygame.image.load(BASE_IMG_PATH + path).convert_alpha()
