import pygame
from sheep import Sheep

pygame.init()
print('pygame init ok')
# create a tiny display so convert_alpha() and image operations work
pygame.display.set_mode((1, 1))

s = Sheep((10, 10))
print('isFound:', s.isFound)
print('isSick before:', s.isSick)

s.make_sick()
print('isSick after make_sick:', s.isSick)

print('image exists:', s.image is not None)
print('sick_image exists:', s.sick_image is not None)

# compare a sample pixel (0,0) if sizes allow
try:
    p1 = s.image.get_at((0, 0))
    p2 = s.sick_image.get_at((0, 0)) if s.sick_image is not None else None
    print('pixel sample:', p1, p2, 'equal:', p1 == p2)
except Exception as e:
    print('could not sample pixels:', e)

pygame.quit()

