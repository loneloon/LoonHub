import os
import datetime

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (600, 200)

import pygame
pygame.init()

scr_width = 900
scr_height = 550

win = pygame.display.set_mode((scr_width, scr_height))

scene0 = pygame.image.load("img/scene0.png")
scene1 = pygame.image.load("img/scene.png")
scene2 = pygame.image.load("img/scene2.png")

pygame.display.set_caption("KirbySha")

phonecall = False

stage = 0



def drawtext(message: str, pos: tuple, color=None, size=None):
    if color is None:
        color = (0, 0, 0)
    if size is None:
        size = 22

    font = pygame.font.Font('freesansbold.ttf', size)

    text = font.render(message, True, color)
    win.blit(text, pos)


class Kirby:
    def __init__(self):
        self.x = -40
        self.y = 125
        self.right = True

        self.w_f = 0
        self.s_f = 0
        self.r_f = 0
        self.e_f = 0

        self.line = 0

        self.walk_fr = [pygame.image.load(f"img/walk/{i+1}.png") for i in range(10)]
        self.stand_fr = [pygame.image.load(f"img/stand/{i+1}.png") for i in range(7)]
        self.reach_fr = [pygame.image.load(f"img/reach/{i+1}.png") for i in range(6)]
        self.eat_fr = [pygame.image.load(f"img/mouth/{i+1}.png") for i in range(9)]
        self.speak_bub = pygame.image.load("img/dialogue.png")

        self.prim_range = ''
        self.sec_code = ''

    def walk(self):
        if not self.right:
            win.blit(self.walk_fr[self.w_f], (self.x, self.y))
        else:
            win.blit(pygame.transform.flip(self.walk_fr[self.w_f], True, False), (self.x, self.y))

        if self.w_f < len(self.walk_fr) - 1:
            self.w_f += 1
        else:
            self.w_f = 0

    def stand(self):
        if not self.right:
            win.blit(self.stand_fr[self.s_f], (self.x, self.y))
        else:
            win.blit(pygame.transform.flip(self.stand_fr[self.s_f], True, False), (self.x, self.y))

        if self.s_f < len(self.stand_fr) - 1:
            self.s_f += 1
        else:
            self.s_f = 0

    def reach(self):
        if self.right:
            win.blit(self.reach_fr[self.r_f], (self.x, self.y))
        else:
            win.blit(pygame.transform.flip(self.reach_fr[self.r_f], True, False), (self.x, self.y))

        if self.r_f < len(self.reach_fr) - 1:
            self.r_f += 1
        else:
            self.r_f = 0

    def reach_rev(self):
        if self.right:
            win.blit(self.reach_fr[self.r_f], (self.x, self.y))
        else:
            win.blit(pygame.transform.flip(self.reach_fr[self.r_f], True, False), (self.x, self.y))

        if self.r_f > 0:
            self.r_f -= 1


    def eat(self):
        if not self.right:
            win.blit(self.eat_fr[self.e_f], (self.x, self.y))
        else:
            win.blit(pygame.transform.flip(self.eat_fr[self.e_f], True, False), (self.x, self.y))

        if self.e_f < len(self.eat_fr) - 1:
            self.e_f += 1


    def speak(self, text1, text2, bpos, pos, size=None):
        if size is None:
            size = 22

        if self.right:
            win.blit(self.speak_bub, (bpos[0], bpos[1]))
            drawtext(text1, (pos[0], pos[1]), size=size)
            drawtext(text2, (pos[0], pos[1]+40), size=size)
        else:
            win.blit(pygame.transform.flip(self.speak_bub, True, False), (bpos[0], bpos[1]))
            drawtext(text1, (pos[0], pos[1]), size=size)
            drawtext(text2, (pos[0], pos[1] + 40), size=size)


kirby = Kirby()

sprites = {'tomatoes':'Tm7j5', 'cabbage':'_cABg', 'cheese':'41iZz', 'chicken':'ChkN>', 'corn':'Ko0Rn', 'donuts':'DO?tS', 'bread':'bread', 'eggs':'E3G62', 'milk':'MIWq#'}

class Food:
    def __init__(self, name, code, r, c):
        self.col = [210, 290, 370]
        self.row = [140, 205, 305]
        self.eaten = False
        self.chosen = False

        self.x = self.col[c]
        self.y = self.row[r]

        self.margin = (self.y - 370) / (self.x - 586)

        self.image = pygame.transform.scale(pygame.image.load(f"img/food/{name}.png"), (85, 85))
        self.code = code

    def fly(self):
        if self.chosen:
            self.x += 10
            self.y += 10*self.margin

    def sparkle(self):
        pass


foods = []

row = 0
col = 0

for food, code in sprites.items():
    foods.append(Food(food, code, row, col))
    if row < 2:
        row+=1
    else:
        row=0
        col+=1

def display_refresh():
    global stage, inc_food, sec_code

    if stage == 0:
        win.blit(scene0, (0, 0))

        kirby.stand()
        if kirby.line == 0:
            kirby.speak("So hungry, i could",  "eat a horse right now!", (240, 90), (350, 220))
        elif kirby.line == 1:
            kirby.speak("I need to order a pizza", "ASAP! I'm starving here!", (240, 90), (335, 215))
    elif stage == 1:
        win.blit(scene0, (0, 0))
        if kirby.x < 400:
            kirby.walk()
            kirby.x += 18
        else:
            kirby.reach()
            if kirby.r_f == 5:
                stage += 1
    elif stage == 2:
        win.blit(scene2, (0, 0))
        if len(kirby.prim_range) == 8:
            stage += 1
            kirby.line = 0
    elif stage == 3:
        win.blit(scene0, (0, 0))
        if kirby.r_f > 0:
            kirby.reach_rev()
        else:
            if kirby.right:
                kirby.right = False
            kirby.stand()
            if kirby.line == 0:
                kirby.speak("FIFTEEN MINUTES!?!?!", "IT IS WAY TOO LONG!", (200, 90), (260, 220), size=21)
            elif kirby.line == 1:
                kirby.speak("   I need to talk to the fridge.", "Lemme holla at you, brother.", (200, 90), (250, 215), size=19)
    elif stage == 4:
        win.blit(scene1, (0, 0))
        kirby.stand()
        for food in foods:
            win.blit(food.image, (food.x, food.y))
        if kirby.line == 0:
            kirby.speak('       WOAH!       ', "Now what do we have here...", (200, 90), (250, 220), size=20)
        elif kirby.line == 1:
            kirby.speak("Just a few bites! Don't wanna", "lose my appetite before pizza.", (200, 90), (250, 220), size=19)
    elif stage == 5:
        win.blit(scene1, (0, 0))
        if inc_food > 0:
            kirby.eat()
        else:
            kirby.stand()

        inc_food = 0
        chosen_food = []
        for idx, food in enumerate(foods):
            if not food.eaten:
                if not food.chosen:
                    win.blit(food.image, (food.x, food.y))
                else:
                    chosen_food.append(food)

        for i in chosen_food:
            i.fly()
            win.blit(i.image, (i.x, i.y))
            if 410 < i.x < 530:
                inc_food += 1
            elif i.chosen and i.x > 530:
                i.eaten = True
                kirby.sec_code += i.code
                if kirby.e_f == 8:
                    kirby.e_f = 0


    pygame.display.update()


run = True

while run:
    pygame.time.delay(80)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if stage == 0:
        if kirby.line == 0:
            if pygame.mouse.get_pressed() == (1, 0, 0):
                kirby.line += 1
                pygame.time.delay(80)
        else:
            if pygame.mouse.get_pressed() == (1, 0, 0):
                stage += 1
                pygame.time.delay(80)

    if stage == 2:
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if (302 < pygame.mouse.get_pos()[0] < 326) and (266 < pygame.mouse.get_pos()[1] < 280):
                #print("1")
                kirby.prim_range += '1'
                pygame.time.delay(80)
            if (330 < pygame.mouse.get_pos()[0] < 355) and (279 < pygame.mouse.get_pos()[1] < 295):
                #print("2")
                pygame.time.delay(80)
                kirby.prim_range += '2'
            if (362 < pygame.mouse.get_pos()[0] < 386) and (292 < pygame.mouse.get_pos()[1] < 309):
                #print("3")
                pygame.time.delay(80)
                kirby.prim_range += '3'
            if (289 < pygame.mouse.get_pos()[0] < 311) and (286 < pygame.mouse.get_pos()[1] < 300):
                #print("4")
                pygame.time.delay(80)
                kirby.prim_range += '4'
            if (317 < pygame.mouse.get_pos()[0] < 341) and (299 < pygame.mouse.get_pos()[1] < 311):
                #print("5")
                pygame.time.delay(80)
                kirby.prim_range += '5'
            if (349 < pygame.mouse.get_pos()[0] < 373) and (312 < pygame.mouse.get_pos()[1] < 329):
                #print("6")
                pygame.time.delay(80)
                kirby.prim_range += '6'
            if (276 < pygame.mouse.get_pos()[0] < 298) and (303 < pygame.mouse.get_pos()[1] < 318):
                #print("7")
                pygame.time.delay(80)
                kirby.prim_range += '7'
            if (304 < pygame.mouse.get_pos()[0] < 327) and (318 < pygame.mouse.get_pos()[1] < 332):
                #print("8")
                pygame.time.delay(80)
                kirby.prim_range += '8'
            if (333 < pygame.mouse.get_pos()[0] < 356) and (331 < pygame.mouse.get_pos()[1] < 349):
                #print("9")
                pygame.time.delay(80)
                kirby.prim_range += '9'
            if (292 < pygame.mouse.get_pos()[0] < 314) and (338 < pygame.mouse.get_pos()[1] < 351):
                #print("0")
                pygame.time.delay(80)
                kirby.prim_range += '0'

    if stage == 3:
        if kirby.line == 0:
            if pygame.mouse.get_pressed() == (1, 0, 0):
                kirby.line += 1
                pygame.time.delay(80)
        else:
            if pygame.mouse.get_pressed() == (1, 0, 0):
                stage += 1
                kirby.line = -1
                pygame.time.delay(80)

    if stage == 4:
        if kirby.line < 0:
            if pygame.mouse.get_pressed() == (1, 0, 0):
                kirby.line += 1
                pygame.time.delay(80)
        elif kirby.line == 0:
            if pygame.mouse.get_pressed() == (1, 0, 0):
                kirby.line += 1
                pygame.time.delay(80)
        else:
            if pygame.mouse.get_pressed() == (1, 0, 0):
                kirby.line = 0
                stage += 1
                pygame.time.delay(80)
                inc_food = 0
                sync = datetime.datetime.now()
    if stage == 5:
        if pygame.mouse.get_pressed() == (1, 0, 0) and (datetime.datetime.now() - sync).microseconds > 40000:
            if (210 < pygame.mouse.get_pos()[0] < 290) and (140 < pygame.mouse.get_pos()[1] < 225):
                foods[0].chosen = True
            elif (290 < pygame.mouse.get_pos()[0] < 370) and (140 < pygame.mouse.get_pos()[1] < 225):
                foods[3].chosen = True
            elif (370 < pygame.mouse.get_pos()[0] < 450) and (140 < pygame.mouse.get_pos()[1] < 225):
                foods[6].chosen = True
            elif (210 < pygame.mouse.get_pos()[0] < 290) and (205 < pygame.mouse.get_pos()[1] < 290):
                foods[1].chosen = True
            elif (290 < pygame.mouse.get_pos()[0] < 370) and (205 < pygame.mouse.get_pos()[1] < 290):
                foods[4].chosen = True
            elif (370 < pygame.mouse.get_pos()[0] < 450) and (205 < pygame.mouse.get_pos()[1] < 290):
                foods[7].chosen = True
            elif (210 < pygame.mouse.get_pos()[0] < 290) and (305 < pygame.mouse.get_pos()[1] < 390):
                foods[2].chosen = True
            elif (290 < pygame.mouse.get_pos()[0] < 370) and (305 < pygame.mouse.get_pos()[1] < 390):
                foods[5].chosen = True
            elif (370 < pygame.mouse.get_pos()[0] < 450) and (305 < pygame.mouse.get_pos()[1] < 390):
                foods[8].chosen = True
            sync = datetime.datetime.now()

    if len(kirby.sec_code) > 9:
        run = False
        #print(kirby.prim_range, kirby.sec_code)

    display_refresh()

pygame.quit()
