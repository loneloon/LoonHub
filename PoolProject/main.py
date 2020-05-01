import os
import datetime
import random
import shapely.geometry
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

top_border = ((67,49), (365, 49))
left_top_border = ((48, 72), (48, 344))
left_bot_border = ((48, 378), (48, 652))
right_top_border = ((384, 72), (384, 344))
right_bot_border = ((384, 378), (384, 652))
bot_border = ((67, 673), (366, 673))

# interaction

mb_idle = (0, 0, 0)
mb_1_pressed = (1, 0, 0)
grab = False




class Ball:
    def __init__(self):
        self.sprite = pygame.image.load('img/ball.png')
        self.x = random.randint(100, 400)
        self.y = random.randint(100, 400)
        self.rad = 13
        self.vector = (random.randint(2, 4), 0, random.randint(2, 4))
        self.collision = False
        self.time_sync = datetime.datetime.now()
        self.inapocket = False

    def draw(self):
        win.blit(self.sprite, (self.x-self.rad, self.y-self.rad))

    def move(self):
        # top/bottom border events
        if not self.inapocket:
            if self.y >= (top_border[0][1] +self.rad) and self.y <= (bot_border[0][1] - self.rad):
                if (self.y > top_border[0][1] and self.y < left_top_border[0][1]) or (self.y > left_top_border[1][1] and self.y < left_bot_border[0][1]) or (self.y > left_bot_border[1][1] and self.y < bot_border[0][1]):
                    if (self.x < (left_top_border[0][0] + self.rad)) or (self.x > (right_top_border[0][0] - self.rad)):
                        self.inapocket = True
                    else:
                        self.x += self.vector[0]
                        self.y += self.vector[0] * self.vector[1] + self.vector[2]
                elif self.x >= (left_top_border[0][0] + self.rad) and self.x <= (right_top_border[0][0] - self.rad):
                    self.x += self.vector[0]
                    self.y += self.vector[0]*self.vector[1] + self.vector[2]
                else:
                    if self.y > left_top_border[0][1] and self.y < left_top_border[1][1]:
                        if self.x - self.rad < (left_top_border[0][0]):
                            self.x = left_top_border[0][0] + self.rad
                        if self.x + self.rad >= right_top_border[0][0]:
                            self.x = right_top_border[0][0] - self.rad
                        self.vector = (self.vector[0]*(-0.8), self.vector[1], self.vector[2]*0.8)
                    elif self.y > left_bot_border[0][1] and self.y < left_bot_border[1][1]:
                        if self.x - self.rad < (left_top_border[0][0]):
                            self.x = left_top_border[0][0] + self.rad
                        if self.x + self.rad >= right_top_border[0][0]:
                            self.x = right_top_border[0][0] - self.rad
                        self.vector = (self.vector[0]*(-0.8), self.vector[1], self.vector[2]*0.8)
            else:
                if self.y < (top_border[0][1] + self.rad):
                    self.y = top_border[0][1] + self.rad
                if self.y > (bot_border[0][1] - self.rad):
                    self.y = bot_border[0][1] - self.rad
                self.vector = (self.vector[0]*(0.8), -(self.vector[1]), self.vector[2]*(-0.8))
        # ball slowing down

            if (datetime.datetime.now() - self.time_sync).seconds > 1:
                self.time_sync = datetime.datetime.now()
                self.vector = ((self.vector[0] * 0.7), self.vector[1], (self.vector[2] * 0.7))
                if (self.vector[0] > -0.1 and self.vector[0] < 0.1):
                    self.vector = (0, self.vector[1], self.vector[2])
                    self.vector = (self.vector[0], self.vector[1], 0)

balls = []
public_vectors = []
ball_circles = []

for n in range(3):
    balls.append(Ball())
    public_vectors.append(balls[n].vector)
    ball_circles.append((balls[n].x - balls[n].rad, balls[n].x + balls[n].rad, balls[n].y - balls[n].rad, balls[n].y + balls[n].rad))



def redrawScreen():
    win.blit(bg, (0, 0))

    for ball in balls:
        if not ball.inapocket:
            ball.draw()


    pygame.display.update()


run = True

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    for idx, ball in enumerate(balls):
        if not ball.inapocket:
            public_vectors[idx] = ball.vector
            ball_circles[idx] = (ball.x - ball.rad, ball.x + ball.rad, ball.y - ball.rad, ball.y + ball.rad)
            ball.move()


    redrawScreen()

pygame.quit()