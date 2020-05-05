import datetime
import math
import random
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (500, 200)

import pygame

pygame.init()

scr_width = 1000
scr_height = 400

win = pygame.display.set_mode((scr_width, scr_height))

pygame.display.set_caption("The Search")

run = True

bg = pygame.image.load("img/back.png")

time_sync = datetime.datetime.now()

def drawtext(message: str, pos: tuple, color=None, custom=None, size=None):
    if size is None:
        size = 8

    if color is None:
        color = (0, 0, 0)

    font = pygame.font.SysFont('freesansbold.ttf', 22)


    text = font.render(message, True, color)
    win.blit(text, pos)


class Hero:

    def __init__(self):
        self.x = 400
        self.y = 140

        self.images = [pygame.image.load(f"img/player/{i+1}.png") for i in range(10)]
        self.frame = 0
        self.frame_pass = 0

        self.left = False

        self.cool = 0

    def draw(self):
        if self.frame == 0:
            if self.frame_pass < 100:
                self.frame_pass += 1
            else:
                self.frame += 1
                self.frame_pass = 0
        else:
            if self.frame_pass < 1:
                self.frame_pass += 1
            else:
                if self.frame < 9:
                    self.frame += 1
                else:
                    self.frame = 0
                self.frame_pass = 0




        if self.left:
            temp = pygame.transform.flip(self.images[self.frame], True, False)
            jacket = pygame.transform.flip(pygame.image.load(f"img/player/cool_jacket.png"), True, False)
        else:
            temp = self.images[self.frame]
            jacket = pygame.image.load(f"img/player/cool_jacket.png")

        win.blit(temp, (self.x, self.y))

        if self.cool:
            win.blit(jacket, (self.x, self.y))


shiro = Hero()


class Civ:
    def __init__(self):
        self.x = random.randint(20, 800)
        self.y = 140

        self.fan = random.choice([True, False])

        if self.fan:
            self.images = [pygame.image.load(f"img/fan/{i + 1}.png") for i in range(10)]
        else:
            self.images = [pygame.image.load(f"img/civ/{i + 1}.png") for i in range(10)]
        self.scared_im = [pygame.image.load(f"img/civ/scared/{i + 1}.png") for i in range(10)]
        self.frame = 0
        self.frame_pass = random.randint(40, 80)

        self.left = True
        self.scared = False

        self.speed = random.uniform(0.5, 2)



    def draw(self):
        if self.frame == 0:
            if self.frame_pass < 100:
                self.frame_pass += 1
            else:
                self.frame += 1
                self.frame_pass = 0
        else:
            if self.frame_pass < 1:
                self.frame_pass += 1
            else:
                if self.frame < 9:
                    self.frame += 1
                else:
                    self.frame = 0
                self.frame_pass = 0

        if not self.scared:
            images = self.images[self.frame]
        else:
            images = self.scared_im[self.frame]

        if self.left:
            temp = pygame.transform.flip(images, True, False)
        else:
            temp = images

        win.blit(temp, (self.x, self.y))


class Button:
    def __init__(self, purpose):
        self.y = 5
        self.active = True

        self.purpose = purpose
        if self.purpose == 'cool':
            self.x = 700
        elif self.purpose == 'shuff':
            self.x = 840
        else:
            self.x = 700

        self.cool_unpressed = pygame.transform.scale(pygame.image.load("img/cool.png"), (130, 50))
        self.cool_pressed = pygame.transform.scale(pygame.image.load("img/cool.png"), (130, 40))

        self.regular_unpressed = pygame.transform.scale(pygame.image.load("img/regular.png"), (130, 50))
        self.regular_pressed = pygame.transform.scale(pygame.image.load("img/regular.png"), (130, 40))

        self.shuffle_unpressed = pygame.transform.scale(pygame.image.load("img/shuffle2.png"), (130, 50))
        self.shuffle_pressed = pygame.transform.scale(pygame.image.load("img/shuffle2.png"), (130, 40))

        self.sprites = [self.cool_unpressed, self.cool_pressed, self.regular_unpressed, self.regular_pressed, self.shuffle_unpressed, self.shuffle_pressed]


    def draw(self):
        if self.purpose == 'cool':
            if self.active and shiro.cool == 0:
                win.blit(self.sprites[2], (self.x, self.y))
            elif not self.active and shiro.cool == 0:
                win.blit(self.sprites[3], (self.x, self.y+10))
            elif self.active and shiro.cool > 0:
                win.blit(self.sprites[0], (self.x, self.y))
            elif not self.active and shiro.cool > 0:
                win.blit(self.sprites[1], (self.x, self.y+10))

        if self.purpose == 'shuff':
            if self.active:
                win.blit(self.sprites[4], (self.x, self.y))
            elif not self.active:
                win.blit(self.sprites[5], (self.x, self.y+10))

cool = Button('cool')

shuffle = Button('shuff')

people = []

for i in range(random.randint(1,4)):
    people.append(Civ())

def display_refresh():
    win.blit(bg, (0, 0))

    shiro.draw()

    for citizen in people:
        citizen.draw()

    cool.draw()
    shuffle.draw()

    pygame.display.update()


while run:

    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        shiro.x += 2
        shiro.left = False
    elif keys[pygame.K_a]:
        shiro.x -= 2
        shiro.left = True

    if pygame.mouse.get_pressed() == (1, 0, 0) and (cool.x < pygame.mouse.get_pos()[0] < (cool.x + 130)) and (cool.y < pygame.mouse.get_pos()[1] < (cool.y + 50)):
        pygame.time.delay(100)
        time_sync = datetime.datetime.now()
        if cool.active:
            cool.active = False
            if shiro.cool == 0:
                shiro.cool = 1
            else:
                shiro.cool = 0

    if pygame.mouse.get_pressed() != (1, 0, 0) and not cool.active and (datetime.datetime.now() - time_sync).microseconds > 100000:
        cool.active = True

    if pygame.mouse.get_pressed() == (1, 0, 0) and (shuffle.x < pygame.mouse.get_pos()[0] < (shuffle.x + 130)) and (shuffle.y < pygame.mouse.get_pos()[1] < (shuffle.y + 50)):
        pygame.time.delay(100)
        time_sync = datetime.datetime.now()
        if shuffle.active:
            shuffle.active = False
            people = []

            for i in range(random.randint(1, 4)):
                people.append(Civ())

    if pygame.mouse.get_pressed() != (1, 0, 0) and not shuffle.active and (datetime.datetime.now() - time_sync).microseconds > 200000:
        shuffle.active = True

    scared_ppl_counter = 0

    fans = 0

    if shiro.cool > 0:
        for citizen in people:
            if not citizen.fan:
                if math.fabs(citizen.x - shiro.x) < 180:
                    if citizen.x - shiro.x > 0:
                        citizen.left = True
                    else:
                        citizen.left = False
            else:
                if citizen.x - shiro.x > 0:
                    citizen.left = True
                else:
                    citizen.left = False


            if math.fabs(citizen.x - shiro.x) < 120:
                if (citizen.left and not shiro.left) or (not citizen.left and shiro.left):
                    if not citizen.fan:
                        citizen.scared = True
            else:
                if math.fabs(citizen.x - shiro.x) > 150:
                    if not citizen.fan:
                        citizen.scared = False
                    else:
                        if citizen.left and shiro.left:
                            citizen.x -= citizen.speed
                        elif not citizen.left and not shiro.left:
                            citizen.x += citizen.speed

            if citizen.scared:
                scared_ppl_counter += 1

            if citizen.fan:
                fans += 1
    else:
        for citizen in people:
            if citizen.fan == 0:
                citizen.scared = False


    display_refresh()

pygame.quit()
