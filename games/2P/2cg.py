import pygame, random,time, os

pygame.init()
screen = pygame.display.set_mode([1000,500])

x = 0
a = 50
b = 50
aa = 50
bb = 50
pp1 = [0,0,50,50]
pp2 = [500, 0, 50,50]
posposx1 = [50, 100,150,200,250,300,350,400,450]
posposy1 = [50, 100,150,200,250,300,350,400,450]

posposx2 = [550, 600,650,700,750,800,850,900,950]
posposy2 = [50, 100,150,200,250,300,350,400,450]

ca1 = [255,0,0]
ca2 = [255,0,0]
ca3 = [255,0,0]
ca4 = [255,0,0]
ca5 = [255,0,0]

cb1 = [255,0,0]
cb2 = [255,0,0]
cb3 = [255,0,0]
cb4 = [255,0,0]
cb5 = [255,0,0]
win = 0
win2 = 0


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



qaa1 = random.choice(posposx2)
qbb1 = random.choice(posposy2)

qaa2 = random.choice(posposx2)
qbb2 = random.choice(posposy2)

qaa3 = random.choice(posposx2)
qbb3 = random.choice(posposy2)

qaa4 = random.choice(posposx2)
qbb4 = random.choice(posposy2)

qaa5 = random.choice(posposx2)
qbb5 = random.choice(posposy2)

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

    b1 = pygame.draw.rect(screen, (cb1), pygame.Rect(qaa1,qbb1,50,50))
    b2 = pygame.draw.rect(screen, (cb2), pygame.Rect(qaa2,qbb2,50,50))
    b3 = pygame.draw.rect(screen, (cb3), pygame.Rect(qaa3,qbb3,50,50))
    b4 = pygame.draw.rect(screen, (cb4), pygame.Rect(qaa4,qbb4,50,50))
    b5 = pygame.draw.rect(screen, (cb5), pygame.Rect(qaa5,qbb5,50,50))



    for i in range(19):
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(a, 0, 1, 500))
        a += 50

    for i in range(9):
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, b, 1000, 1))
        b += 50

    player1 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(pp1))
    player2 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(pp2))
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(495, 0, 10, 500))


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

            if event.key == pygame.K_RETURN:
                if pp2 == [500,0,50,50] and win2 >= 5:
                    win2 += 1

                if pp2 == [qaa1,qbb1,50,50] and cb1 != [255,255,255]:
                    cb1 = [255,255,255]
                    win2 += 1
                if pp2 == [qaa2,qbb2,50,50] and cb2 != [255,255,255]:
                    cb2 = [255,255,255]
                    win2 +=1
                if pp2 == [qaa3,qbb3,50,50] and cb3 != [255,255,255]:
                    cb3 = [255,255,255]
                    win2 += 1
                if pp2 == [qaa4,qbb4,50,50] and cb4 != [255,255,255]:
                    cb4 = [255,255,255]
                    win2 += 1
                if pp2 == [qaa5,qbb5,50,50] and cb5 != [255,255,255]:
                    cb5 = [255,255,255]
                    win2 += 1

            if event.key == pygame.K_d:
                if pp1[0] != 450:
                    pp1[0] += 50
            if event.key == pygame.K_a:
                if pp1[0] != 0:
                    pp1[0] -= 50
            if event.key == pygame.K_w:
                if pp1[1] != 0:
                    pp1[1] -= 50
            if event.key == pygame.K_s:
                if pp1[1] != 450:
                    pp1[1] += 50

            if event.key == pygame.K_RIGHT:
                if pp2[0] != 950:
                    pp2[0] += 50
            if event.key == pygame.K_LEFT:
                if pp2[0] != 500:
                    pp2[0] -= 50
            if event.key == pygame.K_UP:
                if pp2[1] != 0:
                    pp2[1] -= 50
            if event.key == pygame.K_DOWN:
                if pp2[1] != 450:
                    pp2[1] += 50


    pygame.display.flip()
    if win == 6:
        fns = time.time()
        print(round((fns - str), 2), ",1P, WON!")
        run = False

    if win2 == 6:
        fns = time.time()
        print(round((fns - str), 2), ",2P WON!")
        run = False
pygame.quit()
