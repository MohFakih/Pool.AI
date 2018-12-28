import pygame, math, numpy as np

BALLSIZE = 6
DRAG_COEFFICIENT = 0.02
SPEED_CUTOFF = 0.001
BallDict = {}
class Ball:
    def __init__(self, num, pos, vel):
        self.num = num
        self.vel = vel
        self.pos = pos
        BallDict[num] = self


    def nextPos(self):
        return [self.pos[0]+self.vel[0], self.pos[1]+self.vel[1]]

    def move(self):
        moved = False

        # Move before applying drag
        self.pos[1] += self.vel[1]
        self.pos[0] += self.vel[0]

        # Apply Drag
        # TODO: check why simplified comparisons raise errors
        if self.vel[0] != 0:
            self.vel[0] *= (1-DRAG_COEFFICIENT)
            if -SPEED_CUTOFF < self.vel[0] and self.vel[0] < SPEED_CUTOFF:  # -SPEED_CUTOFF<self.vel[0]<SPEED_CUTOFF raises errors. Don't simplify
                self.vel[0] = 0
            moved = True
        if self.vel[1] != 0:
            self.vel[1] *= (1-DRAG_COEFFICIENT)
            if -SPEED_CUTOFF<self.vel[1] and self.vel[1]<SPEED_CUTOFF: # -SPEED_CUTOFF<self.vel[1]<SPEED_CUTOFF raises errors. Don't simplify
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

def check_all_collisions():
    for ball in BallDict.values():


def check_collision(Ball1, Ball2): # VERY INEFFICIENT
    A = Ball1.pos
    B = Ball2.pos
    VelA = -Ball1.vel
    VelB = Ball2.vel
    GT = np.linalg.solve([VelA, VelB], A-B)
    print(GT)


def collide(Ball1, Ball2):
    t = Ball1.vel
    Ball1.vel = Ball2.vel
    Ball2.vel = t
