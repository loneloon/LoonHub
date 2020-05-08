import datetime
import random
import os
from word_scraper import WikiScraper

word_src = WikiScraper()

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (450, 200)

import pygame

pygame.init()

scr_width = 960
scr_height = 630

isFullscreen = False

win = pygame.display.set_mode((scr_width, scr_height))

pygame.display.set_caption("Tigre De Shroedinger")


loader = [pygame.transform.scale(pygame.image.load(f'loader/{i+1}.png'), (930, 630)) for i in range(22)]

load_sync = datetime.datetime.now()

# while (datetime.datetime.now() - load_sync).seconds < 6:
#     for i in loader:
#         pygame.time.delay(70)
#         win.blit(i, (30, -40))
#         pygame.display.update()

run = True

pygame.display.toggle_fullscreen()

bg = pygame.transform.scale(pygame.image.load("level_opt.png"), (960, 630))

def drawtext(message: str, pos: tuple, color=None):
    global left, right

    cfont = pygame.font.Font('youmurdererbb_reg.ttf', 90)
    if color is None:
        text = cfont.render(message, True, (204, 41, 54))
    else:
        text = cfont.render(message, True, (0, 0, 0))

    win.blit(text, (pos[0], pos[1]))


class Problem:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.operations = ['+', '-', '*', '/']
        self.left = 0
        self.right = 0
        self.prob_string = None
        self.result = None
        self.answer = '?'
        self.array = []
        self.op = ''
        self.input_idle = False
        self.input_cd = 20

    def choose_op(self):
        return random.choice(self.operations)

    def new_problem(self, operation):
        self.op = operation

        if operation in '+-':
            if operation == '+':
                self.left, self.right = random.randint(0, 200), random.randint(0, 200)
                self.result = self.left + self.right
            else:
                self.left, self.right = random.randint(0, 200), random.randint(0, 200)
                self.result = self.left - self.right
        else:
            if operation == '*':
                self.left, self.right = random.randint(0, 10), random.randint(0, 10)
                self.result = self.left * self.right

            else:
                self.left = random.randint(27, 101)
                self.right = random.randint(1, 9)
                while (self.left % self.right != 0):
                    self.left = random.randint(27, 101)
                    self.right = random.randint(1, 9)
                self.result = int(self.left / self.right)

        self.prob_string = f'{self.left} {self.op} {self.right} = {self.answer}'
        print(self.prob_string)

    def display(self):
        if self.input_cd > 0:
            self.input_idle = True
            self.input_cd -= 1
        else:
            self.input_idle = False

        drawtext(self.prob_string, (self.x + 3, self.y + 3), 'black')
        drawtext(self.prob_string, (self.x, self.y))

    def solve(self):
        if str(self.answer) == str(self.result):
            print("Correct!")
            return 0
        else:
            print("Wrong!")
            return 1

    def type(self, key=None, delete=None):
        if self.answer == '?':
            self.answer = ''

        if key is not None:
            self.answer += key
            problems.input_cd += 4

        if delete is not None:
            self.answer = self.answer[:-1]
            problems.input_cd += 2

        self.prob_string = f'{self.left} {self.op} {self.right} = {self.answer}'


problems = Problem(320, 300)


class Character:
    def __init__(self, x, y, char_dir: str):
        self.x = x
        self.y = y
        self.health = 100
        self.stand_frames_idx_turn = 0
        self.stand_pass = 0
        self.stand_pass_max = 0
        self.char = char_dir
        self.dead = False
        self.isEvading = False
        self.isShooting = False
        self.shot_unprocessed = False
        self.shoot_frames_turn = 0
        self.ev_frames_turn = 0

        self.bot_attack_sync = datetime.datetime.now()

        if self.char == 'player':
            self.stand_pass_max = 5
        elif self.char == 'bot':
            self.stand_pass_max = 7
        self.idle = True
        if self.char == 'player':
            self.stand_frames = [pygame.image.load(f'{self.char}/stand/{i+1}.png') for i in range(19)]
        elif self.char == 'bot':
            self.stand_frames = [pygame.image.load(f'{self.char}/stand/0dam/{i + 1}.png') for i in range(8)]
            self.stand_frames1 = [pygame.image.load(f'{self.char}/stand/1dam/{i + 1}.png') for i in range(8)]
            self.stand_frames2 = [pygame.image.load(f'{self.char}/stand/2dam/{i + 1}.png') for i in range(8)]
            self.stand_frames3 = [pygame.image.load(f'{self.char}/stand/3dam/{i + 1}.png') for i in range(8)]

            self.shoot_frames = [pygame.image.load(f'{self.char}/shoot/0dam/{i + 1}.png') for i in range(47)]
            self.shoot_frames1 = [pygame.image.load(f'{self.char}/shoot/1dam/{i + 1}.png') for i in range(47)]
            self.shoot_frames2 = [pygame.image.load(f'{self.char}/shoot/2dam/{i + 1}.png') for i in range(47)]

            self.beam_frames = [pygame.image.load(f'beam/{i + 1}.png') for i in range(9)]

        if self.char == 'player':
            self.shoot_frames = [pygame.image.load(f'{self.char}/shoot/{i+1}.png') for i in range(38)]
            self.beam_frames = [pygame.image.load(f'beam/{i+1}.png') for i in range(9)]
            self.evade_frames = [pygame.image.load(f'{self.char}/evade/{i+1}.png') for i in range(14)]


    def bot_random_attack(self):
        if self.char == 'bot':
            if not timer.start and not self.isShooting and (self.health > 0):
                if random.randint(0, 200) % 2 == 0:
                    if (datetime.datetime.now() - self.bot_attack_sync).seconds > 14:
                        bot.isShooting = True
                        bot.shot_unprocessed = True
                        self.bot_attack_sync = datetime.datetime.now()

    def stand(self):
        if self.idle:
            if self.stand_pass < self.stand_pass_max*2:
                if not timer.start:
                    self.stand_pass += 1
            else:
                if self.stand_frames_idx_turn < len(self.stand_frames)-1:
                    self.stand_frames_idx_turn += 1
                else:
                    self.stand_frames_idx_turn = 0
                self.stand_pass = 0

            if self.char == 'bot':
                if self.health > 60:
                    win.blit(self.stand_frames[self.stand_frames_idx_turn], (self.x, self.y))
                elif self.health > 40:
                    win.blit(self.stand_frames1[self.stand_frames_idx_turn], (self.x, self.y))
                elif self.health > 0:
                    win.blit(self.stand_frames2[self.stand_frames_idx_turn], (self.x, self.y))
                else:
                    win.blit(self.stand_frames3[self.stand_frames_idx_turn], (self.x, self.y))
            else:
                win.blit(self.stand_frames[self.stand_frames_idx_turn], (self.x, self.y))

    def shoot(self):
        if self.isShooting:
            if self.char == 'player':
                if not timer.start and (self.health > 0):
                    if self.stand_pass < self.stand_pass_max and (self.shoot_frames_turn < 13 or self.shoot_frames_turn > 16):
                        self.stand_pass += 1
                    else:
                        self.stand_pass = 0
                        if self.shoot_frames_turn < len(self.shoot_frames)-1:
                            self.shoot_frames_turn += 1
                        else:
                            self.isShooting = False
                            self.shoot_frames_turn = 0
                            self.stand_pass = 0
                    if self.shoot_frames_turn > 13 and self.shoot_frames_turn < 21:
                        win.blit(self.beam_frames[self.shoot_frames_turn-13], (self.x+460, self.y))
                    win.blit(self.shoot_frames[self.shoot_frames_turn], (self.x, self.y))
            elif self.char == 'bot':
                if not timer.start and (self.health > 0):
                    if self.stand_pass < self.stand_pass_max and (self.shoot_frames_turn < 27 or self.shoot_frames_turn > 32):
                        self.stand_pass += 1
                    else:
                        self.stand_pass = 0
                        if self.shoot_frames_turn < len(self.shoot_frames)-1:
                            self.shoot_frames_turn += 1
                        else:
                            self.isShooting = False
                            self.shoot_frames_turn = 0
                            self.stand_pass = 0

                if self.health > 60:
                    frames2use = self.shoot_frames
                elif self.health > 40:
                    frames2use = self.shoot_frames1
                else:
                    frames2use = self.shoot_frames2

                if self.shoot_frames_turn > 26 and self.shoot_frames_turn < 35:
                    win.blit(self.beam_frames[self.shoot_frames_turn-26], (self.x-780, self.y+210))

                win.blit(frames2use[self.shoot_frames_turn], (self.x-120, self.y))


    def evade(self):
        if self.char == 'player':
            if self.isEvading:
                if self.stand_pass < self.stand_pass_max and (
                        self.ev_frames_turn < 12):
                    self.stand_pass += 1
                else:
                    self.stand_pass = 0
                    if self.ev_frames_turn < len(self.evade_frames) - 1:
                        self.ev_frames_turn += 1
                    else:
                        self.isEvading = False
                        self.ev_frames_turn = 0
                        self.stand_pass = 0
                        pygame.time.delay(50)
                win.blit(self.evade_frames[self.ev_frames_turn], (self.x, self.y))


    def recycle(self):
        if self.char == 'bot':
            if self.health <= 0:
                if self.x < 1000:
                    self.x += 5
                else:
                    self.dead = True
                    self.stand_frames_idx_turn = 0
                    self.stand_pass = 0
                    self.isEvading = False
                    self.isShooting = False
                    self.shot_unprocessed = False
                    self.shoot_frames_turn = 0
                    self.ev_frames_turn = 0
                    self.bot_attack_sync = datetime.datetime.now()
            else:
                if self.x > 540:
                    self.x -= 5
        elif self.char == 'player':
            if self.health <= 0 and not self.dead:
                trainer.frames = 0
                self.dead = True


gunner = Character(-150, 60, 'player')
bot = Character(540, 40, 'bot')

class TypeWriter:
    def __init__(self, pos=None):
        if pos is None:
            self.x = 360
            self.y = 280
        else:
            self.x = pos[0]
            self.y = pos[1]
        self.task = str(word_src.get_word()).lower()
        self.answer = ''
        self.running = False
        self.sync = None

    def read(self):
        if timer.start and timer.type == 'evasion':
            if self.task == self.answer:
                self.running = False
                gunner.isEvading = True
                self.sync = datetime.datetime.now()
        else:
            if self.task == self.answer:
                self.running = False
                gunner.isEvading = True
                self.sync = datetime.datetime.now()
            else:
                pass
                # not evading

    def display(self):
        drawtext(self.task, (self.x + 3, self.y + 3), 'black')
        drawtext(self.task, (self.x, self.y))

        if self.answer != '':
            drawtext(self.answer, (self.x, self.y), color=(200, 30, 50))


evasion_check = TypeWriter((400,320))


class Timer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.start = False
        self.sync = None
        self.frames_idx = [i for i in range(6)]
        self.frames = [pygame.image.load(f'timer/{i + 1}.png') for i in self.frames_idx]
        self.frames_idx_turn = 0
        self.ripple_im = [pygame.image.load(f'timer/ripple/{i + 1}.png') for i in range(49)]
        self.ripple_fr = 0
        self.ripple_pass = 0
        self.type = None


    def five_sec(self):
        if self.start and (self.sync is None) and self.type == 'problem':
            self.y = -300
            problems.new_problem(problems.choose_op())
            self.sync = datetime.datetime.now()

        if self.y < 20:
            self.y += 20

        if self.start and self.type == 'problem':
            win.blit(self.frames[self.frames_idx_turn], (self.x, self.y))
            if self.frames_idx_turn < 5:
                if int((datetime.datetime.now() - self.sync).seconds) > 0.95:
                    self.sync = datetime.datetime.now()
                    self.frames_idx_turn += 1
            else:
                self.frames_idx_turn = 0
                self.start = False
                self.sync = None
                self.type = None
                problems.answer = '?'
                solve_outer()

    def evasion_time(self):
        if self.start and (self.sync is None) and self.type == 'evasion':
            self.y = -300
            evasion_check.running = True
            self.sync = datetime.datetime.now()

        if self.y < 20:
            self.y += 20

        if self.start and self.type == 'evasion':
            evasion_check.read()
            win.blit(self.frames[self.frames_idx_turn], (self.x, self.y))
            if self.frames_idx_turn < 5:
                if int((datetime.datetime.now() - self.sync).seconds) > 0.95:
                    self.sync = datetime.datetime.now()
                    self.frames_idx_turn += 1
                if not evasion_check.running:
                    self.frames_idx_turn = 0
                    self.start = False
                    self.sync = None
                    self.type = None
            else:
                evasion_check.read()
                if not evasion_check.running:
                    self.frames_idx_turn = 0
                    self.start = False
                    self.sync = None
                    self.type = None
                    evasion_check.answer = ''
                    evasion_check.task = str(word_src.get_word()).lower()
                    gunner.isEvading = True
                else:
                    evasion_check.running = False
                    self.frames_idx_turn = 0
                    self.start = False
                    self.sync = None
                    self.type = None
                    evasion_check.answer = ''
                    evasion_check.task = str(word_src.get_word()).lower()

    def ripple(self):
        if timer.start:
            win.blit(self.ripple_im[self.ripple_fr], (-20, -10))
            if self.ripple_pass < 2:
                self.ripple_pass += 1
            else:
                self.ripple_pass = 0
                if self.ripple_fr < 48:
                    self.ripple_fr += 1
                else:
                    self.ripple_fr = 0
        else:
            self.ripple_pass = 0
            self.ripple_fr = 0


timer = Timer(350, 20)

class Meter:
    def __init__(self, pos=None, color=None):
        self.x = 820
        self.y = 40

        if pos is not None:
            self.x = pos[0]
            self.y = pos[1]

        self.height = 20
        self.bar_w = 2.8
        if color is None:
            self.color = (0, 0, 0)
        else:
            self.color = color

player_hp_meter = Meter((30, 30), (33, 250, 144))
bot_hp_meter = Meter((600, 30), (33, 250, 144))


class Trainer:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.images = [pygame.image.load(f"tips/{i+1}.png") for i in range(5)]
        self.final_images = [pygame.image.load(f"tips/final/{i+1}.png") for i in range(20)]

        self.frames = 0
        self.fr_pass = 0
        self.advice = pygame.image.load(f"tips/adv_{random.choice((1, 2))}.png")
        self.sync = datetime.datetime.now()


    def new_adv(self):
        if (datetime.datetime.now() - self.sync).seconds > 30:
            self.sync = datetime.datetime.now()
            self.advice = pygame.image.load(f"tips/adv_{random.choice((1, 2))}.png")

    def display(self):
        self.new_adv()

        if not timer.start:
            if self.fr_pass < 7:
                self.fr_pass += 1
            else:
                self.fr_pass = 0
                if self.frames < 4:
                    self.frames += 1
                else:
                    self.frames = 0

        win.blit(self.images[self.frames], (self.x, self.y))
        if self.frames == 0 or self.frames == 4:
            win.blit(self.advice, (self.x + 80, self.y - 100 + 4))
        if self.frames == 1 or self.frames == 3:
            win.blit(self.advice, (self.x + 80, self.y - 100+2))
        if self.frames == 2:
            win.blit(self.advice, (self.x + 80, self.y - 100))

    def final_tip(self):
        if self.frames < 13:
            if self.fr_pass < 4:
                self.fr_pass += 1
            else:
                self.fr_pass = 0
                self.frames += 1
        elif self.frames >= 13:
            if self.fr_pass < 7:
                self.fr_pass += 1
            else:
                self.fr_pass = 0
                if self.frames < 13:
                    self.frames += 1
                else:
                    if self.frames < 19:
                        self.frames += 1
                    else:
                        self.frames = 13

        win.blit(self.final_images[self.frames], (self.x, self.y))



trainer = Trainer((300, 40))


class Particles:

    def __init__(self):
        self.x = random.randint(680, 800)
        self.y = random.randint(170, 260)
        self.gone = False

        self.size = random.randint(1, 5)
        self.image = pygame.image.load(f"bot/dust/{self.size}.png")

    def draw(self):
        win.blit(self.image, (self.x, self.y))

    def gravity(self):
        if self.y < 900:
            self.x += random.randint(-1, 1) + 1
            self.y += random.randint(4, 7) + (6 - self.size)
        else:
            self.gone = True

all_trash = []



def solve_outer():
    res = problems.solve()
    timer.frames_idx_turn = 0
    timer.start = False
    timer.sync = None
    problems.answer = '?'
    if res == 0:
        print("Attack succeeded")
        gunner.isShooting = True
        gunner.stand_pass = 0
    else:
        print("You suffer damage")
        gunner.health -= 10



def display_refresh():

    win.blit(bg, (0, 0))

    if gunner.dead:
        trainer.final_tip()
    else:
        trainer.display()

    timer.ripple()

    if bot.isShooting:
        bot.shoot()
    else:
        bot.stand()

    if gunner.isShooting:
        gunner.shoot()
    elif gunner.isEvading:
        gunner.evade()
    else:
        gunner.stand()

    if all_trash != []:
        for particle in all_trash:
            particle.draw()

    # healthbar section

    if gunner.isShooting and gunner.shoot_frames_turn == 15 and gunner.stand_pass == 0:
        if bot.health > 0:
            bot.health -= 20
            for n in range(random.randint(2, 10)):
                all_trash.append(Particles())

    if gunner.health > 60:
        pygame.draw.rect(win, player_hp_meter.color,
                         (player_hp_meter.x + 33, player_hp_meter.y + 13, player_hp_meter.bar_w * gunner.health,
                          player_hp_meter.height))
    elif gunner.health > 40:
        pygame.draw.rect(win, (237, 216, 61),
                         (player_hp_meter.x + 33, player_hp_meter.y + 13,
                          player_hp_meter.bar_w * gunner.health, player_hp_meter.height))
    else:
        pygame.draw.rect(win, (255, 0, 0),
                         (player_hp_meter.x + 33, player_hp_meter.y + 13,
                          player_hp_meter.bar_w * gunner.health, player_hp_meter.height))

    if bot.health > 60:
        pygame.draw.rect(win, bot_hp_meter.color,
                         (bot_hp_meter.x + 12, bot_hp_meter.y + 13, bot_hp_meter.bar_w * bot.health,
                          bot_hp_meter.height))
    elif bot.health > 40:
        pygame.draw.rect(win, (237, 216, 61),
                         (bot_hp_meter.x + 12, bot_hp_meter.y + 13,
                          bot_hp_meter.bar_w * bot.health, bot_hp_meter.height))
    elif bot.health > 0:
        pygame.draw.rect(win, (255, 0, 0),
                         (bot_hp_meter.x + 12, bot_hp_meter.y + 13,
                          bot_hp_meter.bar_w * bot.health, bot_hp_meter.height))


    if timer.start:
        if timer.type == 'problem':
            problems.display()
        elif timer.type == 'evasion' or evasion_check.sync is not None:
            evasion_check.display()

    if not evasion_check.running and not timer.start and (evasion_check.sync is not None):
        evasion_check.display()
        if (datetime.datetime.now() - evasion_check.sync).microseconds > 100000:
            evasion_check.sync = None
            evasion_check.answer = ''
            evasion_check.task = str(word_src.get_word()).lower()

    timer.five_sec()
    timer.evasion_time()

    pygame.display.update()


while run:
    pygame.time.delay(10)

    if all_trash != []:
        for idx, particle in enumerate(all_trash):
            particle.gravity()
            if particle.gone:
                del all_trash[idx]


    if not gunner.isShooting and not gunner.dead and not timer.start:
        bot.bot_random_attack()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if timer.start and timer.type == 'evasion':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pass
                else:
                    if (evasion_check.answer + str(event.unicode)) in evasion_check.task:
                        evasion_check.answer += event.unicode
                        pygame.time.delay(30)

    keys = pygame.key.get_pressed()

    if not isFullscreen:
        if keys[pygame.K_RETURN] and keys[pygame.K_LALT]:
            win = pygame.display.set_mode((scr_width, scr_height), flags=(pygame.FULLSCREEN))
            isFullscreen = True

    if isFullscreen:
        if keys[pygame.K_ESCAPE]:
            isFullscreen = False
            win = pygame.display.set_mode((scr_width, scr_height))

    if not timer.start and (not gunner.isShooting or gunner.shoot_frames_turn > 31) and not gunner.isEvading and not bot.dead:
        if keys[pygame.K_SPACE]:
            gunner.isShooting = False
            gunner.shoot_frames_turn = 0
            gunner.stand_pass = 0
            gunner.stand_frames_idx_turn = 14

            timer.start = True
            timer.type = 'problem'
        elif keys[pygame.K_LCTRL]:
            gunner.isShooting = False
            gunner.shoot_frames_turn = 0
            gunner.stand_pass = 0
            gunner.stand_frames_idx_turn = 14

            timer.start = True
            timer.type = 'evasion'

    if timer.start and not problems.input_idle and timer.type == 'problem':
        if keys[pygame.K_1]:
            problems.type('1')
        elif keys[pygame.K_2]:
            problems.type('2')
        elif keys[pygame.K_3]:
            problems.type('3')
        elif keys[pygame.K_4]:
            problems.type('4')
        elif keys[pygame.K_5]:
            problems.type('5')
        elif keys[pygame.K_6]:
            problems.type('6')
        elif keys[pygame.K_7]:
            problems.type('7')
        elif keys[pygame.K_8]:
            problems.type('8')
        elif keys[pygame.K_9]:
            problems.type('9')
        elif keys[pygame.K_0]:
            problems.type('0')
        elif keys[pygame.K_MINUS]:
            problems.type('-')
        elif keys[pygame.K_BACKSPACE]:
            problems.type(key=None, delete=True)

    if keys[pygame.K_RETURN] and timer.start:
        solve_outer()

    if bot.isShooting and bot.shot_unprocessed:
        if 26 < bot.shoot_frames_turn < 32:
            if gunner.isEvading and (3 < gunner.ev_frames_turn < 11):
                bot.shot_unprocessed = False
            else:
                gunner.health -= 20
                bot.shot_unprocessed = False


    gunner.recycle()
    bot.recycle()

    if bot.dead:
        bot.health = 100
        bot.dead = False

    display_refresh()


pygame.quit()

