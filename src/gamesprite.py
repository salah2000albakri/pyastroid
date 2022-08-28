from pyglet import image


class GameSprite:
    def __init__(self, path_to_image: str, x: float, y: float):
        self._img = image.load(path_to_image)
        self.x = x
        self.y = y

    def draw(self):
        self._img.blit(self.x, self.y)

    def update(self, dt):
        pass

