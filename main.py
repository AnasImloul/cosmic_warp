import pygame
from celestial import Celestial
from universe import Universe
from bufferedCounter import BufferedCounter
from counter import Counter
import sys
from math import sqrt, cos, sin, pi
from random import random, randint, choice


#initialze pygame font

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Solar System")
clock = pygame.time.Clock()
run = True


planet_count = sys.argv[1] if len(sys.argv) > 1 else 2000

center = (screen.get_width() / 2, screen.get_height() / 2)

universe = Universe(size=20000)
fpsCounter = BufferedCounter(text="FPS: ", value=0, pos=(10, 10), color=(255, 255, 255), size=20, refresh_rate=10)
objectCounter = Counter(text="Objects: ", value=0, pos=(10, 40), color=(255, 255, 255), size=20, refresh_rate=10)

max_distance = 600


def random_planet():
    distance = sqrt(randint(0, max_distance ** 2))
    velocity = randint(0, 600)
    angle = random() * 2 * pi
    pos = (center[0] + distance * cos(angle), center[1] + distance * sin(angle))
    velocity = (velocity * cos(angle), velocity * sin(angle))
    radius = choice([1] * 3 + [2])
    color = (randint(0, 192), randint(128, 255), randint(128, 255))
    planet = Celestial(pos=pos, radius=radius, color=color, velocity=velocity)
    return planet

"""
x, y = -y, x
"""

for i in range(int(1)):
    planet = random_planet()
    universe.add_celestial(planet)


offset = (0, 0)

while run:
    clock.tick(1000)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        offset = (offset[0], offset[1] - 2)
    if keys[pygame.K_DOWN]:
        offset = (offset[0], offset[1] + 2)
    if keys[pygame.K_LEFT]:
        offset = (offset[0] - 2, offset[1])
    if keys[pygame.K_RIGHT]:
        offset = (offset[0] + 2, offset[1])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
               run = False

            if event.key == pygame.K_SPACE:
                fpsCounter.show = not fpsCounter.show

            if event.key == pygame.K_t:
                universe.show_trail = not universe.show_trail

    dt = clock.get_time() / 1000

    deleted = []

    universe.update(dt)
    universe.draw(screen, offset=offset)

    fps = clock.get_fps()

    if fps == 0:
        continue

    for i in range(int(2000 / fps)):
        universe.add_celestial(random_planet())

    fpsCounter.update(1 / dt)
    fpsCounter.draw(screen)

    objectCounter.update(len(universe.celestials))
    objectCounter.draw(screen)

    pygame.display.update()
