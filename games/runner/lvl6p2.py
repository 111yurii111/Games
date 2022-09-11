from draw import draw, screen, draw3
import pygame, time, os
pygame.init()


pp1 = [25,450,25,25]

def teleport3():
    pp1[0] = 300
    pp1[1] = 425

def teleport4():
    pp1[0] = 50
    pp1[1] = 75


myfont = pygame.font.SysFont('Corbel',100)
sec = 5
for i in range(5):
    draw3()
    myfont1 = pygame.font.SysFont('Corbel', 30)
    uded = myfont1.render("Bose: WHAT, HOW ARE YOU ALIVE?", True, (200,0,0))
    con = myfont1.render("Continue in:", True, (200,0,0))
    sleft = myfont.render(str(sec), True, (200,0,0))
    screen.blit(uded, (110,50))
    screen.blit(con, (200,350))
    screen.blit(sleft, (240,400))
    pygame.display.flip()
    time.sleep(1)
    sec -= 1
crash = 0
run = True
while run:
    screen.fill((255,255,255))
    player = pygame.draw.rect(screen, (0,0,0), pygame.Rect(pp1))

    pygame.draw.rect(screen, (200,100,0), pygame.Rect(350, 100, 25, 375))
    pygame.draw.rect(screen, (200,100,0), pygame.Rect(25, 400, 325, 25))
    pygame.draw.rect(screen, (200,100,0), pygame.Rect(25, 100, 325  , 25))

    pygame.draw.rect(screen, (0,0,255), pygame.Rect(25, 75, 25, 25))#tl1
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(325, 425, 25, 25))#tl1


    draw()

    pygame.draw.rect(screen, (100,100,100), pygame.Rect(450, 225, 50, 50))
    pygame.draw.rect(screen, (100,100,100), pygame.Rect(0, 225, 25, 50))

    label = myfont.render("Level 6", True, (0,0,0))#change here
    screen.blit(label, (130,520))


    time.sleep(.1)

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



    if pp1 == [450,225,25,25] or pp1 == [450,250,25,25]:
        break

    if pp1 == [25, 75, 25, 25]:
        teleport3()

    if pp1 == [325, 425, 25, 25]:
        teleport4()



    #check if crash
    if pp1[0] == 350 and pp1[1] >= 100:
        crash = 1

    if pp1[1] == 400 and pp1[0] <= 350:
        crash = 1

    if pp1[1] == 100 and pp1[0] <= 325:
        crash = 1
        if pp1[0] == 325:
            crash =0



    if crash == 1:
        break


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.flip()

if crash == 1:
    time.sleep(1)
    sec = 3
    for i in range(3):
        screen.fill((0,0,0))
        uded = myfont.render("U DIED :(", True,(255,0,0))
        sleft = myfont.render(str(sec), True, (255,0,0))
        screen.blit(uded, (100,50))
        screen.blit(sleft, (240,200))
        pygame.display.flip()
        time.sleep(1)
        sec -= 1


pygame.quit()

if crash == 1:
    os.system("python3 lvl6p2.py")#cahnge here

if pp1 == [450,225,25,25] or pp1 == [450,250,25,25]:
    os.system("python3 lvl7.py")#cahnge here
