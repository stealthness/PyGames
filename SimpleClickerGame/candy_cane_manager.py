from SimpleClickerGame.candy_cane import CandyCane


class CandyCaneManager:
    def __init__(self):
        self.candy_list = []
        for _ in range(4):
            self.candy_list.append(CandyCane())

    def update(self, screen, point):
        for candy in self.candy_list:
            if point is not None and candy.rect.collidepoint(point):
                pass
            else:          
                candy.update()
                candy.draw(screen)
