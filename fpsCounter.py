import pygame
from drawable import Drawable
from time import time
from bufferedCounter import BufferedCounter


class FPSCounter(BufferedCounter):
    buffer_size = 32

    def __init__(self, pos, color=(255, 255, 255), size=20, refresh_rate=1):
        super().__init__(value=0, text="FPS: ", pos=pos, size=size, color=color, refresh_rate=refresh_rate)
