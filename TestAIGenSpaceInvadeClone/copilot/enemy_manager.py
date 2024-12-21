import pygame


class EnemyManager:
    def __init__(self):
        self.rows = 5
        self.cols = 10
        self.initial_speed = 0.3
        self.speed_increment = 0.1
        self.current_speed = self.initial_speed
        self.direction = 1
        self.drop_rate = 8
        self.reset()

    def reset(self):
        self.x = [50 + col * 70 for row in range(self.rows) for col in range(self.cols)]
        self.y = [50 + row * 50 for row in range(self.rows) for col in range(self.cols)]
        self.change_x = [self.initial_speed * self.direction for _ in range(self.rows * self.cols)]
        self.active = [True] * (self.rows * self.cols)
        self.current_speed = self.initial_speed

    def update(self, bullet, player):
        active_enemy_count = 0
        reverse_direction = False

        for i in range(len(self.x)):
            if self.active[i]:
                active_enemy_count += 1
                self.x[i] += self.change_x[i] * self.direction

                if self.x[i] <= 0 or self.x[i] >= 736:
                    reverse_direction = True

                if bullet.is_collision(self.x[i], self.y[i]):
                    bullet.reset()
                    self.active[i] = False

                if player.is_collision(self.x[i], self.y[i]):
                    player.game_over = True

        if reverse_direction:
            self.direction *= -1
            for j in range(len(self.y)):
                self.y[j] += self.drop_rate

        if active_enemy_count < len(self.x):
            self.current_speed = self.initial_speed + (len(self.x) - active_enemy_count) * self.speed_increment
            for i in range(len(self.change_x)):
                self.change_x[i] = self.current_speed

    def draw(self, screen):
        for i in range(len(self.x)):
            if self.active[i]:
                screen.blit(pygame.image.load("../Art/enemy.png"), (self.x[i], self.y[i]))

    def all_inactive(self):
        return all(not active for active in self.active)
