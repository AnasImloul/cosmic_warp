from buffer import Buffer


class Universe:
    color = (0, 0, 0)

    def __init__(self, color=(0, 0, 0), size=2000):
        self.color = color
        self.celestials = Buffer(size)
        self.show_trail = False

    def add_celestial(self, celestial):
        self.celestials.add(celestial)

    def update(self, dt):
        for celestial in self.celestials:
            celestial.update(dt)
            if self.show_trail:
                celestial.update_trail()

    def draw(self, surface, offset):
        surface.fill(self.color)

        for celestial in self.celestials:
            if self.show_trail:
                celestial.draw_trail(surface)

        for celestial in self.celestials:
            celestial.draw(surface, offset)

    def clear_trails(self):
        for planet in self.planets:
            planet.clear_trail()