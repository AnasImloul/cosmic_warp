import pygame
from buffer import Buffer
from time import time
from counter import Counter


class BufferedCounter(Counter):
    def __init__(self, value, pos, text="", color=(255, 255, 255), size=20, refresh_rate=1):
        super().__init__(value=value, text=text, pos=pos, size=size, color=color)
        self.buffer = Buffer(32)

    def update(self, value):
        self.buffer.add(value)
        super().update(self.buffer.average())


