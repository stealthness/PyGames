import os

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

def load_images(path):
    """
    Load multiple images
    :param path: List[str]: list of image paths
    :return: List[pygame.Surface]: list of images
    """
    images = []
    for imag_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_img(path + '\\' + imag_name))
        
    return images
