import numpy as np
from math import sqrt
import pygame
class Ball(object):
    def __init__(self, r=1, pos=(0, 0), vel=(0, 0), color=(0, 255, 0)):
        self.r = r
        self.pos = np.array(pos)
        self.vel = np.array(vel)
        self.color = color

    def update(self, size):
        self.pos += self.vel
        self.bounce(size)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.r)

    def bounce(self, size):
        if self.pos[0] < self.r:
            self.pos[0] = self.r
            self.vel[0] *= -1
        elif self.pos[0] >= size[0]-self.r:
            self.pos[0] = size[0]-self.r-1
            self.vel[0] *= -1
        if self.pos[1] < self.r:
            self.pos[1] = self.r
            self.vel[1] *= -1
        elif self.pos[1] >= size[1]-self.r:
            self.pos[1] = size[1]-self.r-1
            self.vel[1] *= -1
def checkCollision(B1, B2):
    assert type(B1) == Ball, "Invalid arg, Ball1 not a ball"
    assert type(B2) == Ball, "Invalid arg, Ball2 not a ball"
    DeltaPos = B1.pos - B2.pos
    DeltaV = B1.vel - B2.vel
    DeltaR = B1.r + B2.r
    a = np.dot(DeltaV, DeltaV)
    b = 2*np.dot(DeltaV, DeltaPos)
    c = np.dot(DeltaPos, DeltaPos)-DeltaR**2
    D = b**2 - 4*a*c
    if D >= 0:
        t1 = (-b-sqrt(D))/2
        t2 = (-b+sqrt(D))/2
        if 0 <= t1 <= 1:
            return t1
        elif 0 <= t2 <= 1:
            return t2
    return -1
