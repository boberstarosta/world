import logging
import pyglet
from game.map import Map


class GameWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__(width=1200, height=800)
        self.set_caption("World")
        logging.basicConfig(level=logging.DEBUG)
        pyglet.clock.schedule_interval(self.on_update, 1/30)
        self.batch = pyglet.graphics.Batch()
        self.load_content()
        self.map = Map()

    def load_content(self):
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        logging.debug(f"Mouse move at {x, y}")

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
