from src.gamesprite import GameSprite


class Asteroid(GameSprite):
    def __init__(self, path_to_image: str, x: float, y: float):
        super().__init__(path_to_image, x, y)
        self.speed = (12, -12)

    def update(self, dt):
        self.x =self.x + self.speed[0]*dt
        self.y =self.y + self.speed[1]*dt
