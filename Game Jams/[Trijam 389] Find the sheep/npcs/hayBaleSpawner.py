from npcs.hayBale import HayBale


class HayBaleSpawner:
    def __init__(self, images, position_provider):
        self.images = images
        self.position_provider = position_provider

    def spawn(self, level: int) -> list:
        hay_bales = []
        for _ in range(level):
            hay_bales.append(HayBale(self.position_provider(), self.images.get_hay_bale_image()))
        return hay_bales
