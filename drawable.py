import pygame


class Drawable:
    def __init__(self, pos, size, color):
        self.pos = [pos[0], pos[1]]
        self.size = size
        self.color = color

    @property
    def x(self):
        return self.pos[0]

    @property
    def y(self):
        return self.pos[1]

    @property
    def width(self):
        return self.size[0]

    @property
    def height(self):
        return self.size[1]

    def draw(self, win, offset):
        x, y = self.pos

        pos = (x + offset[0], y + offset[1])
        size = self.size

        pygame.draw.rect(win, self.color, pygame.Rect(pos, size))


    def __lt__(self, other):
        return self.y < other.y
