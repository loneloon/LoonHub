import random
import time
import datetime
#from horse_names import HorseScraper

from write_to_xl import RecordResults as write_result

import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

pygame.init()

#h_n = HorseScraper()


def horse_name():
    first = []
    second = []

    with open("names/nouns.txt", "r") as nf:
        for i in nf.readlines():
            first.append(i.replace('\n', ''))
    with open("names/adjectives.txt", "r") as af:
        for i in af.readlines():
            second.append(i.replace('\n', ''))

    f_w = random.choice(first)
    s_w = random.choice(second)

    return s_w[0].upper() + s_w[1:] + " " + f_w



def drawtext(message: str, pos: tuple, color=None, custom=None, size=None):
    if size is None:
        size = 8

    if color is None:
        color = (0, 0, 0)
    if custom is None:
        font = pygame.font.SysFont('freesansbold.ttf', 22)
    elif custom == 'title':
        font = pygame.font.Font('names/Chalk Dash.ttf', size)
    elif custom == 'scribble':
        font = pygame.font.Font('names/Chalkabout.ttf', size)

    text = font.render(message, True, color)
    win.blit(text, pos)


scr_width = 1300
scr_height = 650

bg = pygame.image.load("img/track.jpeg")

win = pygame.display.set_mode((scr_width, scr_height))

pygame.display.set_caption("Amazing Race")

race_ended = False

jokey_skins = ['blue', 'green', 'magenta', 'navy', 'orange', 'purple', 'yellow']
horse_skins = ['brown', 'grey', 'white', 'wine']


class Horse:
    def __init__(self):
        self.clouds = False
        self.hell = False

        self.easter = random.randint(0, 200)
        if self.easter == 7:
            self.clouds = True
        if self.easter == 6:
            self.hell = True

        self.x = 20
        self.y = 0
        self.height = 10
        self.width = 20
        self.speed = 2
        self.winner = False
        self.finished = False
        self.name = horse_name()
        self.frame = 0
        self.frame_pass = 0
        self.jokey = random.choice(jokey_skins)
        self.horse = random.choice(horse_skins)

        if self.clouds:
            self.horse = 'clouds'
            self.name = 'Clouds? Clouds?'
            self.jokey = 'clouds'
        if self.hell:
            self.horse = 'hellish'
            self.name = 'Lucy'
            self.jokey = 'satan'

    def run(self):
        if not self.finished:
            self.x += self.speed
            if self.frame_pass < 1:
                self.frame_pass += 1
            else:
                self.frame_pass = 0
                if self.frame < 4:
                    self.frame += 1
                else:
                    self.frame = 0
            if self.speed > 1:
                self.speed += random.uniform(-0.4, 0.4)
                if self.speed > 5:
                    self.speed -= random.uniform(0, 0.4)
            else:
                self.speed += random.uniform(0, 0.5)


horse1, horse2, horse3 = Horse(), Horse(), Horse()

horses = [[horse1.name, horse1], [horse2.name, horse2], [horse3.name, horse3]]

horse1.y, horse2.y, horse3.y = 80, 220, 360


def display_refresh():
    pygame.time.delay(20)

    win.blit(bg, (0, 0))

    for i in horses:
        win.blit(pygame.image.load(f'img/horses/{i[1].horse}/{i[1].frame + 1}.png'), (i[1].x - 82, i[1].y - 82))
        win.blit(pygame.image.load(f'img/jokeys/{i[1].jokey}/{i[1].frame + 1}.png'), (i[1].x - 82, i[1].y - 82))
        drawtext(i[1].name, (i[1].x, i[1].y - 50), color=(255, 255, 255))

    pygame.display.update()


game_on = True

all_races = []


class Race:
    def __init__(self):
        global race_ended, game_on, all_races

        self.start_time = datetime.datetime.now()

        self.finish_time = []

    def go(self):
        global race_ended, game_on, all_races

        for i in horses:
            i[1].x = 20
            i[1].speed = 2
            i[1].finished = False
            race_ended = False

        while not race_ended and game_on:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_on = False

            for i in horses:
                i[1].run()
                if i[1].x > 1200 and not i[1].finished:
                    i[1].speed = 0
                    i[1].finished = True
                    self.finish_time.append([i[1].name, (datetime.datetime.now() - self.start_time).seconds])

            counter = 0
            for i in horses:
                if i[1].finished == False:
                    counter += 1
            if counter == 0:
                race_ended = True
                # print(self.finish_time)

            display_refresh()

        top_time = [0, 500]
        for i in self.finish_time:
            if i[1] < top_time[1]:
                top_time[0], top_time[1] = i[0], i[1]

        all_races.append(self.finish_time)
        print(f'And the winner is - {top_time[0]} with the top time of {top_time[1]} seconds!\r\n')
        for i in horses:
            if i[1].name == top_time[0]:
                i[1].winner = True

        pygame.time.delay(2000)

        for horse in horses:
            for result in self.finish_time:
                if horse[1].name == result[0]:
                    write_result(str(self.start_time), horse[1].name, result[1], horse[1].winner)
                    horse[1].winner = False

menu = True

skip = False

result_string = ''


def start_game():
    global result_string, menu, skip, all_races, horses

    if not menu:
        while len(all_races) < 3:
            next_race = Race()
            next_race.go()

        results = [['name', 0], ['name', 0], ['name', 0]]
        for idx, i in enumerate(horses):
            for j in all_races:
                for h in j:
                    if h[0] == i[0]:
                        results[idx][0] = h[0]
                        results[idx][1] += h[1]

        result_string = ("Results:",
                         "Name:" + " " * 7  + "Total time: ", results[0][0] + " " * (19 - len(results[0][0])) + str(results[0][1]) + " " *
                         (12 - len(str(results[0][1]))), results[1][0] + " " * (19 - len(results[1][0])) + str(results[1][1]) + " " * (12 - len(str(results[1][1]))),
                                                                         results[2][0] + " " * (19 - len(results[2][0])) + str(results[2][1]) + " " * (12 - len(str(results[2][1]))))

        # horse reset
        for i in horses:
            i[1].name = horse_name()
            i[0] = i[1].name
            i[1].frame = 0
            i[1].frame_pass = 0
            i[1].jokey = random.choice(jokey_skins)
            i[1].horse = random.choice(horse_skins)
            all_races = []
        menu = True



while menu and not skip:
    pygame.time.delay(20)

    win.blit(bg, (0, 0))

    if not race_ended:
        win.blit(pygame.image.load("img/st_scr.png"), (340, 200))
    else:
        win.blit(pygame.image.load("img/board.png"), (340, 200))
        drawtext(result_string[0], (400, 270), color = (255, 255, 255), custom='title', size=16)
        drawtext(result_string[1], (400, 320), color=(255, 255, 255), custom='title', size=10)
        drawtext(result_string[2], (400, 360), color=(255, 255, 255), custom='scribble', size=18)
        drawtext(result_string[3], (400, 400), color=(255, 255, 255), custom='scribble', size=18)
        drawtext(result_string[4], (400, 440), color=(255, 255, 255), custom='scribble', size=18)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            skip = True

    if pygame.mouse.get_pressed() == (1, 0, 0) and pygame.mouse.get_pos()[0] > 562 and pygame.mouse.get_pos()[
        0] < 726 and pygame.mouse.get_pos()[1] > 484 and pygame.mouse.get_pos()[1] < 540:
        all_races = []
        menu = False
        start_game()

    pygame.display.update()

pygame.quit()
