
class ShotGun:
    def __init__(self, max_bullets=6):
        self.max_bullets = max_bullets
        self.bullets = max_bullets

    def get_bullets_text(self):
        return f"Bullets: {self.bullets}"
