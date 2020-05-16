import pygame
import time
import random

pygame.init()

display_height = 600
display_width = 800

black = (0, 0, 0)
white = (255, 255, 255)
red = (232, 4, 4)
dark_red = (207, 3, 3)
green = (2, 230, 2)
dark_green = (5, 200, 5)

#declare this later
#map = [main, leftmain, rightmain, upforest, downforest...

disp = pygame.display.set_mode((display_width, display_height))

disp.fill(white)

Hester = pygame.image.load('resources/Hester.png')
HesterRight = pygame.image.load('resources/righthester.png')

HesterRight = [pygame.image.load('resources/righthester1.png'),
pygame.image.load('resources/righthester2.png'), pygame.image.load('resources/righthester3.png'),
pygame.image.load('resources/righthester4.png'), pygame.image.load('resources/righthester5.png')]

HesterLeft = [pygame.image.load('resources/lefthester1.png'),
pygame.image.load('resources/lefthester2.png'), pygame.image.load('resources/lefthester3.png'),
pygame.image.load('resources/lefthester4.png'), pygame.image.load('resources/lefthester5.png')]

DimmesdaleRight = [pygame.image.load('resources/rightdimmesdale1.png'),
pygame.image.load('resources/rightdimmesdale2.png'), pygame.image.load('resources/rightdimmesdale3.png'),
pygame.image.load('resources/rightdimmesdale4.png'), pygame.image.load('resources/rightdimmesdale5.png')]

DimmesdaleLeft = [pygame.image.load('resources/leftdimmesdale1.png'),
pygame.image.load('resources/leftdimmesdale2.png'), pygame.image.load('resources/leftdimmesdale3.png'),
pygame.image.load('resources/leftdimmesdale4.png'), pygame.image.load('resources/leftdimmesdale5.png')]

Dimmesdale = pygame.image.load('resources/Dimmesdale.png')
updimmesdale = pygame.image.load('resources/updimmesdale.png')
winthrop = pygame.image.load('resources/winthrop.png')
start = pygame.image.load('resources/start.png')
cabinexterior = pygame.image.load('resources/cabinExterior.png')
darkforest = pygame.image.load('resources/darkForest.png')
forest = pygame.image.load('resources/forest.png')
gravehouseexterior = pygame.image.load('resources/Graveyard.png')
mansionexterior = pygame.image.load('resources/mansionExterior.png')
mansioninterior = pygame.image.load('resources/mansionInterior.png')
town = pygame.image.load('resources/town.png')
ghouseenter = pygame.image.load('resources/graveyardHouseEntrance.png')
ghousebed = pygame.image.load('resources/graveyardHouseBedroom.png')
ghouseoffice = pygame.image.load('resources/graveyardHouseOffice.png')
hesterhouse = pygame.image.load('resources/cabinInterior.png')
mbushes = pygame.image.load('resources/mansionbushes.png')
pause = pygame.image.load('resources/paused.png')
gravetable = pygame.image.load('resources/graveyardtable.png')
cabintable = pygame.image.load('resources/cabintable.png')
uphester = pygame.image.load('resources/uphester.png')
childstill = pygame.image.load('resources/childstill.png')
npcstill = pygame.image.load('resources/npc2still.png')
npc2still = pygame.image.load('resources/npcstill.png')
boystill = pygame.image.load('resources/boystill.png')
cabintrees = pygame.image.load('resources/cabinexteriortrees.png')
pearl = pygame.image.load('resources/Pearl.png')
mansiontable = pygame.image.load('resources/mansiontable.png')
market = pygame.image.load('resources/market.png')
dock = pygame.image.load('resources/dock.png')
prison = pygame.image.load('resources/prison.png')
marketman = pygame.image.load('resources/extraman.png')
gamemap = [gravehouseexterior, town, mansionexterior, forest, darkforest, cabinexterior, ghouseenter, ghousebed, ghouseoffice, hesterhouse, market, dock, prison, mansioninterior]

#normalmusic = pygame.mixer.music.load('resources/Purple Planet Music - Atmospheric - Space Harmony.mp3')
#startmusic = pygame.mixer.music.load('resources/Purple Planet Music - Cinematic - Battle Plan.mp3')
#platformmusic = pygame.mixer.music.load('resources/Purple Planet Music - Creepy - Impending Doom.mp3')
#darkforestmusic = pygame.mixer.music.load('resources/Purple Planet Music - Creepy - Lurking Fear.mp3')
#hesterhomemusic = pygame.mixer.music.load('resources/Purple Planet Music - Chilled - Black Coffee.mp3')
walking = pygame.mixer.Sound('resources/Walking On Gravel-SoundBible.com-2023303198.wav')

randomkiddialouges = ["Hey look it's the scary woman.", "My Mommy told me to stay away from you. Are you a bad person?",
                      "What are you doing here, aren't you supposed to be in jail?", "Why did they let you live?"]

randomdimmesdalekiddialouge = ["Good morning Mr. Dimmesdale!", "My mommy said you talk to god, is that true?",
                               "Hello sir, what are you doing here?", "Woah look it's Minitser Dimmesdale!"]

pygame.display.set_caption("Scarlet Letter")

clock = pygame.time.Clock()

def hester(x, y, action, tick):
    #disp.blit(Hester, (x, y))
    if action == "standstill":
        disp.blit(Hester, (x, y))
    elif action == "moveright":
        disp.blit(HesterRight[tick], (x, y))
    elif action == "moveleft":
        disp.blit(HesterLeft[tick], (x, y))
    elif action == "moveup":
        disp.blit(uphester, (x, y))

def dimmesdale(x, y, action, tick):
    if action == "standstill":
        disp.blit(Dimmesdale, (x, y))
    elif action == "moveright":
        disp.blit(DimmesdaleRight[tick], (x, y))
    elif action == "moveleft":
        disp.blit(DimmesdaleLeft[tick], (x, y))
    elif action == "moveup":
        disp.blit(updimmesdale, (x, y))

def hesterdynamicdialouge(msg):
    dialouge(msg)
    text = pygame.font.SysFont("Times New Roman", 20)
    textr = text.render("CHOICE 1 (press 1): Everything is horrible, I wish we could just run away!", True, white)
    texttwor = text.render("CHOICE 2 (press 2): I feel like an outcast in this town, everyone constantly avoids me.", True, white)
    disp.blit(textr, (10, 480))
    disp.blit(texttwor, (10, 501))
    pygame.display.update()

def dimmesdaledynamicdialouge(msg):
    dialouge(msg)
    text = pygame.font.SysFont("Times New Roman", 20)
    textr = text.render("CHOICE 1 (press 1): The guilt it unbearable, everyone I see makes me feel horrible!", True, white)
    texttwor = text.render("CHOICE 2 (press 2): No one knows who I really am, they can't see past my label of Minister.", True, white)
    disp.blit(textr, (10, 480))
    disp.blit(texttwor, (10, 501))
    pygame.display.update()

def pearlnpc(x, y, action):
    if action == "standstill":
        disp.blit(pearl, (x, y))

def marketnpc(x, y, action):
    if action == "standstill":
        disp.blit(marketman, (x, y))

#button("play_hester", 150, 450, 170, 80, red, dark_red, "Hester")
def button(text, x, y, w, h, ic, ac, Action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    xw = x + w
    yh = y + h

    pygame.draw.rect(disp, ic, (x, y, w, h))

    if xw > mouse[0] > x:
        if yh > mouse[1] > y:
            pygame.draw.rect(disp, ac, (x, y, w, h))
            if click[0] == 1 and Action != None:
                if Action == "play_hester":
                    hester_loop()
                elif Action == "play_dimmesdale":
                    dimmesdale_loop()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                hester_loop()
            elif event.key == pygame.K_d:
                dimmesdale_loop()

    small_text_hester = pygame.font.SysFont("Old English Five", 30)
    shtext = small_text_hester.render(text, True, black)
    small_text_dimmesdale = pygame.font.SysFont("Old English Five", 23)
    sdtext = small_text_dimmesdale.render(text, True, black)

    if Action == "play_dimmesdale":
        disp.blit(sdtext, (510, 470))
    elif Action == "play_hester":
        disp.blit(shtext, (175, 463))

def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()

def display_message(text):
    large_text = pygame.font.Font("freesansbold.ttf", 108)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((display_width / 2), (display_height / 2))
    disp.blit(text_surf, text_rect)

    pygame.display.update()

def dialouge(msg):
    message = ""
    dessage = ""
    for i in range(0, len(msg)):
        if i <= 90:
            message += msg[i]
        else:
            dessage += msg[i]
        text = pygame.font.SysFont("Times New Roman", 20)
        textr = text.render(message, True, white)
        texttwor = text.render(dessage, True, white)

        pygame.draw.rect(disp, black, [0, 400, 800, 200])
        disp.blit(textr, (10, 410))
        if len(msg) > 91:
            disp.blit(texttwor, (10, 431))
        pygame.display.update()
        time.sleep(0.05)

def tinydialouge(msg):
    message = ""
    dessage = ""
    for i in range(0, len(msg)):
        if i <= 36:
            message += msg[i]
        else:
            dessage += msg[i]
        text = pygame.font.SysFont("Times New Roman", 16)
        textr = text.render(message, True, white)
        texttwor = text.render(dessage, True, white)

        pygame.draw.rect(disp, black, [0, 150, 300, 300])
        disp.blit(textr, (10, 160))
        if len(msg) > 36:
            disp.blit(texttwor, (10, 177))
        pygame.display.update()
        time.sleep(0.05)

def npc(x, y, action):
    if action == "standstill":
        disp.blit(npcstill, (x, y))

def jailman(x, y, action):
    if action == "standstill":
        disp.blit(npc2still, (x, y))

def childnpc(x, y, action):
    if action == "standstill":
        disp.blit(childstill, (x, y))

def winthropnpc(x, y, action):
    if action == "standstill":
        disp.blit(winthrop, (x, y))

def boynpc(x, y, action):
    if action == "standstill":
        disp.blit(boystill, (x, y))

def start_menu():
    intromusic = 0

    intro = True

    while intro == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        #eufm10.ttf
        #disp.fill(white)
        disp.blit(start, (0, 0))

        intromusic += 1

        if intromusic == 1:
            pygame.mixer.music.load('resources/Purple Planet Music - Cinematic - Battle Plan.mp3')
            pygame.mixer.music.play(3, 0.0)
            pygame.mixer.music.set_volume(1.0)

        large_text = pygame.font.SysFont("Old English Five", 30)
        ltext = large_text.render("Choose a character to play as:", True, black)
        disp.blit(ltext, (160, 380))

        #pygame.display.update()

        button("Hester", 150, 450, 170, 80, red, dark_red, "play_hester")
        button("Dimmesdale", 500, 450, 170, 80, red, dark_red, "play_dimmesdale")

        pygame.display.update()
        clock.tick(60)

def dimmesdale_loop():
    dimmesdale_x = 10
    dimmesdale_y = 235
    dx_change = 0
    #dx_change = 0
    dy_change = 0
    #dy_change = 0
    daction = "standstill"

    hester_x = 300
    hester_y = 255

    hx_change = 0
    hy_change = 0

    npc_x = 450
    npc_y = 235

    towndialouge = 0
    childdialouge = 0
    gravehousedialouge = 0

    dimmesdale_x = 300
    dimmesdale_y = 255

    child_x = 600
    child_y = 255

    boy_x = 300
    boy_y = 255

    jailman_x = random.randint(0, 700)
    jailman_y = random.randint(120, 600)

    marketman_x = 358
    marketman_y = 376

    pearl_x = 10
    pearl_y = 20

    winthrop_x = 200
    winthrop_y = 300

    wx_change = 0
    wy_change = 0

    px_change = 0
    py_change = 0

    jx_change = 0
    jy_change = 0

    bx_change = 0
    by_change = 0

    cx_change = 0
    cy_change = 0

    nx_change = 0
    ny_change = 0

    mx_change = 0
    my_change = 0

    placeholder = 1

    meatdialouge = 0
    fishdialouge = 0
    clothesdialouge = 0
    dimmesdaledialouge = 0
    winthropdialouge = 0

    dtick = 2
    dchange = 1

    walk = False

    nmusic = 0
    dmusic = 0

    z = 0

    tick = 0

    playing = True

    while playing:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    walk = True
                    dx_change = 4
                    daction = "moveright"
                elif event.key == pygame.K_LEFT:
                    walk = True
                    dx_change = -4
                    daction = "moveleft"
                elif event.key == pygame.K_DOWN:
                    walk = True
                    dy_change = 4
                elif event.key == pygame.K_UP:
                    walk = True
                    dy_change = -4
                    daction = "moveup"
                if event.key == pygame.K_ESCAPE:
                    start_menu()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    walk = False
                    dtick = 2
                    dx_change = 0
                    daction = "standstill"
                elif event.key == pygame.K_LEFT:
                    walk = False
                    dtick = 2
                    dx_change = 0
                    daction = "standstill"
                elif event.key == pygame.K_DOWN:
                    walk = False
                    dtick = 2
                    dy_change = 0
                    daction = "standstill"
                elif event.key == pygame.K_UP:
                    walk = False
                    dtick = 2
                    dy_change = 0
                    daction = "standstill"

        if dtick >= 4:
            dchange = -0.12
        elif dtick <= 0:
            dchange = 0.12

        dtick += dchange

        if walk == True:
            walking.play()
            walking.set_volume(0.2)
        else:
            walking.stop()

        dimmesdale_y += dy_change
        dimmesdale_x += dx_change

        if placeholder != 5 and placeholder != 4 and placeholder != 0 and placeholder != 11:
            nmusic += 1
        else:
            nmusic = 0
        if placeholder == 4:
            dmusic += 1
        else:
            dmusic = 0

        if placeholder != 5 and placeholder != 4 and placeholder != 0 and placeholder != 11 and nmusic == 1:
            pygame.mixer.music.load('resources/Purple Planet Music - Atmospheric - Space Harmony.mp3')
            pygame.mixer.music.play(3, 0.0)
            pygame.mixer.music.set_volume(1.0)

        if placeholder == 4 and dmusic == 1:
            pygame.mixer.music.load('resources/Purple Planet Music - Creepy - Lurking Fear.mp3')
            pygame.mixer.music.play(3, 0.0)
            pygame.mixer.music.set_volume(1.0)

        #gamemap = [0 gravehouseexterior, 1 town, 2 mansionexterior, 3 forest, 4 darkforest, 5 cabinexterior, 6 ghouseenter, 7 ghousebed, 8 ghouseoffice, 9 hesterhouse, 10 market, 11 dock, 12 prison, 13 mansioninterior]
        if placeholder == 1 and dimmesdale_x > 764:
            dimmesdale_x = 0
            placeholder = 3
        elif placeholder == 11 and dimmesdale_y < 0:
            dimmesdale_y = 500
            placeholder = 10
        elif placeholder == 12 and dimmesdale_y > 500:
            dimmesdale_y = 0
            dimmesdale_x = 550
            placeholder = 1
        elif placeholder == 2 and 558 < dimmesdale_x < 630 and dimmesdale_y <= 196:
            dimmesdale_y = 468
            dimmesdale_x = 274
            screen = pygame.display.set_mode((580, 580))
            pygame.display.flip()
            placeholder = 13
        elif placeholder == 13 and dimmesdale_y > 480:
            dimmesdale_x = 580
            dimmesdale_y = 200
            screen = pygame.display.set_mode((800, 600))
            pygame.display.flip()
            placeholder = 2
        elif placeholder == 1 and dimmesdale_x <= 0:
            dimmesdale_x = 764
            placeholder = 10
        elif placeholder == 1 and 538 < dimmesdale_x < 566 and dimmesdale_y <= 1:
            dimmesdale_y = 500
            placeholder = 12
        elif placeholder  == 10 and dimmesdale_y >= 500:
            dimmesdale_y = 1
            placeholder = 11
        elif placeholder == 10 and dimmesdale_x > 764:
            placeholder = 1
            dimmesdale_x = 0
        elif dimmesdale_x > 700 and placeholder == 3:
            if dx_change > 0:
                dx_change = 0
        elif placeholder == 3 and dimmesdale_y < 0:
            placeholder = 5
            dimmesdale_y = 600
        elif placeholder == 5 and dimmesdale_y > 600:
            placeholder = 3
            dimmesdale_y = 0
        elif placeholder == 4 and dimmesdale_y < 0:
            placeholder = 3
            dimmesdale_y = 600
        elif placeholder == 1 and dimmesdale_y > 600:
            placeholder = 2
            dimmesdale_y = 0
        elif placeholder == 2 and dimmesdale_y < 0:
            placeholder = 1
            dimmesdale_y = 600
        elif placeholder == 3 and dimmesdale_y > 600:
            placeholder = 4
            dimmesdale_y = 0
        elif placeholder == 3 and dimmesdale_x < 0:
            placeholder = 1
            dimmesdale_x = 764
        #for next map set
        #elif placeholder == 1 and dimmesdale_x < 0:
            #dimmesdale_x = 764
            #placeholder =
        elif placeholder == 1 and dimmesdale_y < 0:
            dimmesdale_y = 500
            placeholder = 0
        elif placeholder == 0 and dimmesdale_y > 500:
            dimmesdale_y = 0
            placeholder = 1
        elif dimmesdale_y < 200 and placeholder == 0 and dimmesdale_x > 184 and dimmesdale_x < 220:
            placeholder = 6
            dimmesdale_y = 147
            screen = pygame.display.set_mode((300, 249))
            pygame.display.flip()
        elif placeholder == 6 and dimmesdale_x > 50 and dimmesdale_x < 78 and dimmesdale_y < 4:
            placeholder = 7
            dimmesdale_y = 149
        elif placeholder == 7 and dimmesdale_y > 149:
            placeholder = 6
            dimmesdale_y = 4
            dimmesdale_x = 62
        elif placeholder == 6 and dimmesdale_x > 175 and dimmesdale_x < 210 and dimmesdale_y < 4:
            placeholder = 8
            dimmesdale_y = 149
        elif placeholder == 8 and dimmesdale_y > 149:
            placeholder = 6
            dimmesdale_x = 182
            dimmesdale_y = 4
        elif dimmesdale_y > 159 and placeholder == 6:
            placeholder = 0
            dimmesdale_y = 200
            dimmesdale_x = 203
            screen = pygame.display.set_mode((800, 600))
            pygame.display.flip()
        elif placeholder == 5 and dimmesdale_y < 150 and dimmesdale_x > 180 and dimmesdale_x < 220:
            placeholder = 9
            dimmesdale_y = 92
            dimmesdale_x = 56
            screen = pygame.display.set_mode((300, 195))
            pygame.display.flip()
        elif placeholder == 9 and dimmesdale_y > 92:
            placeholder = 5
            dimmesdale_y = 150
            dimmesdale_x = 200
            screen = pygame.display.set_mode((800, 600))
            pygame.display.flip()

        #collision detectors for images
        if placeholder == 7 or placeholder == 6 or placeholder == 8 or placeholder == 9:
            if dimmesdale_x > 264 and dx_change > 0:
                dx_change = 0
            if dimmesdale_y > 249 and dy_change > 0:
                dy_change = 0
            if dimmesdale_x < 0 and dx_change < 0:
                dx_change = 0
        elif placeholder == 13:
            if dimmesdale_x >= 536 and dx_change > 0:
                dx_change = 0

        else:
            if dimmesdale_x > 764 and dx_change > 0:
                dx_change = 0
            if dimmesdale_x < 0 and dx_change < 0:
                dx_change = 0
            if dimmesdale_y > 600 and dy_change > 0:
                dy_change = 0
            if dimmesdale_y < 0 and dy_change < 0:
                dy_change = 0
            if npc_x > 764 and nx_change > 0:
                nx_change = random.randint(-1, 0)
            if npc_x < 0 and nx_change < 0:
                nx_change = random.randint(0, 1)
            if npc_y > 600 and ny_change > 0:
                ny_change = random.randint(-1, 0)
            if npc_y < 0 and ny_change < 0:
                ny_change = random.randint(0, 1)
            if child_x > 800 and cx_change > 0:
                cx_change = random.randint(-1, 0)
            if child_x < 0 and cx_change < 0:
                cx_change = random.randint(0, 1)
            if child_y > 600 and cy_change > 0:
                cy_change = random.randint(-1, 0)
            if child_y < 0 and cy_change < 0:
                cy_change = random.randint(0, 1)
            if boy_x > 764 and bx_change > 0:
                bx_change = random.randint(-1, 0)
            if boy_x < 0 and bx_change < 0:
                bx_change = random.randint(0, 1)
            if boy_y > 600 and by_change > 0:
                by_change = random.randint(-1, 0)
            if boy_y < 0 and by_change < 0:
                by_change = random.randint(0, 1)

        #collision detection in graveyard exterior
        if placeholder == 0:
            bx_change = 0
            by_change = 0
            cx_change = 0
            cy_change = 0
            nx_change = 0
            ny_change = 0
            px_change = 0
            py_change = 0
            jx_change = 0
            jy_change = 0
            mx_change = 0
            my_change = 0
            wx_change = 0
            wy_change = 0
            if dimmesdale_x >= 216 and dx_change > 0:
                dx_change = 0
            if dimmesdale_x <= 190 and dx_change < 0:
                dx_change = 0

        #collision detection in town
        if placeholder == 1:
            bx_change = 0
            by_change = 0
            cx_change = 0
            cy_change = 0
            px_change = 0
            py_change = 0
            jx_change = 0
            jy_change = 0
            mx_change = 0
            my_change = 0
            wx_change = 0
            wy_change = 0
            hx_change = 0
            hy_change = 0
            if dimmesdale_x - 60 < npc_x < dimmesdale_x + 60 and dimmesdale_y - 60 < npc_y < dimmesdale_y + 60:
                if npc_x < dimmesdale_x and tick % 10 == 0:
                    nx_change = 1.2
                elif npc_x > dimmesdale_x and tick % 10 == 0:
                    nx_change = -1.2
                if npc_y > dimmesdale_y and tick % 10 == 0:
                    ny_change = -1.2
                if npc_y < dimmesdale_y and tick % 10 == 0:
                    ny_change = 1.2
            if dimmesdale_y < 212:
                if -10 <= dimmesdale_x < 189 and dy_change < 0:
                    dy_change = 0
                if dimmesdale_x < 189 and dx_change < 0:
                    dx_change = 0
                if 540 >= dimmesdale_x >= 216 and dx_change != 0:
                    dx_change = 0 #224 532
                if 224 < dimmesdale_x < 532 and dy_change < 0:
                    dy_change = 0
                if dimmesdale_x > 564 and dx_change > 0:
                    dx_change = 0
                if dimmesdale_x > 564 and dy_change < 0:
                    dy_change = 0
            if dimmesdale_y > 267:
                if dimmesdale_x < 148 and dy_change > 0:
                    dy_change = 0
                if 176 < dimmesdale_x < 356 and dy_change > 0:
                    dy_change = 0
                if 380 < dimmesdale_x < 592 and dy_change > 0:
                    dy_change = 0
                if dimmesdale_x > 620 and dy_change > 0:
                    dy_change = 0
                if 148 > dimmesdale_x and dx_change < 0:
                    dx_change = 0
                if 176 < dimmesdale_x < 356 and dx_change != 0:
                    dx_change = 0
                if 380 < dimmesdale_x < 592 and dx_change != 0:
                    dx_change = 0
                if dimmesdale_x > 620 and dx_change > 0:
                    dx_change = 0
            #npc collision
            if npc_y < 212:
                if -10 <= npc_x < 189 and ny_change < 0:
                    ny_change = random.randint(0, 1)
                if npc_x < 189 and nx_change < 0:
                    nx_change = random.randint(0, 1)
                if 540 >= npc_x >= 216 and nx_change != 0:
                    nx_change = random.randint(-1, 1)
                if 224 < npc_x < 532 and ny_change < 0:
                    ny_change = random.randint(0, 1)
                if npc_x > 564 and nx_change > 0:
                    nx_change = random.randint(-1, 0)
                if npc_x > 564 and ny_change < 0:
                    ny_change = random.randint(0, 1)
            if npc_y > 267:
                if npc_x < 148 and ny_change > 0:
                    ny_change = random.randint(-1, 0)
                if 176 < npc_x < 356 and ny_change > 0:
                    ny_change = random.randint(-1, 0)
                if 380 < npc_x < 592 and ny_change > 0:
                    ny_change = random.randint(-1, 0)
                if npc_x > 620 and ny_change > 0:
                    ny_change = random.randint(-1, 0)
                if 148 > npc_x and nx_change < 0:
                    nx_change = random.randint(0, 1)
                if 176 < npc_x < 356 and nx_change != 0:
                    nx_change = random.randint(-1, 1)
                if 380 < npc_x < 592 and nx_change != 0:
                    nx_change = random.randint(-1, 1)
                if npc_x > 620 and nx_change > 0:
                    nx_change = random.randint(-1, 0)

        #collision detection in governors square place outside mansion
        if placeholder == 2:
            bx_change = 0
            by_change = 0
            cx_change = 0
            cy_change = 0
            nx_change = 0
            ny_change = 0
            px_change = 0
            py_change = 0
            jx_change = 0
            jy_change = 0
            mx_change = 0
            my_change = 0
            wx_change = 0
            wy_change = 0
            hx_change = 0
            hy_change = 0
            if dimmesdale_x <= 352 and dx_change < 0:
                dx_change = 0
            if dimmesdale_y <= 200:
                if dimmesdale_x >= 384 and dx_change > 0:
                    dx_change = 0
            if dimmesdale_y >= 256 and dy_change > 0:
                dy_change = 0
            if dimmesdale_x >= 644 and dx_change > 0:
                dx_change = 0
            if 384 < dimmesdale_x < 644:
                if dimmesdale_y < 200 and dy_change < 0:
                    dy_change = 0

        #collision detection in forest
        if placeholder == 3:
            ny_change = 0
            nx_change = 0
            px_change = 0
            py_change = 0
            jx_change = 0
            jy_change = 0
            mx_change = 0
            my_change = 0
            wx_change = 0
            wy_change = 0
            if dimmesdale_x - 60 < child_x < dimmesdale_x + 60 and dimmesdale_y - 60 < child_y < dimmesdale_y + 60:
                if child_x < dimmesdale_x:
                    cx_change = 1.2
                elif child_x > dimmesdale_x:
                    cx_change = -1.2
                if child_y > dimmesdale_y:
                    cy_change = -1.2
                if child_y < dimmesdale_y:
                    cy_change = 1.2
            if dimmesdale_x - 60 < boy_x < dimmesdale_x + 60 and dimmesdale_y - 60 < boy_y < dimmesdale_y + 60:
                if boy_x < dimmesdale_x:
                    bx_change = 1.2
                elif boy_x > dimmesdale_x:
                    bx_change = -1.2
                if boy_y > dimmesdale_y:
                    by_change = -1.2
                if boy_y < dimmesdale_y:
                    by_change = 1.2
            if dimmesdale_x <= 436 or dimmesdale_x >= 472:
                if dimmesdale_y <= 207 and dy_change < 0:
                    dy_change = 0
                if dimmesdale_y >= 271 and dy_change > 0:
                    dy_change = 0
            if dimmesdale_y < 207 or dimmesdale_y > 271:
                if dimmesdale_x >= 471 and dx_change > 0:
                    dx_change = 0
                if dimmesdale_x <= 436 and dx_change < 0:
                    dx_change = 0
            #child collision
            if child_x <= 436 or child_x >= 472:
                if child_y <= 241 and cy_change < 0:
                    cy_change = random.randint(0, 1)
                if child_y >= 305 and cy_change > 0:
                    cy_change = random.randint(-1, 0)
            if child_y < 241 or child_y > 305:
                if child_x >= 471 and cx_change > 0:
                    cx_change = random.randint(-1, 0)
                if child_x <= 436 and cx_change < 0:
                    cx_change = random.randint(0, 1)
            if child_y <= 0 and cy_change != 0:
                cy_change = random.randint(0, 1)
            if child_y >= 480 and cy_change > 0:
                cy_change = random.randint(-1, 0)
            if child_x > 550 and cx_change != 0:
                cx_change = random.randint(-1, 0)
            if child_x <= 20 and cx_change != 0:
                cx_change = random.randint(0, 1)
            #boy collision
            if boy_x <= 436 or boy_x >= 472:
                if boy_y <= 241 and by_change < 0:
                    by_change = random.randint(0, 1)
                if boy_y >= 305 and by_change > 0:
                    by_change = random.randint(-1, 0)
            if boy_y < 241 or boy_y > 305:
                if boy_x >= 471 and bx_change > 0:
                    bx_change = random.randint(-1, 0)
                if boy_x <= 436 and bx_change < 0:
                    bx_change = random.randint(0, 1)
            if boy_y <= 0 and by_change != 0:
                by_change = random.randint(0, 1)
            if boy_y >= 480 and by_change > 0:
                by_change = random.randint(-1, 0)
            if boy_x > 550 and bx_change != 0:
                bx_change = random.randint(-1, 0)
            if boy_x <= 20 and bx_change != 0:
                bx_change = random.randint(0, 1)
            #dimmesdale collision
            if hester_x <= 436 or hester_x >= 472:
                if hester_y <= 207 and hy_change < 0:
                    hy_change = random.randint(0, 1)
                if hester_y >= 271 and hy_change > 0:
                    hy_change = random.randint(-1, 0)
            if hester_y < 207 or hester_y > 305:
                if hester_x >= 471 and hx_change > 0:
                    hx_change = random.randint(-1, 0)
                if hester_x <= 436 and hx_change < 0:
                    hx_change = random.randint(0, 1)
            if hester_y <= 0 and hy_change != 0:
                hy_change = random.randint(0, 1)
            if hester_y >= 480 and hy_change > 0:
                hy_change = random.randint(-1, 0)
            if hester_x > 550 and hx_change != 0:
                hx_change = random.randint(-1, 0)
            if hester_x <= 20 and hx_change != 0:
                hx_change = random.randint(0, 1)

        #collision detection in outside dimmesdales house
        if placeholder == 5:
            bx_change = 0
            by_change = 0
            cx_change = 0
            cy_change = 0
            nx_change = 0
            ny_change = 0
            px_change = 0
            py_change = 0
            jx_change = 0
            jy_change = 0
            mx_change = 0
            my_change = 0
            wx_change = 0
            wy_change = 0
            hx_change = 0
            hy_change = 0
            if z == 0:
                z = 1
            if dimmesdale_x >= 468 and dx_change > 0:
                dx_change = 0
            if dimmesdale_x <= 440 and dimmesdale_y >= 280 and dx_change < 0:
                dx_change = 0
            if 184 <= dimmesdale_x <= 404:
                if dimmesdale_y >= 280 and dy_change > 0:
                    dy_change = 0
            if dimmesdale_x < 188 and dx_change < 0:
                dx_change = 0
            if dimmesdale_x >= 212 and dimmesdale_y <= 224 and dy_change < 0:
                dy_change = 0
            if dimmesdale_y < 224 and dimmesdale_x > 216 and dx_change > 0:
                dx_change = 0

        #collision detection in graveyard house
        # DONT HAVE COLLISION DETECTION IN HERE JUST SEND HER STRAIGHT OUT OF THE HOUSE
        if placeholder == 6:
            bx_change = 0
            by_change = 0
            cx_change = 0
            cy_change = 0
            nx_change = 0
            ny_change = 0
            px_change = 0
            py_change = 0
            jx_change = 0
            jy_change = 0
            mx_change = 0
            my_change = 0
            wx_change = 0
            wy_change = 0
            hx_change = 0
            hy_change = 0
        '''if placeholder == 6:
            bx_change = 0
            by_change = 0
            cx_change = 0
            cy_change = 0
            nx_change = 0
            ny_change = 0
            px_change = 0
            py_change = 0
            if 28 <= dimmesdale_x <= 104:
                if dimmesdale_y >= 63 and dy_change >= 0:
                    dy_change = 0
            if dimmesdale_y >= 83 and dx_change != 0 and 136 >= dimmesdale_x >= 4:
                dx_change = 0
            if 75 >= dimmesdale_y >= 59:
                if 119 >= dimmesdale_x >= 23 and dx_change != 0:
                    dx_change = 0
            if dimmesdale_y <= 0 and dy_change < 0:
                dy_change = 0'''

        #collision detection in dimmesdales cabin
        if placeholder == 9:
            bx_change = 0
            by_change = 0
            cx_change = 0
            cy_change = 0
            nx_change = 0
            ny_change = 0
            jx_change = 0
            jy_change = 0
            mx_change = 0
            my_change = 0
            wx_change = 0
            wy_change = 0
            hx_change = 0
            hy_change = 0
            if 168 <= dimmesdale_x <= 300:
                if dimmesdale_y > 56 and dx_change != 0:
                    dx_change = 0
            if 46 <= dimmesdale_y <= 56:
                if 188 <= dimmesdale_x <= 300 and dx_change != 0:
                    dx_change = 0
            if 188 <= dimmesdale_x <= 300:
                if dimmesdale_y >= 40 and dy_change > 0:
                    dy_change = 0
            if dimmesdale_y <= 0 and dy_change < 0:
                dy_change = 0
            #collision detection pearl 300 195
            if pearl_y >= 140 and py_change > 0:
                py_change = random.randint(-1, 0)
            if pearl_x >= 262 and px_change > 0:
                px_change = random.randint(0, 1)
            if 168 <= pearl_x <= 300:
                if pearl_y > 56 and px_change != 0:
                    px_change = random.randint(-1, 1)
            if 46 <= pearl_y <= 56:
                if 188 <= pearl_x <= 300 and px_change != 0:
                    px_change = random.randint(-1, 1)
            if 188 <= pearl_x <= 300:
                if pearl_y >= 40 and py_change > 0:
                    py_change = random.randint(-1, 0)
            if pearl_y <= 0 and py_change < 0:
                py_change = random.randint(0, 1)
            if pearl_x <= 0 and px_change < 0:
                px_change = random.randint(0, 1)

        #detection in market
        if placeholder == 10:
            bx_change = 0
            by_change = 0
            cx_change = 0
            cy_change = 0
            nx_change = 0
            ny_change = 0
            wx_change = 0
            wy_change = 0
            hx_change = 0
            hy_change = 0
            if dimmesdale_x - 60 < marketman_x < dimmesdale_x + 60 and dimmesdale_y - 60 < marketman_y < dimmesdale_y + 60:
                if marketman_x < dimmesdale_x:
                    mx_change = 1.2
                elif marketman_x > dimmesdale_x:
                    mx_change = -1.2
                if marketman_y > dimmesdale_y:
                    my_change = -1.2
                if marketman_y < dimmesdale_y:
                    my_change = 1.2
            if dimmesdale_x >= 378:
                if dimmesdale_y >= 267 and dy_change > 0:
                    dy_change = 0
                if dimmesdale_y <= 207 and dy_change < 0:
                    dy_change = 0
            if dimmesdale_y >= 17:
                if dimmesdale_x <= 339 and dx_change < 0:
                    dx_change = 0
            if dimmesdale_y < 17:
                if dimmesdale_x >= 460 and dx_change != 0:
                    dx_change = 0
                if dimmesdale_x <= 264 and dx_change != 0:
                    dx_change = 0
                if dimmesdale_x >= 378:
                    if dimmesdale_y >= 11 and dy_change > 0:
                        dy_change = 0
                if dimmesdale_x <= 339:
                    if dimmesdale_y >= 11 and dy_change > 0:
                        dy_change = 0
            if 35 <= dimmesdale_y <= 203:
                if dimmesdale_x >= 368 and dx_change > 0:
                    dx_change = 0
            if dimmesdale_y >= 271:
                if dimmesdale_x >= 368 and dx_change > 0:
                    dx_change = 0
            #market man collision
            if marketman_x >= 378:
                if marketman_y >= 267 and my_change > 0:
                    my_change = random.randint(-1, 0)
                if marketman_y <= 207 and my_change < 0:
                    my_change = random.randint(0, 1)
            if marketman_y >= 17:
                if marketman_x <= 339 and mx_change < 0:
                    mx_change = random.randint(0, 1)
            if marketman_y < 17 and my_change < 0:
                my_change = random.randint(0, 1)
            if 35 <= marketman_y <= 203:
                if marketman_x >= 368 and mx_change > 0:
                    mx_change = random.randint(-1, 0)
            if marketman_y >= 271:
                if marketman_x >= 368 and mx_change > 0:
                    mx_change = random.randint(-1, 0)
            if marketman_y  >= 500 and my_change != 0:
                my_change = random.randint(-1, 0)
            if marketman_x >= 766 and mx_change > 0:
                mx_change = random.randint(-1, 0)




        #detection in jail
        if placeholder == 12:
            bx_change = 0
            by_change = 0
            cx_change = 0
            cy_change = 0
            nx_change = 0
            ny_change = 0
            mx_change = 0
            my_change = 0
            wx_change = 0
            wy_change = 0
            hx_change = 0
            hy_change = 0
            if dimmesdale_x - 60 < jailman_x < dimmesdale_x + 60 and dimmesdale_y - 60 < jailman_y < dimmesdale_y + 60:
                if jailman_x < dimmesdale_x:
                    jx_change = 1.2
                elif jailman_x > dimmesdale_x:
                    jx_change = -1.2
                if jailman_y > dimmesdale_y:
                    jy_change = -1.2
                if jailman_y < dimmesdale_y:
                    jy_change = 1.2
                if dimmesdale_y <= 116 and dy_change < 0:
                    dy_change = 0
            #jailman collision
            if jailman_y <= 116 and jy_change < 0:
                jy_change = random.randint(0, 1)
            if jailman_x <= 0 and jx_change < 0:
                jx_change = random.randint(0, 1)
            if jailman_x >= 764 and jx_change > 0:
                jx_change = random.randint(-1, 0)
            if jailman_y >= 500 and jy_change > 0:
                jy_change = random.randint(0, 1)

        #detection in mansion interior
        if placeholder == 13:
            bx_change = 0
            by_change = 0
            cx_change = 0
            cy_change = 0
            nx_change = 0
            ny_change = 0
            mx_change = 0
            my_change = 0
            hx_change = 0
            hy_change = 0
            if 416 <= dimmesdale_y <= 428:
                if 74 <= dimmesdale_x <= 174 and dx_change != 0:
                    dx_change = 0
            if 74 <= dimmesdale_x <= 168 and 406 <= dimmesdale_y <= 412 and dy_change > 0:
                dy_change = 0
            if dimmesdale_y >= 428 and 54 <= dimmesdale_x <= 190 and dx_change != 0:
                dx_change = 0
            if dimmesdale_x >= 296 and dimmesdale_y <= 120 and dy_change < 0:
                dy_change = 0
                if dx_change > 0:
                    dx_change = 0
            if dimmesdale_y <= 76 and dy_change < 0:
                dy_change = 0
            #winthrop collision detection
            if 416 <= winthrop_y <= 428:
                if 74 <= winthrop_x <= 174 and wx_change != 0:
                    wx_change = random.randint(-1, 1)
            if 74 <= winthrop_x <= 168 and 406 <= winthrop_y <= 412 and wy_change > 0:
                wy_change = random.randint(-1, 0)
            if winthrop_y >= 428 and 54 <= winthrop_x <= 190 and wx_change != 0:
                wx_change = random.randint(-1, 1)
            if winthrop_x >= 296 and winthrop_y <= 120 and wy_change < 0:
                wy_change = random.randint(0, 1)
                if wx_change > 0:
                    wx_change = random.randint(-1, 0)
            if winthrop_y <= 76 and wy_change < 0:
                wy_change = random.randint(0, 1)
            if winthrop_x >= 546 and wx_change != 0:
                wx_change = random.randint(-1, 0)
            if winthrop_y >= 491 and wy_change > 0:
                wy_change = random.randint(-1, 0)
            if winthrop_x <= 0 and wx_change < 0:
                wx_change = random.randint(0, 1)

        naction = "standstill"
        caction = "standstill"
        baction = "standstill"
        paction = "standstill"
        jaction = "standstill"
        maction = "standstill"
        waction = "standstill"
        haction = "standstill"

        tick += 1

        if placeholder != 5 and placeholder != 3 and z == 1:
            z = 2

        if nx_change == 0 and tick % 20 == 0 and placeholder == 1:
            nx_change = random.randint(-1, 1)
        if ny_change == 0 and tick % 20 == 0 and placeholder == 1:
            ny_change = random.randint(-1, 1)

        if cx_change == 0 and tick % 20 == 0 and placeholder == 3:
            cx_change = random.randint(-1, 1)
        if cy_change == 0 and tick % 20 == 0 and placeholder == 3:
            cy_change = random.randint(-1, 1)

        if bx_change == 0 and tick % 20 == 0 and placeholder == 3:
            bx_change = random.randint(-1, 1)
        if by_change == 0 and tick % 20 == 0 and placeholder == 3:
            by_change = random.randint(-1, 1)

        if px_change == 0 and tick % 20 == 0 and placeholder == 9:
            px_change = random.randint(-1, 1)
        if py_change == 0 and tick % 20 == 0 and placeholder == 9:
            py_change = random.randint(-1, 1)

        if jx_change == 0 and tick % 20 == 0 and placeholder == 12:
            jx_change = random.randint(-1, 1)
        if jy_change == 0 and tick % 20 == 0 and placeholder == 12:
            jy_change = random.randint(-1, 1)
        if jy_change != 0 and tick % 100 == 80 and placeholder == 12:
            jy_change = 0
        if jx_change != 0 and tick % 100 == 50 and placeholder == 12:
            jx_change = 0

        if mx_change == 0 and tick % 20 == 0 and placeholder == 10:
            mx_change = random.randint(-1, 1)
        if my_change == 0 and tick % 20 == 0 and placeholder == 10:
            my_change = random.randint(-1, 1)

        if wx_change == 0 and tick % 20 == 0 and placeholder == 13:
            wx_change = random.randint(-1, 1)
        if wy_change == 0 and tick % 20 == 0 and placeholder == 13:
            wy_change = random.randint(-1, 1)

        if hx_change == 0 and tick % 20 == 0 and placeholder == 3:
            hx_change = random.randint(-1, 1)
        if hy_change == 0 and tick % 20 == 0 and placeholder == 3:
            hy_change = random.randint(-1, 1)

        #people love dimmesdale feature

        npc_x += nx_change
        npc_y += ny_change

        child_x += cx_change
        child_y += cy_change

        boy_x += bx_change
        boy_y += by_change

        pearl_x += px_change
        pearl_y += py_change

        jailman_x += jx_change
        jailman_y += jy_change

        marketman_x += mx_change
        marketman_y += my_change

        winthrop_x += wx_change
        winthrop_y += wy_change

        hester_x += hx_change
        hester_y += hy_change

        dlick = int(round(dtick, 0))

        disp.fill(black)
        disp.blit(gamemap[placeholder], (0, 0))
        if placeholder == 1:
            npc(npc_x, npc_y, naction)
        if placeholder == 3 and z != 1:
            childnpc(child_x, child_y, caction)
            boynpc(boy_x, boy_y, baction)
        if placeholder == 3 and z == 1:
            hester(hester_x, hester_y, haction, 2)
        if placeholder == 9:
            pearlnpc(pearl_x, pearl_y, paction)
        if placeholder == 10:
            marketnpc(marketman_x, marketman_y, maction)
        if placeholder == 12:
            jailman(jailman_x, jailman_y, jaction)
        if placeholder == 13:
            winthropnpc(winthrop_x, winthrop_y, waction)

        dlick = int(round(dtick, 0))

        dimmesdale(dimmesdale_x, dimmesdale_y, daction, dlick)

        if placeholder == 2:
            disp.blit(mbushes, (0, 0))
        if placeholder == 5:
            disp.blit(cabintrees, (0, 0))
        if placeholder == 6:
            disp.blit(gravetable, (0, 0))
        if placeholder == 9:
            disp.blit(cabintable, (0, 0))
        if placeholder == 13:
            disp.blit(mansiontable, (0, 0))
        ####################################################################
        #     WHEN dimmesdale IS TALKING WITH ANYONE OTHER THAN DIMMESDALE #
        # SHE SHOULD BE UNABLE TO HAVE FLUID DIALOUGE AND ONLY GIVE SIMPLE #
        #                             PHRASES                              #
        #                                                                  #
        # YOU CAN BARELY TRAVEL WITHOUT PEOPLE BARRATING YOU WITH COMMENTS #
        ####################################################################
        if dimmesdale_x < npc_x < dimmesdale_x + 60 and placeholder == 1 and dimmesdale_y < npc_y < dimmesdale_y + 60:
            if towndialouge == 1:
                dialouge("TOWNSPERSON: Hello there Mr. Dimmesdale, I'm sorry for getting in the way.")
                b = True
                while b == True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            dialouge("DIMMESDALE: It's ok, have a nice day!")
                            b = False

            if towndialouge >= 40:
                dialouge("TOWNSPERSON: Sorry I don't mean to get in the way.")
                b = True
                while b == True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            dialouge("DIMMESDALE: Oh no it's perfectly fine.")
                            b = False

                towndialouge = 2

            towndialouge += 1
        childdialouge += 1
            #nx_change = 3

        if z != 1:
            if placeholder == 3 and childdialouge % 100 == 50 and dimmesdale_x - 50 < child_x < dimmesdale_x + 50 and dimmesdale_y - 50 < child_y < dimmesdale_y + 50:
                a = random.randint(0, 3)
                dialouge("GIRL: " + randomdimmesdalekiddialouge[a])
                time.sleep(1)
            if placeholder == 3 and childdialouge % 100 == 50 and dimmesdale_x - 50 < boy_x < dimmesdale_x + 50 and dimmesdale_y - 50 < boy_y < dimmesdale_y + 50:
                a = random.randint(0, 3)
                dialouge("BOY: " + randomdimmesdalekiddialouge[a])
                time.sleep(1)
        if z == 1:
            if placeholder == 3 and dimmesdaledialouge == 0 and dimmesdale_x - 20 < hester_x < dimmesdale_x + 20 and dimmesdale_y - 20 < hester_y < dimmesdale_y + 20:
                dimmesdaledynamicdialouge("HESTER: Hi Dimmesdale, how have you been?")
                a = True
                while a == True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_1:
                                dialouge("HESTER: I'm surrounded by people, and yet I feel completely alone.")
                                a = False
                            elif event.key == pygame.K_2:
                                dialouge("HESTER: This terrible letter has engulfed my entire personality, people can't even imagine me without it.")
                                a = False
                time.sleep(1)
                dimmesdaledialouge = 1

        if placeholder == 9 and gravehousedialouge == 0:
            tinydialouge("HESTER: What are you doing in my house! Get out before anyone sees you.")
            time.sleep(2)
            dimmesdale_y = 300
            gravehousedialouge = 1

        if placeholder != 10:
            meatdialouge = 0
            clothesdialouge = 0
            fishdialouge = 0

        if placeholder == 10:
            if 700 < dimmesdale_x < 740 and dimmesdale_y <= 207 and meatdialouge == 0:
                dialouge("MEATMAN: What would you like Minister Dimmesdale?")
                time.sleep(1)
                a = True
                while a == True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            dialouge("DIMMESDALE: Oh I'm just browsing.")
                            a = False
                            time.sleep(1)
                dialouge("MEATMAN: Sorry for wasting your time.")
                time.sleep(1)
                meatdialouge = 1
            if 576 < dimmesdale_x < 620 and dimmesdale_y <= 207 and fishdialouge == 0:
                dialouge("FISHMAN: What would you like Minister Dimmesdale?")
                time.sleep(1)
                a = True
                while a == True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            dialouge("DIMMMESDALE: Oh I'm just browsing.")
                            a = False
                            time.sleep(1)
                dialouge("FISHMAN: Sorry for wasting your time.")
                time.sleep(1)
                fishdialouge = 1
            if 444 < dimmesdale_x < 492 and 150 <= dimmesdale_y <= 207 and clothesdialouge == 0:
                dialouge("CLOTHESWOMAN: What would you like Minister Dimmesdale?")
                time.sleep(1)
                a = True
                while a == True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            dialouge("DIMMESDALE: Oh I'm just browsing.")
                            a = False
                            time.sleep(1)
                dialouge("CLOTHESWOMAN: Sorry for wasting your time.")
                time.sleep(1)
                clothesdialouge = 1

        if placeholder == 13 and winthropdialouge == 0 and dimmesdale_x - 20 < winthrop_x < dimmesdale_x + 20 and dimmesdale_y - 20 < winthrop_y < dimmesdale_y + 20:
            dialouge("DIMMESDALE: Hello John, how have you been feeling?")
            time.sleep(1.5)
            dialouge("WINTHROP: Good morning Dimmesdale, I'm not feeling so well.")
            time.sleep(1.5)
            dialouge("DIMMESDALE: I hope that you do get better soon.")
            time.sleep(1.2)
            winthropdialouge = 1

        pygame.display.update()
        clock.tick(60)

def hester_loop():
    hester_x = 10
    dimmesdale_x = 100
    hester_y = 235
    dimmesdale_y = 100
    hx_change = 0
    #dx_change = 0
    hy_change = 0
    #dy_change = 0
    haction = "standstill"

    npc_x = 450
    npc_y = 235

    towndialouge = 0
    childdialouge = 0
    gravehousedialouge = 0

    dimmesdale_x = 300
    dimmesdale_y = 255

    child_x = 600
    child_y = 255

    boy_x = 300
    boy_y = 255

    jailman_x = random.randint(0, 700)
    jailman_y = random.randint(120, 600)

    marketman_x = 358
    marketman_y = 376

    pearl_x = 10
    pearl_y = 20

    winthrop_x = 200
    winthrop_y = 300

    wx_change = 0
    wy_change = 0

    px_change = 0
    py_change = 0

    jx_change = 0
    jy_change = 0

    bx_change = 0
    by_change = 0

    cx_change = 0
    cy_change = 0

    nx_change = 0
    ny_change = 0

    mx_change = 0
    my_change = 0

    dx_change = 0
    dy_change = 0

    placeholder = 1

    meatdialouge = 0
    fishdialouge = 0
    clothesdialouge = 0
    dimmesdaledialouge = 0
    winthropdialouge = 0
    pearldialouge = 0

    htick = 2
    hchange = 1

    walk = False

    nmusic = 0
    dmusic = 0

    z = 0

    tick = 0

    playing = True

    while playing:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    walk = True
                    hx_change = -4
                    haction = "moveleft"
                elif event.key == pygame.K_RIGHT:
                    walk = True
                    hx_change = 4
                    haction = "moveright"
                elif event.key == pygame.K_UP:
                    walk = True
                    hy_change = -4
                    haction = "moveup"
                elif event.key == pygame.K_DOWN:
                    walk = True
                    hy_change = 4
                elif event.key == pygame.K_ESCAPE:
                    start_menu()
                elif event.key == pygame.K_p:
                    p = True

                    while p == True:
                        disp.blit(pause, (0, 0))

                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                p = False

                        pygame.display.update()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    htick = 2
                    walk = False
                    hx_change = 0
                    haction = "standstill"
                elif event.key == pygame.K_RIGHT:
                    htick = 2
                    walk = False
                    hx_change = 0
                    haction = "standstill"
                elif event.key == pygame.K_UP:
                    walk = False
                    hy_change = 0
                    haction = "standstill"
                elif event.key == pygame.K_DOWN:
                    walk = False
                    hy_change =  0
                    haction = "standstill"

        hester_x += hx_change
        hester_y += hy_change

        if htick >= 4:
            hchange = -0.12
        elif htick <= 0:
            hchange = 0.12

        htick += hchange

        if walk == True:
            walking.play()
            walking.set_volume(0.2)
        else:
            walking.stop()

        if placeholder != 5 and placeholder != 4 and placeholder != 0 and placeholder != 11:
            nmusic += 1
        else:
            nmusic = 0
        if placeholder == 4:
            dmusic += 1
        else:
            dmusic = 0

        if placeholder != 5 and placeholder != 4 and placeholder != 0 and placeholder != 11 and nmusic == 1:
            pygame.mixer.music.load('resources/Purple Planet Music - Atmospheric - Space Harmony.mp3')
            pygame.mixer.music.play(3, 0.0)
            pygame.mixer.music.set_volume(1.0)

        if placeholder == 4 and dmusic == 1:
            pygame.mixer.music.load('resources/Purple Planet Music - Creepy - Lurking Fear.mp3')
            pygame.mixer.music.play(3, 0.0)
            pygame.mixer.music.set_volume(1.0)

        #gamemap = [0 gravehouseexterior, 1 town, 2 mansionexterior, 3 forest, 4 darkforest, 5 cabinexterior, 6 ghouseenter, 7 ghousebed, 8 ghouseoffice, 9 hesterhouse, 10 market, 11 dock, 12 prison, 13 mansioninterior]
        if placeholder == 1 and hester_x > 764:
            hester_x = 0
            placeholder = 3
        elif placeholder == 11 and hester_y < 0:
            hester_y = 500
            placeholder = 10
        elif placeholder == 12 and hester_y > 500:
            hester_y = 0
            hester_x = 550
            placeholder = 1
        elif placeholder == 2 and 558 < hester_x < 630 and hester_y <= 196:
            hester_y = 468
            hester_x = 274
            screen = pygame.display.set_mode((580, 580))
            pygame.display.flip()
            placeholder = 13
        elif placeholder == 10 and hester_x > 764:
            hester_x = 0
            placeholder = 1
        elif placeholder == 13 and hester_y > 480:
            hester_x = 580
            hester_y = 200
            screen = pygame.display.set_mode((800, 600))
            pygame.display.flip()
            placeholder = 2
        elif placeholder == 1 and hester_x <= 0:
            hester_x = 764
            placeholder = 10
        elif placeholder == 1 and 538 < hester_x < 566 and hester_y <= 1:
            hester_y = 500
            placeholder = 12
        elif placeholder  == 10 and hester_y >= 500:
            hester_y = 1
            placeholder = 11
        elif hester_x > 700 and placeholder == 3:
            if hx_change > 0:
                hx_change = 0
        elif placeholder == 3 and hester_y < 0:
            placeholder = 5
            hester_y = 600
        elif placeholder == 5 and hester_y > 600:
            placeholder = 3
            hester_y = 0
        elif placeholder == 4 and hester_y < 0:
            placeholder = 3
            hester_y = 600
        elif placeholder == 1 and hester_y > 600:
            placeholder = 2
            hester_y = 0
        elif placeholder == 2 and hester_y < 0:
            placeholder = 1
            hester_y = 600
        elif placeholder == 3 and hester_y > 600:
            placeholder = 4
            hester_y = 0
        elif placeholder == 3 and hester_x < 0:
            placeholder = 1
            hester_x = 764
        #for next map set
        #elif placeholder == 1 and hester_x < 0:
            #hester_x = 764
            #placeholder =
        elif placeholder == 1 and hester_y < 0:
            hester_y = 500
            placeholder = 0
        elif placeholder == 0 and hester_y > 500:
            hester_y = 0
            placeholder = 1
        elif hester_y < 200 and placeholder == 0 and hester_x > 184 and hester_x < 220:
            placeholder = 6
            hester_y = 147
            screen = pygame.display.set_mode((300, 249))
            pygame.display.flip()
        elif placeholder == 6 and hester_x > 50 and hester_x < 78 and hester_y < 4:
            placeholder = 7
            hester_y = 149
        elif placeholder == 7 and hester_y > 149:
            placeholder = 6
            hester_y = 4
            hester_x = 62
        elif placeholder == 6 and hester_x > 175 and hester_x < 210 and hester_y < 4:
            placeholder = 8
            hester_y = 149
        elif placeholder == 8 and hester_y > 149:
            placeholder = 6
            hester_x = 182
            hester_y = 4
        elif hester_y > 159 and placeholder == 6:
            placeholder = 0
            hester_y = 200
            hester_x = 203
            screen = pygame.display.set_mode((800, 600))
            pygame.display.flip()
        elif placeholder == 5 and hester_y < 150 and hester_x > 180 and hester_x < 220:
            placeholder = 9
            hester_y = 92
            hester_x = 56
            screen = pygame.display.set_mode((300, 195))
            pygame.display.flip()
        elif placeholder == 9 and hester_y > 92:
            placeholder = 5
            hester_y = 150
            hester_x = 200
            screen = pygame.display.set_mode((800, 600))
            pygame.display.flip()

        #collision detectors for images
        if placeholder == 7 or placeholder == 6 or placeholder == 8 or placeholder == 9:
            if hester_x > 264 and hx_change > 0:
                hx_change = 0
            if hester_y > 249 and hy_change > 0:
                hy_change = 0
            if hester_x < 0 and hx_change < 0:
                hx_change = 0
        elif placeholder == 13:
            if hester_x >= 536 and hx_change > 0:
                hx_change = 0

        else:
            if hester_x > 764 and hx_change > 0:
                hx_change = 0
            if hester_x < 0 and hx_change < 0:
                hx_change = 0
            if hester_y > 600 and hy_change > 0:
                hy_change = 0
            if hester_y < 0 and hy_change < 0:
                hy_change = 0
            if npc_x > 764 and nx_change > 0:
                nx_change = random.randint(-1, 0)
            if npc_x < 0 and nx_change < 0:
                nx_change = random.randint(0, 1)
            if npc_y > 600 and ny_change > 0:
                ny_change = random.randint(-1, 0)
            if npc_y < 0 and ny_change < 0:
                ny_change = random.randint(0, 1)
            if child_x > 800 and cx_change > 0:
                cx_change = random.randint(-1, 0)
            if child_x < 0 and cx_change < 0:
                cx_change = random.randint(0, 1)
            if child_y > 600 and cy_change > 0:
                cy_change = random.randint(-1, 0)
            if child_y < 0 and cy_change < 0:
                cy_change = random.randint(0, 1)
            if boy_x > 764 and bx_change > 0:
                bx_change = random.randint(-1, 0)
            if boy_x < 0 and bx_change < 0:
                bx_change = random.randint(0, 1)
            if boy_y > 600 and by_change > 0:
                by_change = random.randint(-1, 0)
            if boy_y < 0 and by_change < 0:
                by_change = random.randint(0, 1)

        #collision detection in graveyard exterior
        if placeholder == 0:
            bx_change = 0
            by_change = 0
            cx_change = 0
            cy_change = 0
            nx_change = 0
            ny_change = 0
            px_change = 0
            py_change = 0
            jx_change = 0
            jy_change = 0
            mx_change = 0
            my_change = 0
            wx_change = 0
            wy_change = 0
            if hester_x >= 216 and hx_change > 0:
                hx_change = 0
            if hester_x <= 190 and hx_change < 0:
                hx_change = 0

        #collision detection in town
        if placeholder == 1:
            bx_change = 0
            by_change = 0
            cx_change = 0
            cy_change = 0
            px_change = 0
            py_change = 0
            jx_change = 0
            jy_change = 0
            dx_change = 0
            dy_change = 0
            mx_change = 0
            my_change = 0
            wx_change = 0
            wy_change = 0

            if hester_x - 100 < npc_x < hester_x + 100 and hester_y - 100 < npc_y < hester_y + 100:
                if npc_x > hester_x:
                    nx_change = 2
                elif npc_x < hester_x:
                    nx_change = -2
            if hester_y < 212:
                if -10 <= hester_x < 189 and hy_change < 0:
                    hy_change = 0
                if hester_x < 189 and hx_change < 0:
                    hx_change = 0
                if 540 >= hester_x >= 216 and hx_change != 0:
                    hx_change = 0 #224 532
                if 224 < hester_x < 532 and hy_change < 0:
                    hy_change = 0
                if hester_x > 564 and hx_change > 0:
                    hx_change = 0
                if hester_x > 564 and hy_change < 0:
                    hy_change = 0
            if hester_y > 267:
                if hester_x < 148 and hy_change > 0:
                    hy_change = 0
                if 176 < hester_x < 356 and hy_change > 0:
                    hy_change = 0
                if 380 < hester_x < 592 and hy_change > 0:
                    hy_change = 0
                if hester_x > 620 and hy_change > 0:
                    hy_change = 0
                if 148 > hester_x and hx_change < 0:
                    hx_change = 0
                if 176 < hester_x < 356 and hx_change != 0:
                    hx_change = 0
                if 380 < hester_x < 592 and hx_change != 0:
                    hx_change = 0
                if hester_x > 620 and hx_change > 0:
                    hx_change = 0
            #npc collision
            if npc_y < 212:
                if -10 <= npc_x < 189 and ny_change < 0:
                    ny_change = random.randint(0, 1)
                if npc_x < 189 and nx_change < 0:
                    nx_change = random.randint(0, 1)
                if 540 >= npc_x >= 216 and nx_change != 0:
                    nx_change = random.randint(-1, 1)
                if 224 < npc_x < 532 and ny_change < 0:
                    ny_change = random.randint(0, 1)
                if npc_x > 564 and nx_change > 0:
                    nx_change = random.randint(-1, 0)
                if npc_x > 564 and ny_change < 0:
                    ny_change = random.randint(0, 1)
            if npc_y > 267:
                if npc_x < 148 and ny_change > 0:
                    ny_change = random.randint(-1, 0)
                if 176 < npc_x < 356 and ny_change > 0:
                    ny_change = random.randint(-1, 0)
                if 380 < npc_x < 592 and ny_change > 0:
                    ny_change = random.randint(-1, 0)
                if npc_x > 620 and ny_change > 0:
                    ny_change = random.randint(-1, 0)
                if 148 > npc_x and nx_change < 0:
                    nx_change = random.randint(0, 1)
                if 176 < npc_x < 356 and nx_change != 0:
                    nx_change = random.randint(-1, 1)
                if 380 < npc_x < 592 and nx_change != 0:
                    nx_change = random.randint(-1, 1)
                if npc_x > 620 and nx_change > 0:
                    nx_change = random.randint(-1, 0)

        #collision detection in governors square place outside mansion
        if placeholder == 2:
            bx_change = 0
            by_change = 0
            cx_change = 0
            cy_change = 0
            nx_change = 0
            ny_change = 0
            px_change = 0
            py_change = 0
            jx_change = 0
            jy_change = 0
            mx_change = 0
            my_change = 0
            dx_change = 0
            dy_change = 0
            wx_change = 0
            wy_change = 0
            if hester_x <= 352 and hx_change < 0:
                hx_change = 0
            if hester_y <= 200:
                if hester_x >= 384 and hx_change > 0:
                    hx_change = 0
            if hester_y >= 256 and hy_change > 0:
                hy_change = 0
            if hester_x >= 644 and hx_change > 0:
                hx_change = 0
            if 384 < hester_x < 644:
                if hester_y < 200 and hy_change < 0:
                    hy_change = 0

        #collision detection in forest
        if placeholder == 3:
            ny_change = 0
            nx_change = 0
            px_change = 0
            py_change = 0
            jx_change = 0
            jy_change = 0
            mx_change = 0
            my_change = 0
            wx_change = 0
            wy_change = 0

            if hester_x - 100 < child_x < hester_x + 100 and hester_y - 100 < child_y < hester_y + 100:
                if child_x > hester_x:
                    cx_change = 2
                elif child_x < hester_x:
                    cx_change = -2
            if hester_x - 100 < boy_x < hester_x + 100 and hester_y - 100 < boy_y < hester_y + 100:
                if boy_x > hester_x:
                    bx_change = 2
                elif boy_x < hester_x:
                    bx_change = -2
            if hester_x <= 436 or hester_x >= 472:
                if hester_y <= 207 and hy_change < 0:
                    hy_change = 0
                if hester_y >= 271 and hy_change > 0:
                    hy_change = 0
            if hester_y < 207 or hester_y > 271:
                if hester_x >= 471 and hx_change > 0:
                    hx_change = 0
                if hester_x <= 436 and hx_change < 0:
                    hx_change = 0
            #child collision
            if child_x <= 436 or child_x >= 472:
                if child_y <= 241 and cy_change < 0:
                    cy_change = random.randint(0, 1)
                if child_y >= 305 and cy_change > 0:
                    cy_change = random.randint(-1, 0)
            if child_y < 241 or child_y > 305:
                if child_x >= 471 and cx_change > 0:
                    cx_change = random.randint(-1, 0)
                if child_x <= 436 and cx_change < 0:
                    cx_change = random.randint(0, 1)
            if child_y <= 0 and cy_change != 0:
                cy_change = random.randint(0, 1)
            if child_y >= 480 and cy_change > 0:
                cy_change = random.randint(-1, 0)
            if child_x > 550 and cx_change != 0:
                cx_change = random.randint(-1, 0)
            if child_x <= 20 and cx_change != 0:
                cx_change = random.randint(0, 1)
            #boy collision
            if boy_x <= 436 or boy_x >= 472:
                if boy_y <= 241 and by_change < 0:
                    by_change = random.randint(0, 1)
                if boy_y >= 305 and by_change > 0:
                    by_change = random.randint(-1, 0)
            if boy_y < 241 or boy_y > 305:
                if boy_x >= 471 and bx_change > 0:
                    bx_change = random.randint(-1, 0)
                if boy_x <= 436 and bx_change < 0:
                    bx_change = random.randint(0, 1)
            if boy_y <= 0 and by_change != 0:
                by_change = random.randint(0, 1)
            if boy_y >= 480 and by_change > 0:
                by_change = random.randint(-1, 0)
            if boy_x > 550 and bx_change != 0:
                bx_change = random.randint(-1, 0)
            if boy_x <= 20 and bx_change != 0:
                bx_change = random.randint(0, 1)
            #dimmesdale collision
            if dimmesdale_x <= 436 or dimmesdale_x >= 472:
                if dimmesdale_y <= 207 and dy_change < 0:
                    by_change = random.randint(0, 1)
                if dimmesdale_y >= 271 and dy_change > 0:
                    dy_change = random.randint(-1, 0)
            if dimmesdale_y < 207 or dimmesdale_y > 305:
                if dimmesdale_x >= 471 and dx_change > 0:
                    dx_change = random.randint(-1, 0)
                if dimmesdale_x <= 436 and dx_change < 0:
                    dx_change = random.randint(0, 1)
            if dimmesdale_y <= 0 and dy_change != 0:
                dy_change = random.randint(0, 1)
            if dimmesdale_y >= 480 and dy_change > 0:
                dy_change = random.randint(-1, 0)
            if dimmesdale_x > 550 and dx_change != 0:
                dx_change = random.randint(-1, 0)
            if dimmesdale_x <= 20 and dx_change != 0:
                dx_change = random.randint(0, 1)

        #collision detection in outside hesters house
        if placeholder == 5:
            bx_change = 0
            by_change = 0
            cx_change = 0
            cy_change = 0
            nx_change = 0
            ny_change = 0
            px_change = 0
            py_change = 0
            jx_change = 0
            jy_change = 0
            mx_change = 0
            my_change = 0
            dx_change = 0
            dy_change = 0
            wx_change = 0
            wy_change = 0
            if z == 0:
                z = 1
            if hester_x >= 468 and hx_change > 0:
                hx_change = 0
            if hester_x <= 440 and hester_y >= 280 and hx_change < 0:
                hx_change = 0
            if 184 <= hester_x <= 404:
                if hester_y >= 280 and hy_change > 0:
                    hy_change = 0
            if hester_x < 188 and hx_change < 0:
                hx_change = 0
            if hester_x >= 212 and hester_y <= 224 and hy_change < 0:
                hy_change = 0
            if hester_y < 224 and hester_x > 216 and hx_change > 0:
                hx_change = 0

        #collision detection in graveyard house
        # DONT HAVE COLLISION DETECTION IN HERE JUST SEND HER STRAIGHT OUT OF THE HOUSE
        if placeholder == 6:
            bx_change = 0
            by_change = 0
            cx_change = 0
            cy_change = 0
            nx_change = 0
            ny_change = 0
            px_change = 0
            py_change = 0
            jx_change = 0
            jy_change = 0
            mx_change = 0
            my_change = 0
            wx_change = 0
            dx_change = 0
            dy_change = 0
            wy_change = 0
        '''if placeholder == 6:
            bx_change = 0
            by_change = 0
            cx_change = 0
            cy_change = 0
            nx_change = 0
            ny_change = 0
            px_change = 0
            py_change = 0
            if 28 <= hester_x <= 104:
                if hester_y >= 63 and hy_change >= 0:
                    hy_change = 0
            if hester_y >= 83 and hx_change != 0 and 136 >= hester_x >= 4:
                hx_change = 0
            if 75 >= hester_y >= 59:
                if 119 >= hester_x >= 23 and hx_change != 0:
                    hx_change = 0
            if hester_y <= 0 and hy_change < 0:
                hy_change = 0'''

        #collision detection in hesters cabin
        if placeholder == 9:
            bx_change = 0
            by_change = 0
            cx_change = 0
            cy_change = 0
            nx_change = 0
            ny_change = 0
            dx_change = 0
            dy_change = 0
            jx_change = 0
            jy_change = 0
            mx_change = 0
            my_change = 0
            wx_change = 0
            wy_change = 0
            if 168 <= hester_x <= 300:
                if hester_y > 56 and hx_change != 0:
                    hx_change = 0
            if 46 <= hester_y <= 56:
                if 188 <= hester_x <= 300 and hx_change != 0:
                    hx_change = 0
            if 188 <= hester_x <= 300:
                if hester_y >= 40 and hy_change > 0:
                    hy_change = 0
            if hester_y <= 0 and hy_change < 0:
                hy_change = 0
            #collision detection pearl 300 195
            if pearl_y >= 140 and py_change > 0:
                py_change = random.randint(-1, 0)
            if pearl_x >= 262 and px_change > 0:
                px_change = random.randint(0, 1)
            if 168 <= pearl_x <= 300:
                if pearl_y > 56 and px_change != 0:
                    px_change = random.randint(-1, 1)
            if 46 <= pearl_y <= 56:
                if 188 <= pearl_x <= 300 and px_change != 0:
                    px_change = random.randint(-1, 1)
            if 188 <= pearl_x <= 300:
                if pearl_y >= 40 and py_change > 0:
                    py_change = random.randint(-1, 0)
            if pearl_y <= 0 and py_change < 0:
                py_change = random.randint(0, 1)
            if pearl_x <= 0 and px_change < 0:
                px_change = random.randint(0, 1)

        #detection in market
        if placeholder == 10:
            bx_change = 0
            by_change = 0
            cx_change = 0
            cy_change = 0
            nx_change = 0
            ny_change = 0
            wx_change = 0
            wy_change = 0
            dx_change = 0
            dy_change = 0
            if hester_x - 100 < marketman_x < hester_x + 100 and hester_y - 100 < marketman_y < hester_y + 100:
                if marketman_x > hester_x:
                    mx_change = 2
                elif marketman_x < hester_x:
                    mx_change = -2
            if hester_x >= 378:
                if hester_y >= 267 and hy_change > 0:
                    hy_change = 0
                if hester_y <= 207 and hy_change < 0:
                    hy_change = 0
            if hester_y >= 17:
                if hester_x <= 339 and hx_change < 0:
                    hx_change = 0
            if hester_y < 17:
                if hester_x >= 460 and hx_change != 0:
                    hx_change = 0
                if hester_x <= 264 and hx_change != 0:
                    hx_change = 0
                if hester_x >= 378:
                    if hester_y >= 11 and hy_change > 0:
                        hy_change = 0
                if hester_x <= 339:
                    if hester_y >= 11 and hy_change > 0:
                        hy_change = 0
            if 35 <= hester_y <= 203:
                if hester_x >= 368 and hx_change > 0:
                    hx_change = 0
            if hester_y >= 271:
                if hester_x >= 368 and hx_change > 0:
                    hx_change = 0
            #market man collision
            if marketman_x >= 378:
                if marketman_y >= 267 and my_change > 0:
                    my_change = random.randint(-1, 0)
                if marketman_y <= 207 and my_change < 0:
                    my_change = random.randint(0, 1)
            if marketman_y >= 17:
                if marketman_x <= 339 and mx_change < 0:
                    mx_change = random.randint(0, 1)
            if marketman_y < 17 and my_change < 0:
                my_change = random.randint(0, 1)
            if 35 <= marketman_y <= 203:
                if marketman_x >= 368 and mx_change > 0:
                    mx_change = random.randint(-1, 0)
            if marketman_y >= 271:
                if marketman_x >= 368 and mx_change > 0:
                    mx_change = random.randint(-1, 0)
            if marketman_y  >= 500 and my_change != 0:
                my_change = random.randint(-1, 0)
            if marketman_x >= 766 and mx_change > 0:
                mx_change = random.randint(-1, 0)




        #detection in jail
        if placeholder == 12:
            bx_change = 0
            by_change = 0
            cx_change = 0
            cy_change = 0
            nx_change = 0
            ny_change = 0
            mx_change = 0
            my_change = 0
            wx_change = 0
            wy_change = 0
            dx_change = 0
            dy_change = 0
            if hester_x - 100 < jailman_x < hester_x + 100 and hester_y - 100 < jailman_y < hester_y + 100:
                if jailman_x > hester_x:
                    jx_change = 2
                elif jailman_x < hester_x:
                    jx_change = -2
            if hester_y <= 116 and hy_change < 0:
                hy_change = 0
            #jailman collision
            if jailman_y <= 116 and jy_change < 0:
                jy_change = random.randint(0, 1)
            if jailman_x <= 0 and jx_change < 0:
                jx_change = random.randint(0, 1)
            if jailman_x >= 764 and jx_change > 0:
                jx_change = random.randint(-1, 0)
            if jailman_y >= 500 and jy_change > 0:
                jy_change = random.randint(0, 1)

        #detection in mansion interior
        if placeholder == 13:
            bx_change = 0
            by_change = 0
            dx_change = 0
            dy_change = 0
            cx_change = 0
            cy_change = 0
            nx_change = 0
            ny_change = 0
            mx_change = 0
            my_change = 0
            if 416 <= hester_y <= 428:
                if 74 <= hester_x <= 174 and hx_change != 0:
                    hx_change = 0
            if 74 <= hester_x <= 168 and 406 <= hester_y <= 412 and hy_change > 0:
                hy_change = 0
            if hester_y >= 428 and 54 <= hester_x <= 190 and hx_change != 0:
                hx_change = 0
            if hester_x >= 296 and hester_y <= 120 and hy_change < 0:
                hy_change = 0
                if hx_change > 0:
                    hx_change = 0
            if hester_y <= 76 and hy_change < 0:
                hy_change = 0
            #winthrop collision detection
            if 416 <= winthrop_y <= 428:
                if 74 <= winthrop_x <= 174 and wx_change != 0:
                    wx_change = random.randint(-1, 1)
            if 74 <= winthrop_x <= 168 and 406 <= winthrop_y <= 412 and wy_change > 0:
                wy_change = random.randint(-1, 0)
            if winthrop_y >= 428 and 54 <= winthrop_x <= 190 and wx_change != 0:
                wx_change = random.randint(-1, 1)
            if winthrop_x >= 296 and winthrop_y <= 120 and wy_change < 0:
                wy_change = random.randint(0, 1)
                if wx_change > 0:
                    wx_change = random.randint(-1, 0)
            if winthrop_y <= 76 and wy_change < 0:
                wy_change = random.randint(0, 1)
            if winthrop_x >= 546 and wx_change != 0:
                wx_change = random.randint(-1, 0)
            if winthrop_y >= 491 and wy_change > 0:
                wy_change = random.randint(-1, 0)
            if winthrop_x <= 0 and wx_change < 0:
                wx_change = random.randint(0, 1)

        naction = "standstill"
        caction = "standstill"
        baction = "standstill"
        paction = "standstill"
        jaction = "standstill"
        maction = "standstill"
        waction = "standstill"
        daction = "standstill"

        tick += 1

        if placeholder != 5 and placeholder != 3 and z == 1:
            z = 2

        if nx_change == 0 and tick % 20 == 0 and placeholder == 1:
            nx_change = random.randint(-1, 1)
        if ny_change == 0 and tick % 20 == 0 and placeholder == 1:
            ny_change = random.randint(-1, 1)

        if cx_change == 0 and tick % 20 == 0 and placeholder == 3:
            cx_change = random.randint(-1, 1)
        if cy_change == 0 and tick % 20 == 0 and placeholder == 3:
            cy_change = random.randint(-1, 1)

        if bx_change == 0 and tick % 20 == 0 and placeholder == 3:
            bx_change = random.randint(-1, 1)
        if by_change == 0 and tick % 20 == 0 and placeholder == 3:
            by_change = random.randint(-1, 1)

        if px_change == 0 and tick % 20 == 0 and placeholder == 9:
            px_change = random.randint(-1, 1)
        if py_change == 0 and tick % 20 == 0 and placeholder == 9:
            py_change = random.randint(-1, 1)

        if jx_change == 0 and tick % 20 == 0 and placeholder == 12:
            jx_change = random.randint(-1, 1)
        if jy_change == 0 and tick % 20 == 0 and placeholder == 12:
            jy_change = random.randint(-1, 1)
        if jy_change != 0 and tick % 100 == 80 and placeholder == 12:
            jy_change = 0
        if jx_change != 0 and tick % 100 == 50 and placeholder == 12:
            jx_change = 0

        if mx_change == 0 and tick % 20 == 0 and placeholder == 10:
            mx_change = random.randint(-1, 1)
        if my_change == 0 and tick % 20 == 0 and placeholder == 10:
            my_change = random.randint(-1, 1)

        if wx_change == 0 and tick % 20 == 0 and placeholder == 13:
            wx_change = random.randint(-1, 1)
        if wy_change == 0 and tick % 20 == 0 and placeholder == 13:
            wy_change = random.randint(-1, 1)

        if dx_change == 0 and tick % 20 == 0 and placeholder == 3:
            dx_change = random.randint(-1, 1)
        if dy_change == 0 and tick % 20 == 0 and placeholder == 3:
            dy_change = random.randint(-1, 1)


        #run away from hester feature
        

        npc_x += nx_change
        npc_y += ny_change

        child_x += cx_change
        child_y += cy_change

        boy_x += bx_change
        boy_y += by_change

        pearl_x += px_change
        pearl_y += py_change

        jailman_x += jx_change
        jailman_y += jy_change

        dimmesdale_x += dx_change
        dimmesdale_y += dy_change

        marketman_x += mx_change
        marketman_y += my_change

        winthrop_x += wx_change
        winthrop_y += wy_change

        disp.fill(black)
        disp.blit(gamemap[placeholder], (0, 0))
        if placeholder == 1:
            npc(npc_x, npc_y, naction)
        if placeholder == 3 and z != 1:
            childnpc(child_x, child_y, caction)
            boynpc(boy_x, boy_y, baction)
        if placeholder == 3 and z == 1:
            dimmesdale(dimmesdale_x, dimmesdale_y, daction, 2)
        if placeholder == 9:
            pearlnpc(pearl_x, pearl_y, paction)
        if placeholder == 10:
            marketnpc(marketman_x, marketman_y, maction)
        if placeholder == 12:
            jailman(jailman_x, jailman_y, jaction)
        if placeholder == 13:
            winthropnpc(winthrop_x, winthrop_y, waction)

        hlick = int(round(htick, 0))

        hester(hester_x, hester_y, haction, hlick)

        if placeholder == 2:
            disp.blit(mbushes, (0, 0))
        if placeholder == 5:
            disp.blit(cabintrees, (0, 0))
        if placeholder == 6:
            disp.blit(gravetable, (0, 0))
        if placeholder == 9:
            disp.blit(cabintable, (0, 0))
        if placeholder == 13:
            disp.blit(mansiontable, (0, 0))
        ####################################################################
        #     WHEN HESTER IS TALKING WITH ANYONE OTHER THAN DIMMESDALE     #
        # SHE SHOULD BE UNABLE TO HAVE FLUID DIALOUGE AND ONLY GIVE SIMPLE #
        #                             PHRASES                              #
        #                                                                  #
        # YOU CAN BARELY TRAVEL WITHOUT PEOPLE BARRATING YOU WITH COMMENTS #
        ####################################################################
        if hester_x < npc_x < hester_x + 60 and placeholder == 1 and hester_y < npc_y < hester_y + 60:
            if towndialouge == 1:
                dialouge("TOWNSPERSON: Oh... it's the adulterer. Get away from me heathen!")
                b = True
                while b == True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            dialouge("HESTER: I am very sorry sir. Have a good day!")
                            b = False

            if towndialouge >= 40:
                dialouge("TOWNSPERSON: Didn't I tell you to get away from me!")
                b = True
                while b == True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            dialouge("HESTER: Oh I'm sorry sir I'll leave right now.")
                            b = False

                towndialouge = 2

            towndialouge += 1
        childdialouge += 1
            #nx_change = 3

        if z != 1:
            if placeholder == 3 and childdialouge % 100 == 50 and hester_x - 50 < child_x < hester_x + 50 and hester_y - 50 < child_y < hester_y + 50:
                a = random.randint(0, 3)
                dialouge("GIRL: " + randomkiddialouges[a])
                time.sleep(1)
            if placeholder == 3 and childdialouge % 100 == 50 and hester_x - 50 < boy_x < hester_x + 50 and hester_y - 50 < boy_y < hester_y + 50:
                a = random.randint(0, 3)
                dialouge("BOY: " + randomkiddialouges[a])
                time.sleep(1)
        if z == 1:
            if placeholder == 3 and dimmesdaledialouge == 0 and hester_x - 20 < dimmesdale_x < hester_x + 20 and hester_y - 20 < dimmesdale_y < hester_y + 20:
                hesterdynamicdialouge("DIMMESDALE: Hi Hester, how have you been holding up?")
                a = True
                while a == True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_1:
                                dialouge("DIMMESDALE: This is no time to run, give it some time and everything will be fine!")
                                a = False
                            elif event.key == pygame.K_2:
                                dialouge("DIMMESDALE: I wish people would avoid me, the guilt is too much to handle!")
                                a = False
                time.sleep(1)
                dimmesdaledialouge = 1

        if placeholder == 6 and gravehousedialouge == 0:
            tinydialouge("DIMMESDALE: What are you doing in my house! Get out before anyone sees you.")
            time.sleep(2)
            hester_y = 300
            gravehousedialouge = 1

        if placeholder != 10:
            meatdialouge = 0
            clothesdialouge = 0
            fishdialouge = 0
        
        pearldialouge += 1

        if placeholder == 9 and pearldialouge % 100 == 50:
            if hester_x - 30 < pearl_x < hester_x + 30 and hester_y - 30 < pearl_y < hester_y + 30:
                tinydialouge("PEARL: I thought you were going to town?")
                time.sleep(1)
                a = True
                while a == True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            tinydialouge("HESTER: I'm just checking in.")
                            a = False
                            time.sleep(1)

        if placeholder == 10:
            if 700 < hester_x < 740 and hester_y <= 207 and meatdialouge == 0:
                dialouge("MEATMAN: What is it Hester?")
                time.sleep(1)
                a = True
                while a == True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            dialouge("HESTER: Oh I'm sorry I'm just browsing.")
                            a = False
                            time.sleep(1)
                dialouge("MEATMAN: Stop wasting my time!")
                time.sleep(1)
                meatdialouge = 1
            if 576 < hester_x < 620 and hester_y <= 207 and fishdialouge == 0:
                dialouge("FISHMAN: What is it Hester?")
                time.sleep(1)
                a = True
                while a == True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            dialouge("HESTER: Oh I'm sorry I'm just browsing.")
                            a = False
                            time.sleep(1)
                dialouge("FISHMAN: Stop wasting my time!")
                time.sleep(1)
                fishdialouge = 1
            if 444 < hester_x < 492 and 150 <= hester_y <= 207 and clothesdialouge == 0:
                dialouge("CLOTHESWOMAN: What is it Hester?")
                time.sleep(1)
                a = True
                while a == True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            dialouge("HESTER: Oh I'm sorry I'm just browsing.")
                            a = False
                            time.sleep(1)
                dialouge("CLOTHESWOMAN: Stop wasting my time!")
                time.sleep(1)
                clothesdialouge = 1

        if placeholder == 13 and winthropdialouge == 0 and hester_x - 20 < winthrop_x < hester_x + 20 and hester_y - 20 < winthrop_y < hester_y + 20:
            dialouge("HESTER: Hello Governor, how have you been feeling?")
            time.sleep(1.5)
            dialouge("WINTHROP: Good morning Hester, I'm not feeling so well.")
            time.sleep(1.5)
            dialouge("HESTER: I pray that you get better.")
            time.sleep(1.2)
            winthropdialouge = 1

        print(hester_x, hester_y)
        print(placeholder)

        pygame.display.update()
        clock.tick(60)

start_menu()
pygame.quit()
quit()
