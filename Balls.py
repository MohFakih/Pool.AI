import pygame

BALLSIZE = 5
DRAG_COEFFICIENT = 0.05
SPEED_CUTOFF = 0.001

class Ball:
    def __init__(self, num, pos, vel):
        self.num = num
        self.vel = vel
        self.pos = pos

    def move(self):
        moved = False
        if self.vel[0] != 0:
            self.pos[0] += self.vel[0]
            self.vel[0] *= (1-DRAG_COEFFICIENT)
            if -SPEED_CUTOFF < self.vel[0] and self.vel[0] < SPEED_CUTOFF:  # -0.01<self.vel[0]<0.01 raises errors. Don't simplify
                self.vel[0] = 0
            moved = True
        if self.vel[1] != 0:
            self.pos[1] += self.vel[1]
            self.vel[1] *= (1-DRAG_COEFFICIENT)
            if -SPEED_CUTOFF<self.vel[1] and self.vel[1]<SPEED_CUTOFF: # -0.01<self.vel[1]<0.01 raises errors. Don't simplify
                self.vel[1]=0
            moved = True
        if moved:
            self.check_bounce_walls()

    def check_bounce_walls(self):
        import main
        if self.pos[0] < main.WALLOFFSET+BALLSIZE:
            self.pos[0] = main.WALLOFFSET+BALLSIZE
            self.vel[0] = -1 * self.vel[0]
        elif self.pos[0] > main.width-main.WALLOFFSET-BALLSIZE:
            self.pos[0] = main.width-main.WALLOFFSET-BALLSIZE
            self.vel[0] = -1 * self.vel[0]
        if self.pos[1] < main.WALLOFFSET+BALLSIZE:
            self.pos[1] = main.WALLOFFSET+BALLSIZE
            self.vel[1] = -1 * self.vel[1]
        elif self.pos[1] > main.height-main.WALLOFFSET-BALLSIZE:
            self.pos[1] = main.height-main.WALLOFFSET-BALLSIZE
            self.vel[1] = -1 * self.vel[1]

    def draw(self, screen, color=(0, 0, 0)):
        pygame.draw.circle(screen, color, [int(self.pos[0]), int(self.pos[1])], BALLSIZE)
