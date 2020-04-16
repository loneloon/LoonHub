import os
import pygame

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (600, 200)


pygame.init()

scr_width = 748
scr_height = 892

win = pygame.display.set_mode((scr_width, scr_height))

pygame.display.set_caption("Sunset Falls")

icon = pygame.image.load('retry/icon.png')
pygame.display.set_icon(icon)

# images
bg2 = pygame.image.load('retry/orange_cliff2.png')
bg = pygame.image.load('retry/orange_cliff.png')
dead = pygame.image.load('retry/dead.png')
retry = [pygame.image.load('retry/1.png'), pygame.image.load('retry/2.png'), pygame.image.load('retry/3.png'), pygame.image.load('retry/4.png')]

noise = [pygame.image.load("noise/1.png"), pygame.image.load("noise/2.png"), pygame.image.load("noise/3.png"), pygame.image.load("noise/4.png"), pygame.image.load("noise/5.png"), pygame.image.load("noise/6.png"), pygame.image.load("noise/7.png"), pygame.image.load("noise/8.png"), pygame.image.load("noise/9.png"), pygame.image.load("noise/10.png"), pygame.image.load("noise/11.png"), pygame.image.load("noise/12.png"), pygame.image.load("noise/13.png"), pygame.image.load("noise/14.png"), pygame.image.load("noise/15.png")]

flash = [pygame.image.load("retry/flash/1.png"), pygame.image.load("retry/flash/2.png"), pygame.image.load("retry/flash/3.png"), pygame.image.load("retry/flash/4.png"), pygame.image.load("retry/flash/5.png"), pygame.image.load("retry/flash/6.png"), pygame.image.load("retry/flash/7.png"), pygame.image.load("retry/flash/8.png"), pygame.image.load("retry/flash/9.png"), pygame.image.load("retry/flash/10.png"), pygame.image.load("retry/flash/11.png"), pygame.image.load("retry/flash/12.png"), pygame.image.load("retry/flash/13.png")]

title = pygame.image.load("retry/title1.png")

retry_idle = 0
retry_frame = 0
retry_x = 263
retry_y = 420

arrow = [pygame.image.load('retry/arrow_left_black.png'), pygame.image.load('retry/arrow_right_black.png')]

char_left_stand = [pygame.image.load('stand/stand_left_0.png'), pygame.image.load('stand/stand_left_1.png'), pygame.image.load('stand/stand_left_2.png'), pygame.image.load('stand/stand_left_3.png'), pygame.image.load('stand/stand_left_4.png')]
char_right_stand = [pygame.image.load('stand/stand_right_0.png'), pygame.image.load('stand/stand_right_1.png'), pygame.image.load('stand/stand_right_2.png'), pygame.image.load('stand/stand_right_3.png'), pygame.image.load('stand/stand_right_4.png')]

char_left_walk = [pygame.image.load('walk/walk_left_2.png'), pygame.image.load('walk/walk_left_3.png'), pygame.image.load('walk/walk_left_4.png'), pygame.image.load('walk/walk_left_5.png'), pygame.image.load('walk/walk_left_6.png'), pygame.image.load('walk/walk_left_7.png'), pygame.image.load('walk/walk_left_8.png'), pygame.image.load('walk/walk_left_9.png')]
char_right_walk = [pygame.image.load('walk/walk_right_2.png'), pygame.image.load('walk/walk_right_3.png'), pygame.image.load('walk/walk_right_4.png'), pygame.image.load('walk/walk_right_5.png'), pygame.image.load('walk/walk_right_6.png'), pygame.image.load('walk/walk_right_7.png'), pygame.image.load('walk/walk_right_8.png'), pygame.image.load('walk/walk_right_9.png')]
char_left_fall = [pygame.image.load('fall/fall_left_1.png'), pygame.image.load('fall/fall_left_2.png'), pygame.image.load('fall/fall_left_3.png'), pygame.image.load('fall/fall_left_4.png')]
char_right_fall = [pygame.image.load('fall/fall_right_1.png'), pygame.image.load('fall/fall_right_2.png'), pygame.image.load('fall/fall_right_3.png'), pygame.image.load('fall/fall_right_4.png')]

shadow = [pygame.image.load('walk/shadow_left.png'), pygame.image.load('walk/shadow_right.png')]

# title

title_x = -100
title_y = 100
title_idle = 0


isIntro = True


# terrain
cliff = 230

x = 400
y = 340
width = 63
height = 170
vel = 2
# jump params
isJump = False
jumpCount = 10
#
neg = 1
left = True
l_frame = 0
right = False
r_frame = 0

walk_frame = 0
walkCount = 0

idle_points = 10
isStanding = True
standCount = 0
# fall params
isDescending = False
isFalling = False
fallCount = 10
an_fall_count = -1
# Dead or Alive
isDead = False

noise_frame = 0

# text
text = None




def drawtext(message: str, pos: tuple):
    global left, right

    cfont = pygame.font.Font('retry/Taylor_Swift_Handwriting_Font.ttf', 22)
    text = cfont.render(message, True, (34, 32, 52))
    if left:
        win.blit(text, (pos[0]+60, pos[1]+10))
        win.blit(arrow[0], (pos[0] + 90, pos[1] + 30))
    else:
        win.blit(text, (pos[0] -60, pos[1] + 10))
        win.blit(arrow[1], (pos[0], pos[1] + 30))

def retry_anim():
    global retry_frame, retry_idle, retry_y, retry_x

    if retry_idle < 5:
        retry_idle += 1
    else:
        if retry_frame < 6:
            retry_frame += 1
            retry_idle = 0
            if retry_frame < 3:
                retry_y -= 1
            else:
                retry_y += 1
        else:
            retry_frame = 0
            retry_idle = 0


def restart():
    global neg, walkCount, isDead, isJump, isStanding, jumpCount, x, y, l_frame, r_frame, standCount, walk_frame, fallCount, an_fall_count, isDescending, text, isFalling, idle_points
    x = 400
    y = 340
    fallCount = 10
    an_fall_count = -1
    idle_points = 10
    isDead = False
    isStanding = True
    isDescending = False
    isFalling = False


def intro():
    global neg, walkCount, isDead, isJump, isStanding, jumpCount, x, y, l_frame, r_frame, standCount, walk_frame, an_fall_count, isDescending, text, isFalling, retry_frame, retry_idle, noise_frame, title_x, title_y, isIntro, title_idle


    win.blit(bg, (0, 0))
    win.blit(title, (title_x, title_y))

    if title_x < 180:
        title_x += 2
    else:
        if title_idle < 12:
            title_idle += 1
        else:
            isIntro = False

    win.blit(flash[title_idle], (0, 0))

    win.blit(noise[noise_frame], (0, 0))

    if noise_frame < 14:
        noise_frame += 1
    else:
        noise_frame = 0

    pygame.display.update()


def redrawScreen():
    global neg, walkCount, isDead, isJump, isStanding, jumpCount, x, y, l_frame, r_frame, standCount, walk_frame, an_fall_count, isDescending, text, isFalling, retry_frame, retry_idle, noise_frame

    win.blit(bg2, (0, 0))

    if isDead:
        win.blit(dead, (185, 150))
        if retry_frame <= 3:
            win.blit(retry[retry_frame], (retry_x, retry_y))
        elif retry_frame > 3:
            win.blit(retry[6 - retry_frame], (retry_x, retry_y))
        retry_anim()

    if idle_points > 10:
        isStanding = True
    elif idle_points < 10:
        isStanding = False

    if (x+5) > 230 and not isFalling and not isDead:
        if left:
            win.blit(shadow[0], (x+3, 340))
        else:
            win.blit(shadow[1], (x+5, 340))

    if isStanding:
        text = "I'm standing"
        if standCount < 10:
            if left:
                win.blit(char_left_stand[l_frame], (x, y))
            elif right:
                win.blit(char_right_stand[r_frame], (x, y))
            standCount += 1
        else:
            if left:
                if l_frame == 0:
                    neg = 1
                elif l_frame == 4:
                    neg = -1
                l_frame += (1*neg)
                win.blit(char_left_stand[l_frame], (x, y))
            elif right:
                if r_frame == 0:
                    neg = 1
                elif r_frame == 4:
                    neg = -1
                r_frame += (1 * neg)
                win.blit(char_right_stand[r_frame], (x, y))
            standCount = 0
    elif isDescending:
        if an_fall_count < 2:
            an_fall_count += 1
        if left:
            win.blit(char_left_fall[an_fall_count], (x, y))
        else:
            win.blit(char_right_fall[an_fall_count], (x, y))
    elif isFalling:
        text = "I'm falling"
        if fallCount >= 10 and (y > 500):
            an_fall_count = 3
        elif fallCount <= 10 and (an_fall_count < 3) and (y > 500):
            an_fall_count += 1
        elif an_fall_count < 2:
            an_fall_count += 1

        if left:
            win.blit(char_left_fall[an_fall_count], (x, y))
        else:
            win.blit(char_right_fall[an_fall_count], (x, y))
    else:
        text = "I'm walking"
        if walkCount < 2:
            if left:
                win.blit(char_left_walk[walk_frame], (x, y))
            elif right:
                win.blit(char_right_walk[walk_frame], (x, y))
            walkCount += 1
        else:
            if left:
                if walk_frame < 7:
                    walk_frame += 1
                else:
                    walk_frame = 0
                win.blit(char_left_walk[walk_frame], (x, y))
            elif right:
                if walk_frame < 7:
                    walk_frame += 1
                else:
                    walk_frame = 0
                win.blit(char_right_walk[walk_frame], (x, y))
            walkCount = 0

    drawtext(text, (x-30, y-40))  # <- uncomment this if you want status text over character



    win.blit(noise[noise_frame], (0, 0))

    if noise_frame < 14:
        noise_frame += 1
    else:
        noise_frame = 0

    pygame.display.update()

# mainloop
run = True
while run:
    pygame.time.delay(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if not isDead:
        if x < (cliff - width) and not isDead and y <= 340:
            isFalling = True

        if keys[pygame.K_LEFT] and x > 0:
            if right:
                walk_frame = 0
            x -= vel
            left = True
            right = False
            idle_points = 0

        if keys[pygame.K_RIGHT] and x < (scr_width - width):
            if left:
                walk_frame = 0
            x += vel
            left = False
            right = True
            idle_points = 0

        if not isJump or not isFalling:
            if keys[pygame.K_SPACE]:
                isJump = True

        if isJump:
            text = "I'm jumping"
            idle_points = 0
            fallCount += 1
            if jumpCount >= -10:
                neg = 1
                if jumpCount < 0:
                    isDescending = True
                    neg = -1
                y -= (jumpCount ** 2) * 0.5 * neg
                jumpCount -= 1
            else:
                isJump = False
                isDescending = False
                jumpCount = 10
                fallCount = 0
                an_fall_count = -1

        if isFalling and not isJump:
            idle_points = 0
            if fallCount >= 10 and (y < 340):
                y += (jumpCount ** 2) * 0.5
            else:
                y += 27
            fallCount -= 1


        if y > (892 + height):
            isFalling = False
            isDead = True

        idle_points += 1

    if (pygame.mouse.get_pos()[0] > 310) and (pygame.mouse.get_pos()[0] < 424) and (pygame.mouse.get_pos()[1] > (retry_y + 60)) and (pygame.mouse.get_pos()[1] < (retry_y + 100)) and pygame.mouse.get_pressed()[0] == 1:
        if isDead:
            restart()

    if isIntro:
        intro()
    else:
        redrawScreen()

pygame.quit()
