import pyglet
from pyglet import image


window = pyglet.window.Window(width=1280, height=960)

player = image.load("./assets/img/starship.png")

asteroid_big = image.load("./assets/img/Asteroid_Large.png")
asteroid_medium = image.load("./assets/img/Asteroid_Medium.png")
asteroid_small = image.load("./assets/img/Asteroid_Small.png")

@window.event
def on_draw():
    window.clear()
    player.blit(50, 50)
    asteroid_big.blit(100,50)
    asteroid_medium.blit(150,30)
    asteroid_small.blit(50,100)

def update(dt):
    pass


pyglet.clock.schedule_interval(update, 1/60.0)  # update at 60Hz


if __name__ == '__main__':
    pyglet.app.run()
