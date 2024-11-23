class GameObject:

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.active = True

    def move(self, dx, dy):

        if self.active:
            self.x += dx
            self.y += dy

    def Update(self) -> bool:
        if not self.active:
            return False
        self.move(self.dx, self.dy)
        return True

    def __str__(self):
        return f'{self.name} at {self.x},{self.y}'


