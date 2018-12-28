import pygame, sys, Balls
pygame.init()
size = width, height = 640, 320
screen = pygame.display.set_mode(size)

WALLOFFSET = 20
running = True

test_ball = Balls.Ball(8, [int(width/2), int(height/2)], [3, 3])
test_ball2 = Balls.Ball(7, [50, 50], [-4, -4])
frames = 0
Clock = pygame.time.Clock()
while running:
    Clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)

    pygame.draw.rect(screen, (0, 255, 0), [0, 0, width, height])

    pygame.draw.rect(screen, (255, 255, 255), [int(width/4), 0, 1, height])
    pygame.draw.circle(screen, (255, 255, 255), [int(width/4), int(height/2)], 2)

    pygame.draw.rect(screen, (102, 51, 0), [0, 0, width, WALLOFFSET])
    pygame.draw.rect(screen, (102, 51, 0), [0, 0, WALLOFFSET, height])
    pygame.draw.rect(screen, (102, 51, 0), [0, height - 20, width, WALLOFFSET])
    pygame.draw.rect(screen, (102, 51, 0), [width - WALLOFFSET, 0, WALLOFFSET, height])

    pygame.draw.circle(screen, (0, 0, 0), (WALLOFFSET, WALLOFFSET), 10)
    pygame.draw.circle(screen, (0, 0, 0), (int(width / 2), WALLOFFSET), 10)
    pygame.draw.circle(screen, (0, 0, 0), (width - WALLOFFSET, WALLOFFSET), 10)
    pygame.draw.circle(screen, (0, 0, 0), (WALLOFFSET, height - WALLOFFSET), 10)
    pygame.draw.circle(screen, (0, 0, 0), (int(width / 2), height - WALLOFFSET), 10)
    pygame.draw.circle(screen, (0, 0, 0), (width - WALLOFFSET, height - WALLOFFSET), 10)


    for ball in Balls.BallDict.values():
        ball.move()
        ball.draw(screen)
    pygame.display.flip()

