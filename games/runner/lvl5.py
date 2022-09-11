from draw import draw, screen, move2, pp1, teleport1,teleport2
import pygame, time, os
pygame.init()

myfont = pygame.font.SysFont('Corbel',100)
crash = 1
run = True
while run:
    screen.fill((200,100,0))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(0, 500, 500, 100))

    player = pygame.draw.rect(screen, (0,0,0), pygame.Rect(pp1))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(25, 225, 250, 50))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(250, 75, 25, 150))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(75, 75, 200, 25))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(75, 75, 25, 100))

    pygame.draw.rect(screen, (255,255,255), pygame.Rect(300, 400, 150, 25))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(300, 250, 25, 150))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(300, 225, 150, 50))

    pygame.draw.rect(screen, (0,0,255), pygame.Rect(75, 175, 25, 25))#tl1
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(450, 400, 25, 25))#tl2



    draw()
    player = pygame.draw.rect(screen, (0,0,0), pygame.Rect(pp1))

    pygame.draw.rect(screen, (100,100,100), pygame.Rect(450, 225, 50, 50))
    pygame.draw.rect(screen, (100,100,100), pygame.Rect(0, 225, 25, 50))

    label = myfont.render("Level 5", True, (0,0,0))#change here
    screen.blit(label, (130,520))


    time.sleep(.1)

    move2()
    if pp1 == [75, 175, 25, 25]:
        teleport1()

    if pp1 == [450, 400, 25, 25]:
        teleport2()

    if pp1 == [450,225,25,25] or pp1 == [450,250,25,25]:
        break


    #check if crash
    crash = 1

    if pp1[1] == 250 or pp1[1] == 225:
        crash = 0
        if pp1[0] == 275:
            crash = 1

    if pp1[0] == 250 and pp1[1] >= 75:
        crash = 0
        if pp1[1] >= 275:
            crash = 1


    if pp1[1] == 75 and pp1[0] >= 75:
        crash = 0
        if pp1[0] >= 275:
            crash =1

    if pp1[0] == 75 and pp1[1] >= 75:
        crash = 0




    if pp1[1] == 400 and pp1[0] >= 300:
        crash = 0

    if pp1[0] == 300 and pp1[1] >= 250:
        crash = 0
        if pp1[1] > 400:
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
    os.system("python3 lvl5.py") #change here

if pp1 == [450,225,25,25] or pp1 == [450,250,25,25]:
    os.system("python3 lvl6.py")#cahnge here
