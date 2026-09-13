import random


class TargetGenerator:

    def __init__(self, screen):
        self.spawn_rate = 2.0
        self.isSpawn = True
        self.time_to_next_spawn = self.spawn_rate
        self.time_from_last_spawn = 0
        self.targets = []
        self.screen = screen

    def update(self, dt:float)->None:
        if not self.isSpawn:
            return

        self.time_from_last_spawn += dt
        if self.time_from_last_spawn > self.time_to_next_spawn:
            self.time_from_last_spawn = 0
            self.spawn_target()

    def spawn_target(self):
        pos_x = random.randint(-4, 4)
        pos_y = 6
        target = Target((pos_x, pos_y))



    def has_started(self):
        return self.isSpawn

    def get_targets(self):
        return self.targets

    def start(self):
        self.isSpawn = True


class Target:

    def __init__(self, pos_x:int, pos_y:int):
        self.pos = (pos_x, pos_y)

    def draw(self):
        pass

    def update(self, dt):
        pass