import itertools
import pyglet
import settings

import logging
logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)

from world import content
from world import graphics
from world import world


class GameWindow(pyglet.window.Window):
    def __init__(self):
        logging.info("Initializing GameWindow")
        super().__init__(width=settings.WIDTH, height=settings.HEIGHT)
        self.set_caption("World")
        graphics.init(self)
        pyglet.clock.schedule_interval(self.on_update, 1/settings.FRAMES_PER_SECOND)
        self.cursor_sprite = pyglet.sprite.Sprite(
            img=content.image("cursor.png"),
            batch=graphics.batch,
            group=graphics.groups["cursor"]
        )
        self.world = world.World()

    def on_mouse_motion(self, x, y, dx, dy):
        coords = world.coords_from_screen(x, y)
        self.cursor_sprite.position = world.position_from_coords(*coords)
        logging.debug(f"Mouse move at {x, y}, coords={coords}")

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        logging.debug(f"Mouse drag buttons {buttons} at {x, y}")

    def on_mouse_press(self, x, y, button, modifiers):
        logging.debug(f"Mouse button {button} press at {x, y}")

    def on_mouse_release(self, x, y, button, modifiers):
        logging.debug(f"Mouse button {button} release at {x, y}")

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        logging.debug(f"Mouse scroll {scroll_y} at {x, y}")

    def on_update(self, dt):
        pass

    def on_draw(self):
        pyglet.gl.glClearColor(*settings.BACKGROUND_COLOR)
        self.clear()
        graphics.batch.draw()


window = GameWindow()
pyglet.app.run()
