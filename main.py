from ball import Ball, checkCollision
import pygame
import sys

pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
b1 = Ball(10, (width//2 - 10, height//2), (1, 0))
b2 = Ball(20, (width//2 + 10, height//2), (-1, 0))
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(1)
    pygame.draw.rect(screen, (255, 0, 0), [0, 0, width, height])
    b1.update(size)
    b2.update(size)
    b1.draw(screen)
    b2.draw(screen)
    u = checkCollision(b1, b2)
    if u!=-1:
        print(b1.pos, b1.vel, b2.pos, b2.vel, u)
    pygame.display.flip()