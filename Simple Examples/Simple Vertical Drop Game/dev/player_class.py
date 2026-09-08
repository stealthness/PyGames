import pygame

class Player:
    def __init__(self, x, y, width=50, height=50):
        self.rect = pygame.Rect(x, y, width, height)

        self.speed = 300

        self.fill_color = (80, 180, 255)
        self.outline_color = (255, 255, 255)

    def handle_input(self):
        keys = pygame.key.get_pressed()

        movement = pygame.Vector2()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            movement.x -= 1

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            movement.x += 1

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            movement.y -= 1

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            movement.y += 1

        # Prevent diagonal movement from being faster.
        if movement.length_squared() > 0:
            movement = movement.normalize()

        return movement

    def update(self, dt, screen_rect):
        movement = self.handle_input()

        self.rect.x += int(movement.x * self.speed * dt)
        self.rect.y += int(movement.y * self.speed * dt)

        # Keep the player inside the screen.
        self.rect.clamp_ip(screen_rect)

    def draw(self, surface):
        pygame.draw.rect(
            surface,
            self.fill_color,
            self.rect,
        )

        pygame.draw.rect(
            surface,
            self.outline_color,
            self.rect,
            width=2,
        )