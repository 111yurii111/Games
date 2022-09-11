from draw import draw, screen, move, pp1, teleport3, teleport4
import pygame, time, os
pygame.init()

myfont = pygame.font.SysFont('Corbel',100)
crash = 0
run = True
while run:
    screen.fill((255,255,255))
    player = pygame.draw.rect(screen, (0,0,0), pygame.Rect(pp1))

    pygame.draw.rect(screen, (200,100,0), pygame.Rect(350, 25, 25, 475))
    pygame.draw.rect(screen, (200,100,0), pygame.Rect(25, 400, 325, 25))
    pygame.draw.rect(screen, (200,100,0), pygame.Rect(25, 100, 300, 25))

    pygame.draw.rect(screen, (0,0,255), pygame.Rect(25, 75, 25, 25))#tl1
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(325, 425, 25, 25))#tl1
    pygame.draw.rect(screen, (200,0,0), pygame.Rect(25, 450, 25, 25))#bg2

    draw()

    pygame.draw.rect(screen, (100,100,100), pygame.Rect(450, 225, 50, 50))
    pygame.draw.rect(screen, (100,100,100), pygame.Rect(0, 225, 25, 50))

    label = myfont.render("Level 6", True, (0,0,0))#change here
    screen.blit(label, (130,520))


    time.sleep(.1)

    move()
    if pp1 == [450,225,25,25] or pp1 == [450,250,25,25]:
        break

    if pp1 == [25, 75, 25, 25]:
        teleport3()

    if pp1 == [325, 425, 25, 25]:
        teleport4()

    if pp1 == [25, 450, 25, 25]:
        break


    #check if crash
    if pp1[0] == 350:
        crash = 1

    if pp1[1] == 400 and pp1[0] <= 350:
        crash = 1

    if pp1[1] == 100:
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

if pp1 == [25, 450, 25, 25]:
    os.system("python3 bg2.py")#del this

if crash == 1:
    os.system("python3 lvl6.py")#cahnge here

if pp1 == [450,225,25,25] or pp1 == [450,250,25,25]:
    os.system("python3 lvl7.py")#cahnge here
