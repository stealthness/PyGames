from config import BACKGROUND_RECYCLE_THRESHOLD, BACKGROUND_SCROLL_SPEED, GAME_BACKGROUNDS

class BackgroundController:
    """
    The background controller moves the backgrounds of the game, At the start first background will be active
    one in the center, and one each to the left and right. When the player moves the background will move to the left
    When right most screen has move 100 pixel in to the screen, the left is removed and the next back ground in the list is
    added at the end to the right, when the backgrounds list reaches the end of its list it starts from the from
    beginning again.
    """

    def __init__(self):
        self.backgrounds = GAME_BACKGROUNDS
        if not self.backgrounds:
            raise ValueError("GAME_BACKGROUNDS must contain at least one surface")

        self.scroll_speed = BACKGROUND_SCROLL_SPEED
        self.recycle_threshold = BACKGROUND_RECYCLE_THRESHOLD
        self.background_width = self.backgrounds[0].get_width()

        # Start with three tiles: left, center, right.
        self.active_tiles = [
            [self.backgrounds[0], -self.background_width],
            [self.backgrounds[1], 0],
            [self.backgrounds[2], self.background_width]
        ]
        self.next_background_index = 1 % len(self.backgrounds)

    def _get_next_background(self):
        background = self.backgrounds[self.next_background_index]
        self.next_background_index = (self.next_background_index + 1) % len(self.backgrounds)
        return background

    def draw(self, screen):
        for background, x_position in self.active_tiles:
            screen.blit(background, (int(x_position), 0))

    def update(self):
        for tile in self.active_tiles:
            tile[1] -= self.scroll_speed

        # Add a new tile once the right-most tile has moved far enough left.
        right_most_x = self.active_tiles[-1][1]
        if right_most_x <= self.background_width - self.recycle_threshold:
            new_background = self._get_next_background()
            new_x = right_most_x + self.background_width
            self.active_tiles.append([new_background, new_x])

        # Drop old left tiles that are well outside the visible area.
        while len(self.active_tiles) > 3 and self.active_tiles[0][1] <= -self.background_width - self.recycle_threshold:
            self.active_tiles.pop(0)
