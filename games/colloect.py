import pygame, random,time, os

pygame.init()
screen = pygame.display.set_mode([500,500])
smallfont = pygame.font.SysFont('Corbel',200)

x = 0
a = 50
b = 50
aa = 50
bb = 50
pp1 = [0,0,50,50]
pp2 = [500, 0, 50,50]
posposx1 = [50, 100,150,200,250,300,350,400,450]
posposy1 = [50, 100,150,200,250,300,350,400,450]

ca1 = [255,0,0]
ca2 = [255,0,0]
ca3 = [255,0,0]
ca4 = [255,0,0]
ca5 = [255,0,0]
win = 0

aa1 = random.choice(posposx1)
bb1 = random.choice(posposy1)

aa2 = random.choice(posposx1)
bb2 = random.choice(posposy1)

aa3 = random.choice(posposx1)
bb3 = random.choice(posposy1)

aa4 = random.choice(posposx1)
bb4 = random.choice(posposy1)

aa5 = random.choice(posposx1)
bb5 = random.choice(posposy1)

run = True
str = time.time()
while run:
    screen.fill((255,255,255))
    a = 50
    b = 50

    a1 = pygame.draw.rect(screen, (ca1), pygame.Rect(aa1,bb1,50,50))
    a2 = pygame.draw.rect(screen, (ca2), pygame.Rect(aa2,bb2,50,50))
    a3 = pygame.draw.rect(screen, (ca3), pygame.Rect(aa3,bb3,50,50))
    a4 = pygame.draw.rect(screen, (ca4), pygame.Rect(aa4,bb4,50,50))
    a5 = pygame.draw.rect(screen, (ca5), pygame.Rect(aa5,bb5,50,50))



    for i in range(9):
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(a, 0, 1, 500))
        a += 50

    for i in range(9):
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, b, 1000, 1))
        b += 50

    player1 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(pp1))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pp1 == [0,0,50,50] and win >= 5:
                    win += 1

                if pp1 == [aa1,bb1,50,50] and ca1 != [255,255,255]:
                    ca1 = [255,255,255]
                    win += 1
                if pp1 == [aa2,bb2,50,50] and ca2 != [255,255,255]:
                    ca2 = [255,255,255]
                    win +=1
                if pp1 == [aa3,bb3,50,50] and ca3 != [255,255,255]:
                    ca3 = [255,255,255]
                    win += 1
                if pp1 == [aa4,bb4,50,50] and ca4 != [255,255,255]:
                    ca4 = [255,255,255]
                    win += 1
                if pp1 == [aa5,bb5,50,50] and ca5 != [255,255,255]:
                    ca5 = [255,255,255]
                    win += 1

            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if pp1[0] != 450:
                    pp1[0] += 50
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if pp1[0] != 0:
                    pp1[0] -= 50
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                if pp1[1] != 0:
                    pp1[1] -= 50
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if pp1[1] != 450:
                    pp1[1] += 50

    pygame.display.flip()
    if win == 6:
        fns = time.time()
        print(round((fns - str), 2))
        run = False
pygame.quit()
