import itertools
import logging
import pyglet
import settings


logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)


class GameWindow(pyglet.window.Window):
    def __init__(self):
        logging.info("Initializing GameWindow")
        super().__init__(width=settings.width, height=settings.height)
        self.set_caption("World")
        pyglet.clock.schedule_interval(self.on_update, 1/settings.frames_per_second)
        self.batch = pyglet.graphics.Batch()
        self.content = self.load_content()
        self.layers = self.setup_layers()
        self.cursor_sprite = pyglet.sprite.Sprite(
            img=self.content["cursor"],
            batch=self.batch,
            group=self.layers["cursor"]
        )

    def load_content(self):
        logging.info(f"Loading content")
        pyglet.resource.path = ["content"]
        pyglet.resource.reindex()
        return {
            "cursor": pyglet.resource.image("cursor.png")
        }

    def setup_layers(self):
        order = itertools.count()
        return {
            "cursor": pyglet.graphics.OrderedGroup(next(order))
        }

    def on_mouse_motion(self, x, y, dx, dy):
        logging.debug(f"Mouse move at {x, y}")
        self.cursor_sprite.position = (x, y)

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
        self.clear()
        self.batch.draw()


window = GameWindow()
pyglet.app.run()
