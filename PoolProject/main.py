import os
import datetime
import random
import shapely.geometry

pause = False

# system tweaks

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (650, 200)

import pygame

# screen

pygame.init()

scr_width = 434
scr_height = 723

win = pygame.display.set_mode((scr_width, scr_height))

pygame.display.set_caption("Pool Sim.")

# graphics

bg = pygame.image.load("img/table.png")

# world

top_border = ((67, 49), (365, 49))
left_top_border = ((48, 72), (48, 344))
left_bot_border = ((48, 378), (48, 652))
right_top_border = ((384, 72), (384, 344))
right_bot_border = ((384, 378), (384, 652))
bot_border = ((67, 673), (366, 673))

# interaction

mb_idle = (0, 0, 0)
mb_1_pressed = (1, 0, 0)
grab = False


def drawtext(message: str, pos: tuple, color=None, size=None):
    if size is None:
        size = 16

    if color is None:
        color = (0, 0, 0)

    font = pygame.font.SysFont('freesansbold.ttf', size)

    text = font.render(message, True, color)
    win.blit(text, pos)


class Ball:
    def __init__(self):
        self.sprite = pygame.image.load('img/ball.png')
        self.sprite2 = pygame.image.load('img/ball_red.png')
        self.x = random.randint(100, 400)
        self.y = random.randint(100, 400)
        self.rad = 13
        self.vector = (random.randint(-4, 4), (random.randint(0, 2)), 0)
        self.collision = False
        self.time_sync = datetime.datetime.now()
        self.inapocket = False

    def draw(self):
        if not self.collision:
            win.blit(self.sprite, (self.x - self.rad, self.y - self.rad))
        else:
            win.blit(self.sprite2, (self.x - self.rad, self.y - self.rad))

    def move(self):
        # top/bottom border events
        if not self.inapocket:
            if self.y >= (top_border[0][1] + self.rad) and self.y <= (bot_border[0][1] - self.rad):
                if (self.y > top_border[0][1] and self.y < left_top_border[0][1]) or (
                        self.y > left_top_border[1][1] and self.y < left_bot_border[0][1]) or (
                        self.y > left_bot_border[1][1] and self.y < bot_border[0][1]):
                    if (self.x < (left_top_border[0][0] + self.rad)) or (
                            self.x > (right_top_border[0][0] - self.rad)):
                        self.inapocket = True
                    else:
                        self.x += self.vector[0]
                        self.y += self.vector[0] * self.vector[1] + self.vector[2]
                elif self.x >= (left_top_border[0][0] + self.rad) and self.x <= (right_top_border[0][0] - self.rad):
                    self.x += self.vector[0]
                    self.y += self.vector[0] * self.vector[1] + self.vector[2]
                else:
                    if self.y > left_top_border[0][1] and self.y < left_top_border[1][1]:
                        if self.x - self.rad < (left_top_border[0][0]):
                            self.x = left_top_border[0][0] + self.rad
                        if self.x + self.rad >= right_top_border[0][0]:
                            self.x = right_top_border[0][0] - self.rad
                        self.vector = (self.vector[0] * (-0.8), -self.vector[1], 0)
                    elif self.y > left_bot_border[0][1] and self.y < left_bot_border[1][1]:
                        if self.x - self.rad < (left_top_border[0][0]):
                            self.x = left_top_border[0][0] + self.rad
                        if self.x + self.rad >= right_top_border[0][0]:
                            self.x = right_top_border[0][0] - self.rad
                        self.vector = (self.vector[0] * (-0.8), -self.vector[1], 0)
            else:
                if self.y < (top_border[0][1] + self.rad):
                    self.y = top_border[0][1] + self.rad
                if self.y > (bot_border[0][1] - self.rad):
                    self.y = bot_border[0][1] - self.rad
                self.vector = (self.vector[0] * (0.8), -(self.vector[1]), 0)
            # ball slowing down

            if (datetime.datetime.now() - self.time_sync).seconds > 1:
                self.time_sync = datetime.datetime.now()
                self.vector = ((self.vector[0] * 0.7), self.vector[1], 0)
                if (self.vector[0] > -0.1 and self.vector[0] < 0.1):
                    self.vector = (0, self.vector[1], self.vector[2])
                    self.vector = (self.vector[0], self.vector[1], 0)


balls = []
public_vectors = []
ball_pos = []
all_dist = []


for n in range(5):
    balls.append(Ball())
    public_vectors.append(balls[n].vector)
    ball_pos.append((balls[n].x, balls[n].y))


def check_collision():
    global all_dist

    for idx1, ball in enumerate(balls):
        temp = []

        for idx in range(len(balls)):
            if idx1 != idx:
                dist = ((ball.x - balls[idx].x) ** 2 + (ball.y - balls[idx].y) ** 2) ** (0.5)
                temp.append(dist)
            else:
                temp.append('#')

        all_dist.append(temp)

    for idx, i in enumerate(all_dist):
        coll_count = 0
        for idx2, j in enumerate(i):
            if type(j) != str:
                if j < 26:
                    coll_count += 1
                    balls[idx].collision = True
                    balls[idx2].collision = True
        if coll_count == 0:
            balls[idx].collision = False

    all_dist = []



def redrawScreen():
    win.blit(bg, (0, 0))

    for idx, ball in enumerate(balls):
        if not ball.inapocket:
            ball.draw()
            drawtext(str(idx), (ball.x - 3, ball.y - 5))

    if pause:
        drawtext('PAUSE', (180, 330), size=40, color=(255, 255, 255))

    pygame.display.update()


run = True

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            counter = 100

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        pygame.time.delay(100)
        if not pause:
            pause = True
        else:
            pause = False


    if not pause:
        moving = 0
        for idx, ball in enumerate(balls):
            if not ball.inapocket:
                public_vectors[idx] = ball.vector
                ball_pos[idx] = (ball.x, ball.y)
                check_collision()
                ball.move()

                if ball.vector[0] != 0 or ball.vector[2] != 0:
                    moving += 1

        if moving == 0:
            run = False

    redrawScreen()

pygame.quit()