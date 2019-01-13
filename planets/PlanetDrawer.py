from PIL import Image, ImageDraw


class PlanetDrawer:
    def __init__(self, background_color='white', indent=20):
        self.background_color = background_color
        self.indent = indent
        self.width = indent
        self.height = 0

        self._left_bound = indent
        self._planets = []

    def draw_next_planet(self, diameter, color='black'):
        self._planets.append((diameter, color))
        self.width += diameter + self.indent
        self.height = max(self.height, diameter + self.indent * 2)

    def show(self):
        image = Image.new('RGBA', (int(self.width), int(self.height)), self.background_color)
        draw = ImageDraw.Draw(image)
        for planet in self._planets:
            planet_bounds = self._get_planet_bounds(planet[0])
            draw.ellipse(planet_bounds, fill=planet[1])
            self._left_bound = planet_bounds[2] + self.indent
        image.show()
        self._left_bound = self.indent

    def save(self, path='planets.png'):
        image = Image.new('RGBA', (int(self.width), int(self.height)), self.background_color)
        draw = ImageDraw.Draw(image)
        for planet in self._planets:
            planet_bounds = self._get_planet_bounds(planet[0])
            draw.ellipse(planet_bounds, fill=planet[1])
            self._left_bound = planet_bounds[2] + self.indent
        image.save(path)
        self._left_bound = self.indent

    def _get_planet_bounds(self, diameter):
        x1 = self._left_bound
        x2 = x1 + diameter
        y1 = int((self.height - diameter) / 2)
        y2 = y1 + diameter

        return x1, y1, x2, y2
