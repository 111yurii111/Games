import pygame, os, time
screen = pygame.display.set_mode([500,600])

pp1 = [25,225,25,25]


def draw():
    a = 25
    b = 25
    pygame.draw.rect(screen, (0,0,100), pygame.Rect(0, 0, 25, 500))
    pygame.draw.rect(screen, (0,0,100), pygame.Rect(475, 0, 25, 500))
    pygame.draw.rect(screen, (0,0,100), pygame.Rect(0, 0, 500, 25))
    pygame.draw.rect(screen, (0,0,100), pygame.Rect(0, 475, 500, 25))

    for i in range(19):
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(a, 0, 1, 500))
        a += 25

    for i in range(19):
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, b, 500, 1))
        b += 25



def move():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        if pp1[0] != 450:
            pp1[0] += 25
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if pp1[0] != 25:
            pp1[0] -= 25
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        if pp1[1] != 25:
            pp1[1] -= 25
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        if pp1[1] != 450:
            pp1[1] += 25

def move2():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if pp1[0] != 450:
                    pp1[0] += 25
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if pp1[0] != 25:
                    pp1[0] -= 25
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                if pp1[1] != 25:
                    pp1[1] -= 25
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if pp1[1] != 450:
                    pp1[1] += 25



def draw2():
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (0,200,0), pygame.Rect(10, 10, 100, 100))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(30, 30, 15, 15))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(75, 30, 15, 15))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(30, 80, 60, 10))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(20, 70, 10, 10))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(90, 70, 10, 10))




def draw3():
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (200,0,0), pygame.Rect(10, 10, 100, 100))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(30, 30, 15, 15))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(75, 30, 15, 15))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(30, 80, 60, 10))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(20, 70, 10, 10))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(90, 70, 10, 10))

def draw4():
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (200,0,0), pygame.Rect(10, 10, 100, 100))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(30, 30, 15, 15))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(75, 30, 15, 15))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(30, 80, 60, 10))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(20, 90, 10, 10))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(90, 90, 10, 10))



def teleport1():
    pp1[0] += 350
    pp1[1] += 225

def teleport2():
    pp1[0] -= 375
    pp1[1] -= 250

def teleport3():
    pp1[0] = 300
    pp1[1] = 425

def teleport4():
    pp1[0] = 50
    pp1[1] = 75




def tl1():
    pp1[0] = 200
    pp1[1] = 25

def tl2():
    pp1[0] = 100
    pp1[1] = 275

def tl3():
    pp1[0] = 25
    pp1[1] = 425

def tl4():
    pp1[0] = 250
    pp1[1] = 25

def tl5():
    pp1[0] = 350
    pp1[1] = 125

def tl6():
    pp1[0] = 100
    pp1[1] = 325

def tl7():
    pp1[0] = 275
    pp1[1] = 425

def tl8():
    pp1[0] = 425
    pp1[1] = 25

def tl9():
    pp1[0] = 325
    pp1[1] = 250

def tl10():
    pp1[0] = 275
    pp1[1] = 350



def tb1():
    pp1[0] = 325
    pp1[1] = 350

def tb2():
    pp1[0] = 100
    pp1[1] = 175

def tb3():
    pp1[0] = 25
    pp1[1] = 50

def tb4():
    pp1[0] = 325
    pp1[1] = 425

def tb5():
    pp1[0] = 200
    pp1[1] = 175

def tb6():
    pp1[0] = 100
    pp1[1] = 125


tryes = 0
def plus():
    tryes += 1


def p3():
    pp1[0] = 25
    pp1[1] = 450




#hi
