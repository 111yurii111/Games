from draw import draw, screen, move2, pp1, tl1,tl2, tl3,tl4,tl5,tl6,tl7,tl8,tl9,tl10,tb1,tb2,tb3,tb4,tb5,tb6
import pygame, time, os
pygame.init()

myfont = pygame.font.SysFont('Corbel',100)
crash = 0
run = True
while run:
    screen.fill((255,255,255))
    player = pygame.draw.rect(screen, (0,0,0), pygame.Rect(pp1))

    pygame.draw.rect(screen, (200,100,0), pygame.Rect(150, 25, 25, 450))
    pygame.draw.rect(screen, (200,100,0), pygame.Rect(300, 25, 25, 450))

    pygame.draw.rect(screen, (200,100,0), pygame.Rect(25, 150, 450, 25))
    pygame.draw.rect(screen, (200,100,0), pygame.Rect(25, 300, 450, 25))


    #teleports:
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(125, 175, 25, 25))#b
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(325, 325, 25, 25))#b
    if pp1 == [125, 175, 25, 25]:
        tb1()
    if pp1 == [325, 325, 25, 25]:
        tb2()

    pygame.draw.rect(screen, (0,0,255), pygame.Rect(325, 450, 25, 25))#b
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(25, 25, 25, 25))#b
    if pp1 == [325, 450, 25, 25]:
        tb3()
    if pp1 == [25, 25, 25, 25]:
        tb4()

    pygame.draw.rect(screen, (0,0,255), pygame.Rect(125, 125, 25, 25))#b
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(175, 175, 25, 25))#b
    if pp1 == [125, 125, 25, 25]:
        tb5()
    if pp1 == [175, 175, 25, 25]:
        tb6()





    pygame.draw.rect(screen, (0,0,255), pygame.Rect(125, 275, 25, 25))#g
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(175, 25, 25, 25))#g
    if pp1 == [125, 275, 25, 25]:
        tl1()
    if pp1 == [175, 25, 25, 25]:
        tl2()

    pygame.draw.rect(screen, (0,0,255), pygame.Rect(275, 25, 25, 25))#g
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(25, 450, 25, 25))#g
    if pp1 == [275, 25, 25, 25]:
        tl3()
    if pp1 == [25, 450, 25, 25]:
        tl4()

    pygame.draw.rect(screen, (0,0,255), pygame.Rect(125, 325, 25, 25))#g
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(325, 125, 25, 25))#g
    if pp1 == [125, 325, 25, 25]:
        tl5()
    if pp1 == [325, 125, 25, 25]:
        tl6()

    pygame.draw.rect(screen, (0,0,255), pygame.Rect(450, 25, 25, 25))#g
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(275, 450, 25, 25))#g
    if pp1 == [450, 25, 25, 25]:
        tl7()
    if pp1 == [275, 450, 25, 25]:
        tl8()

    pygame.draw.rect(screen, (0,0,255), pygame.Rect(275, 325, 25, 25))#g
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(325, 275, 25, 25))#g
    if pp1 == [275, 325, 25, 25]:
        tl9()
    if pp1 == [325, 275, 25, 25]:
        tl10()

    draw()
    player = pygame.draw.rect(screen, (0,0,0), pygame.Rect(pp1))

    pygame.draw.rect(screen, (100,100,100), pygame.Rect(450, 225, 50, 50))
    pygame.draw.rect(screen, (100,100,100), pygame.Rect(0, 225, 25, 50))

    label = myfont.render("Level 7", True, (0,0,0))#change here
    screen.blit(label, (130,520))


    time.sleep(.1)

    move2()
    if pp1 == [450,225,25,25] or pp1 == [450,250,25,25]:
        break


    #check if crash
    if pp1[0] == 150 or pp1[0] == 300:
        crash = 1
    if pp1[1] == 150 or pp1[1] == 300:
        crash = 1







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
    os.system("python3 lvl7.py") #change here

if pp1 == [450,225,25,25] or pp1 == [450,250,25,25]:
    os.system("python3 finish.py")#cahnge here
