import pygame
from drawable import Drawable


class TextBox(Drawable):

    def __init__(self, text, pos, color=(255, 255, 255), size=20):
        super().__init__(pos=pos, size=size, color=color)
        self.font = pygame.font.SysFont('Comic Sans MS', size)
        self.text = text
        self.textbox = self.font.render(text, False, color)
        self.show = True

    def draw(self, win, offset=(0, 0)):
        if not self.show:
            return

        win.blit(self.textbox, tuple(self.pos))

    def update_text(self, text):
        self.text = text
        self.textbox = self.font.render(f'{self.text}', False, tuple(self.color))

