import datetime
import random
import os
import math

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (450, 200)

import pygame as pg

pg.init()

scr_width = 960
scr_height = 540

isFullscreen = False

win = pg.display.set_mode((scr_width, scr_height))

pg.display.set_caption("Tigre De Shroedinger")


class Char:
    def __init__(self, pos):
        if pos is not None:
            self.x = pos[0]
            self.y = pos[1]
        else:
            self.x = 100
            self.y = 100

        self.vel = [0, 0]
        self.vel_max = [15, 20]
        self.state = 0
        self.box_coll = (0, 0)
        self.box_states = {-1: (20, 30), 0: (20, 50), 1: (20, 50), 2: (10, 40)}

        # states -1: 'crouch', 0: 'stand', 1: 'jump', 2: 'wallgrab'}

        for state, params in self.box_states.items():
            if self.state == state:
                self.box_coll = params

    def __repr__(self):
        pg.draw.rect(win, (255, 0, 0), (self.x-(self.box_coll[0]/2), self.y-self.box_coll[1], self.box_coll[0], self.box_coll[1]))

    def box_coll_refresh(self):
        for state, params in self.box_states.items():
            if self.state == state:
                self.box_coll = params


    def move(self):
        if (0 + char.box_coll[0] / 2 + math.fabs(char.vel[0])) <= self.x:
            if self.vel[0] < 0:
                self.x += self.vel[0]
        else:
            if char.vel[0] < 0:
                char.x = 0 + char.box_coll[0]/2

        if self. x <= (scr_width - char.box_coll[0]/2 - math.fabs(char.vel[0])):
            if self.vel[0] > 0:
                self.x += self.vel[0]
        else:
            if char.vel[0] > 0:
                char.x = scr_width - char.box_coll[0]/2

        if self.y <= (scr_height + self.vel[1]) and self.state == 1:
            if self.state == 1:
                self.y -= self.vel[1]
                if scr_height > self.y + 10**0.5:
                    self.vel[1] -= 10**0.5
        else:
            self.y = scr_height
            self.vel[1] = 0
            if self.state != -1:
                self.state = 0


char = Char((100, scr_height))


def display_refresh():
    win.fill((0, 0, 0))

    char.__repr__()

    pg.display.update()


run = True


while run:
    pg.time.delay(40)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    char.box_coll_refresh()
    char.move()

    keys = pg.key.get_pressed()

    if keys[pg.K_a]:
        if char.state in [0, 1]:
            if char.vel[0] > -char.vel_max[0]:
                char.vel[0] -= 3
        else:
            char.vel[0] = -5
    elif keys[pg.K_d]:
        if char.state in [0, 1]:
            if char.vel[0] < char.vel_max[0]:
                char.vel[0] += 3
        else:
            char.vel[0] = 5
    else:
        char.vel[0] = 0


    if char.state != 1:
        if keys[pg.K_SPACE]:
            char.state = 1
            char.vel[1] += 30
        elif keys[pg.K_LCTRL]:
            char.state = -1
        else:
            char.state = 0

    display_refresh()

pg.quit()
