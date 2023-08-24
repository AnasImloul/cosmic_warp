import pygame
from drawable import Drawable
from time import time
from textBox import TextBox


class Counter(TextBox):

    def __init__(self, value, pos, text="", color=(255, 255, 255), size=20, refresh_rate=1):
        super().__init__(text="", pos=pos, color=color, size=size)
        self.value = value
        self.refresh_rate = refresh_rate
        self.last_update = None
        self.prefix = text

    def update(self, value):
        if self.last_update is None:
            self.value = value
            self.last_update = time()

        elif time() - self.last_update > 1 / self.refresh_rate:
            self.value = value
            self.last_update = time()

        self.update_text(text=f'{self.prefix} {round(self.value)}')
