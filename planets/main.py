from requests import get
from bs4 import BeautifulSoup
import sys

from PlanetDrawer import PlanetDrawer


class Planet:
    def __init__(self, name, diameter, rings=None):
        self.name = name
        self.diameter = diameter
        self.rings = rings or []


def get_planets():
    planets_data_url = 'http://nssdc.gsfc.nasa.gov/planetary/factsheet/index.html'
    html = get(planets_data_url).text
    soup = BeautifulSoup(html, 'lxml')
    table_rows = soup.findAll('tr')

    planets = []
    moon = None
    for name, diameter in zip(table_rows[0].findAll('td')[1:], table_rows[2].findAll('td')[1:]):
        name = name.text.strip().lower()
        diameter = int(diameter.text.replace(',', ''))
        if name == 'moon':
            moon = Planet(name, diameter)
        else:
            planets.append(Planet(name, diameter))

    return planets, moon


def main():
    planets, moon = get_planets()
    proportion = max(x.diameter for x in planets) / int(sys.argv[1])

    canvas = PlanetDrawer()
    for planet in planets:
        canvas.draw_next_planet(planet.diameter / proportion)
    canvas.show()
    # canvas.save()


if __name__ == '__main__':
    main()
