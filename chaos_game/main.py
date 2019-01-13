from datetime import datetime, timedelta
from random import randint, choice
import random

import pygame


class Game:
    TRIANGLE = [
        (350, 0),
        (4, 600),
        (696, 600)
    ]

    RECTANGLE = [
        (50, 50),
        (550, 50),
        (50, 550),
        (550, 550),
    ]

    PENTAGON = [
        (350, 30),
        (93, 217),
        (191, 518),
        (509, 518),
        (607, 217),
    ]

    HEXAGON = [
        (485, 66),
        (215, 66),
        (80, 300),
        (215, 534),
        (485, 534),
        (620, 300)
    ]

    def __init__(self, width=700, height=600, base_points=TRIANGLE):
        self.width = width
        self.height = height

        pygame.init()
        self.screen = pygame.display.set_mode((width, height))

        self.base_points = base_points
        self.current_point = (width/2, height/2)

        self.draw_base_points()

        #self.last_base_point = base_points[0]

    def run(self, wait=True):
        pressed_time = datetime.now()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.current_point = self.update_current_point()
                    self.draw_point(*self.current_point)
                    pressed_time = datetime.now()

            keys = pygame.key.get_pressed()
            if not wait or (wait and keys[pygame.K_SPACE] and self._press_timeout(pressed_time)):
                self.current_point = self.update_current_point()
                self.draw_point(*self.current_point)

            pygame.display.flip()

    @staticmethod
    def _press_timeout(pressed_time, timeout=500):
        return datetime.now() - pressed_time > timedelta(milliseconds=timeout)

    def draw_base_points(self):
        for point in self.base_points:
            self.draw_point(*point, radius=5, color=(0, 255, 255))

    def draw_point(self, x, y, radius=2, color=None):
        if not color:
            r, g, b = 255, 255, 255
            r = r * (x / self.width)
            b = b * (y / self.height)
        else:
            r, g, b = color

        pygame.draw.circle(self.screen, (r, g, b), (int(x), int(y)), radius)

    def update_current_point_(self):
        x, y = self.current_point
        mat = [[0.0, 0.0, 0.0, 0.6, 0.0, 0.0, 0.01],
               [0.85, 0.04, -0.04, 0.85, 0.0, 1.6, 0.85],
               [0.2, -0.26, 0.23, 0.22, 0.0, 1.6, 0.07],
               [-0.15, 0.28, 0.26, 0.24, 0.0, 0.44, 0.07]]
        p = random.random()
        if p <= mat[0][6]:
            i = 0
        elif p <= mat[0][6] + mat[1][6]:
            i = 1
        elif p <= mat[0][6] + mat[1][6] + mat[2][6]:
            i = 2
        else:
            i = 3

        x0 = x * mat[i][0] + y * mat[i][1] + mat[i][4]
        y = x * mat[i][2] + y * mat[i][3] + mat[i][5]
        x = x0

        return x, y

    def update_current_point(self, part=2):
        random_base_point = choice(self.base_points)
        return self.current_point[0] + ((random_base_point[0] - self.current_point[0]) / part), \
               self.current_point[1] + ((random_base_point[1] - self.current_point[1]) / part)


full_hd = (1920, 1080)

phone_full_hd = (1080, 1920)
phone_full_hd_square = [
    (20, 435),
    (1070, 435),
    (20, 1485),
    (1070, 1485),
]

g = Game()
g.run()

pygame.image.save(g.screen, 'image.png')
