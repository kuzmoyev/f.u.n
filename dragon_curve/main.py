#!/usr/bin/python3.6

from math import sqrt
from random import randint

import pygame


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

    def euclid(self, p):
        return sqrt((p.x - self.x) ** 2 + (p.y - self.y) ** 2)

    def rotated(self, cosY, sinY):
        x = self.x * cosY - self.y * sinY
        y = self.x * sinY + self.y * cosY
        return Point(x, y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'({self.x}, {self.y})'


class Line:
    def __init__(self, a, b, color=None):
        self.a = a
        self.b = b
        self.color = [int(c) for c in color] or (255, 255, 255)

    def generate(self, iteration):
        A, B = self.a, self.b
        AB = A.euclid(B)
        sinY = (A.y - B.y) / AB
        cosY = (A.x - B.x) / AB
        C_ = Point(AB / 2, AB / 2)
        C = B + C_.rotated(cosY, sinY)

        colorA = (c + 256 / (2 ** iteration) for c in self.color)
        colorB = (c - 256 / (2 ** iteration) for c in self.color)

        return Line(A, C, colorA), Line(B, C, colorB)

    def __str__(self):
        return f'Line(A={self.a} B={self.b})'

    def __repr__(self):
        return self.__str__()


class Game:
    def __init__(self, width=700, height=700):
        self.width = width
        self.height = height

        pygame.init()
        self.screen = pygame.display.set_mode((width, height))

        # a = Point(600, height / 2 + 161)
        # b = Point(width - (2300 - width), height / 2 + 161)

        a = Point(200, 300)
        b = Point(600, 300)

        self.lines = [Line(a, b, (128, 128, 128))]
        self.iteration = 1

    def generate(self):
        new_lines = []
        self.iteration += 1
        for line in self.lines:
            new_lines.extend(line.generate(self.iteration))
        self.lines = new_lines
        print(len(self.lines))

    def update(self):
        pass

    def draw(self):
        # self.screen.fill((0, 0, 0))
        for line in self.lines:
            r, g, b = line.color
            x, y = line.a.get_coords()
            r = r * (x / self.width)
            g = g * (y / self.height)
            pygame.draw.line(self.screen, (r, g, b), line.a.get_coords(), line.b.get_coords(), 2)
        pygame.display.flip()


full_hd = (1920, 1080)

g = Game(800, 600)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                g.generate()
            if event.key == pygame.K_s:
                pygame.image.save(g.screen, f'curve{g.iteration}.png')
    g.update()
    g.draw()
