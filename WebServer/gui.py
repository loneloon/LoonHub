import os
import string
import datetime
from client import Network
import select


# system tweaks

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (450, 200)

import pygame

# screen

pygame.init()

scr_x = 450
scr_y = 200
scr_width = 700
scr_height = 400

win = pygame.display.set_mode((scr_width, scr_height))

win.fill((255, 255, 255, 128))
pygame.display.set_caption("Chat Client")

bg = pygame.image.load("img/body2.png")
send_b = pygame.image.load("img/send.png")
key = pygame.image.load("img/key.png")
glasses = pygame.image.load("img/glasses.png")


net = Network()

print_cash = ''
chat_feed = ''
user_input = ''
message_sent = False
time_sent = None

last_sync = datetime.datetime.now()
token = ''

def data_sync():
    global message_sent, time_sent, chat_feed, user_input

    net.send(user_input) # withheld messages are sent
    user_input = '' # user's own message cash wiped



def drawtext(message: str, pos: tuple, color=None, fontsize=None, linelen=None, custom=None):
    if color is None:
        color = (0, 0, 0)

    if fontsize is None:
        fontsize = 22

    if linelen is None:
        linelen = 38

    if custom is None:
        font = pygame.font.Font('freesansbold.ttf', fontsize)
    else:
        font = pygame.font.Font('room/Taylor_Swift_Handwriting_Font.ttf', 20)

    line = ''
    rows = []
    for i in message:
        if len(line) < linelen:
            line += i
        elif len(line) == linelen:
            rows.append(font.render(line, True, color))
            line = ''

    if line != '':
        rows.append(font.render(line, True, color))
        line = ''

    for row in rows:
        win.blit(row, pos)
        pos = (pos[0], pos[1] + 20)


def display_refresh():
    global message_sent, time_sent, chat_feed

    win.blit(bg, (0, 0))

    # cutting chat stream down to window size
    try:
        if len(chat_feed) > 280:
            chat_feed = chat_feed[-280:]
    except TypeError:
        chat_feed = ''

    # chat text display
    drawtext(chat_feed, (290, 105), (0, 0, 0), linelen=40, fontsize=16)

    # user input
    drawtext(print_cash, (212, 265), (0, 0, 0))

    # 'message sent' lifetime
    if message_sent and (datetime.datetime.now() - time_sent).seconds < 4:
        drawtext('Message sent', (320, 350), (111, 156, 235))


    win.blit(send_b, (494, 336))
    win.blit(key, (20, 270))
    win.blit(glasses, (20, 340))

    pygame.display.update()


run = True

while run:
    pygame.time.delay(40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_BACKSPACE]:
        print_cash = print_cash[:-1]


    if keys[pygame.K_RETURN]:
        if print_cash != '':
            message_sent = True
            time_sent = datetime.datetime.now()
            user_input += print_cash
            print_cash = ''


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.unicode in (string.ascii_lowercase + string.ascii_uppercase + string.digits + ' ') and len(
                    print_cash) < 114:
                print_cash += event.unicode
        elif event.type == pygame.QUIT:
            run = False

    if user_input != '':
        data_sync() # withheld messages sent if there are any

    if net.chat_feed != '':
        token = net.chat_feed[-3:] # token recovered from the message delivery
        net.send(token) # token sent back as a validation of receipt
        token = '' # token wiped
        chat_feed += net.chat_feed[:-3] # message stripped off its token and added to user's chat history/displayed
        net.chat_feed = '' # initial message wiped

    net.read() # requesting to read the message feed, socket is locked unless the message exists to stop listening
    net.client.setblocking(False) # socket unlocked
    display_refresh() # chat window refreshed
pygame.quit()


# Где-то остаётся кусочек токена у клиента (больше не остаётся, всё нормально)