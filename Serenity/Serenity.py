import os
import pygame

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (600, 200)

pygame.init()

icon = pygame.image.load('room/icon.png')
pygame.display.set_icon(icon)

scr_width = 1024
scr_height = 768

win = pygame.display.set_mode((scr_width, scr_height))

pygame.display.set_caption("Serenity")

bg = pygame.image.load("room/room_set.png")
title = pygame.image.load("room/title.png")
plant = [pygame.image.load("green_beret/1.png"), pygame.image.load("green_beret/2.png"), pygame.image.load("green_beret/3.png"), pygame.image.load("green_beret/4.png"), pygame.image.load("green_beret/5.png"), pygame.image.load("green_beret/6.png"), pygame.image.load("green_beret/7.png"), pygame.image.load("green_beret/8.png"), pygame.image.load("green_beret/9.png"), pygame.image.load("green_beret/10.png"), pygame.image.load("green_beret/11.png"), pygame.image.load("green_beret/12.png"), pygame.image.load("green_beret/13.png"), pygame.image.load("green_beret/14.png"), pygame.image.load("green_beret/15.png"), pygame.image.load("green_beret/16.png")]
pot_skin = pygame.image.load("room/pot_sunset_skin.png")
glass = [pygame.image.load("room/glass/glass_full.png"), pygame.image.load("room/glass/glass_empty.png")]
glass_stroke = [pygame.image.load("room/glass/glass_stroke1.png"), pygame.image.load("room/glass/glass_stroke2.png"), pygame.image.load("room/glass/glass_stroke3.png"), pygame.image.load("room/glass/glass_stroke4.png"), pygame.image.load("room/glass/glass_stroke5.png")]
moon_img = pygame.image.load("room/moon.png")
city_img = pygame.image.load("room/city.png")
cloud = pygame.image.load("room/cloud.png")

meter_frame = pygame.image.load("room/meter.png")


def drawtext(message: str, pos: tuple, color=None, custom=None):
    if color is None:
        color = (0, 0, 0)
    if custom is None:
        font = pygame.font.Font('freesansbold.ttf', 22)
    else:
        font = pygame.font.Font('room/Taylor_Swift_Handwriting_Font.ttf', 22)
    text = font.render(message, True, color)
    win.blit(text, pos)

cloud_x = -200
cloud_y = 10

def cloud_float():
    global cloud_x, cloud_y

    if cloud_x < 800:
        cloud_x += 0.2
    else:
        cloud_x = -200


class Plant:
    def __init__(self):
        self.x = 605
        self.y = -70
        self.frame = 0
        self.water = 100
        self.lvl = 0

    def grow(self):
        if self.frame < 90:
            self.frame += 1
        else:
            if self.water > 0:
                if self.lvl < 15:
                    self.water -= 10
                    self.lvl += 1
                    print(self.lvl)
                    print(self.water)
            self.frame = 0


class Glass:
    def __init__(self):
        self.x = 830
        self.y = 440
        self.height = 108
        self.width = 67
        self.frame = 0
        self.empty = 0
        self.stroke = False
        self.str_frame_idle = 0
        self.str_frame = 0

    def refill(self):
        if self.empty == 1:
            if self.frame < 210:
                self.frame += 1
            else:
                if self.empty == 1:
                    self.empty = 0
                    self.frame = 0
                else:
                    self.frame = 0

    def highlight(self):
        if self.stroke:
            if self.str_frame_idle < 3:
                self.str_frame_idle += 1
            else:
                if self.str_frame < 4:
                    self.str_frame += 1
                    self.str_frame_idle = 0
                else:
                    self.str_frame = 4
                    self.str_frame_idle = 0
        elif not self.stroke and self.str_frame == 4:
            self.str_frame = 0
            self.str_frame_idle = 0

    def use(self):
        self.empty = 1


class Meter:
    def __init__(self, color=None):
        self.x = 820
        self.y = 40
        self.height = 20
        self.bar_w = 1.29
        if color is None:
            self.color = (0, 0, 0)
        else:
            self.color = color


weed = Plant()
glass_item = Glass()
water_meter = Meter((87, 226, 229))


class Overview:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

        if x is not None and y is not None:
            self.text_x = self.x
            self.text_y = self.y - 40

    def search(self):
        if pygame.mouse.get_pressed() == (1, 0, 0):
            print(pygame.mouse.get_pos())

    def describe(self):
        if self.x > 678 and self.x < 753 and self.y > 337 and self.y < 463:
            drawtext("someone's growing :3", (self.text_x - 100, self.text_y), (255, 255, 255), custom=True)

        if self.x > 832 and self.x < 961 and self.y > 53 and self.y < 90:
            drawtext("it's a water meter", (self.text_x - 100, self.text_y + 70), (255, 255, 255), custom=True)

        if self.x > 835 and self.x < 887 and self.y > 455 and self.y < 535:
            drawtext("it's a glass of water", (self.text_x - 100, self.text_y), (255, 255, 255), custom=True)



def redrawScreen():
    global text, cloud_x, cloud_y

    win.blit(city_img, (20, 0))

    win.blit(cloud, (cloud_x, cloud_y))

    win.blit(bg, (0, 0))

    win.blit(pot_skin, (weed.x + 66, weed.y + 471))

    win.blit(plant[weed.lvl], (weed.x, weed.y))

    win.blit(glass[glass_item.empty], (glass_item.x, glass_item.y))
    if glass_item.stroke:
        win.blit(glass_stroke[glass_item.str_frame], (glass_item.x, glass_item.y))


    win.blit(meter_frame, (water_meter.x, water_meter.y))
    pygame.draw.rect(win, water_meter.color, (water_meter.x + 12, water_meter.y + 13, water_meter.bar_w * weed.water, water_meter.height))

    drawtext('water', (water_meter.x + 85, water_meter.y + 40), water_meter.color, custom=None)
    win.blit(title, (200, 520))

    tips = Overview(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    tips.search()
    tips.describe()

    pygame.display.update()


# mainloop
run = True
while run:
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if pygame.mouse.get_pos()[0] > 835 and pygame.mouse.get_pos()[0] < 887 and pygame.mouse.get_pos()[1] > 455 and pygame.mouse.get_pos()[1] < 535:
        glass_item.stroke = True
        if pygame.mouse.get_pressed()[0] == 1 and glass_item.empty == 0:
            glass_item.use()
            if weed.water >= 30:
                weed.water = 100
            else:
                weed.water += 70
    else:
        glass_item.stroke = False
        glass_item.str_frame = 0

    glass_item.highlight()
    glass_item.refill()

    weed.grow()
    cloud_float()

    redrawScreen()

pygame.quit()