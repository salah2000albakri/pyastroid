import pyglet
from pyglet import image


window = pyglet.window.Window(width=1280, height=960)

player = image.load("./assets/img/starship.png")


@window.event
def on_draw():
    window.clear()
    player.blit(50, 50)


def update(dt):
    pass


pyglet.clock.schedule_interval(update, 1/60.0)  # update at 60Hz


if __name__ == '__main__':
    pyglet.app.run()
