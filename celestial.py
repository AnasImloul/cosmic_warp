from moveable import Moveable
from drawable import Drawable
from trailable import Trailable
import pygame


class Celestial(Moveable, Drawable, Trailable):
    def __init__(self, pos=None, radius=0, color=(0, 0, 0), velocity=None):
        Moveable.__init__(self, pos, velocity)
        Drawable.__init__(self, pos, (radius, radius), color)
        Trailable.__init__(self, color, max_size=10, refresh_rate=20)
        self.radius = radius

    def update(self, dt, gravity=(0, 0)):
        self.move(dt)
        self.accelerate(gravity, dt)

    def update_trail(self):
        if self.pos is not None:
            self.trail.add_point(self.pos)

    def draw_trail(self, win):
        self.trail.draw(win)

    def __add__(self, other):
        return other

    def __radd__(self, other):
        return other

    def __iadd__(self, other):
        return other

    def __sub__(self, other):
        return other

    def __rsub__(self, other):
        return other

    def __isub__(self, other):
        return other
