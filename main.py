import pyglet

from src.gamesprite import GameSprite

window = pyglet.window.Window(width=1280, height=960)

player = GameSprite("./assets/img/starship.png", 50, 50)

asteroid_big = GameSprite("./assets/img/Asteroid_Large.png", 100,50)
asteroid_medium = GameSprite("./assets/img/Asteroid_Medium.png", 150,30)
asteroid_small = GameSprite("./assets/img/Asteroid_Small.png", 50,100)

entity_list = [player, asteroid_small, asteroid_medium, asteroid_big]


@window.event
def on_draw():
    window.clear()
    for entity in entity_list:
        entity.draw()


def update(dt):
    for entity in entity_list:
        entity.update()


pyglet.clock.schedule_interval(update, 1/60.0)  # update at 60Hz


if __name__ == '__main__':
    pyglet.app.run()
