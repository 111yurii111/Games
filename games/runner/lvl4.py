from draw import draw, screen, move, pp1
import pygame, time, os
pygame.init()

myfont = pygame.font.SysFont('Corbel',100)
crash = 0
color1 = [200,100,0]
color2 = [255,255,255]
count = 0
turn = 1

run = True
while run:
    screen.fill((255,255,255))


    pygame.draw.rect(screen, (color1), pygame.Rect(25, 150, 275, 25))
    pygame.draw.rect(screen, (color2), pygame.Rect(150, 25, 25, 125))
    pygame.draw.rect(screen, (color2), pygame.Rect(175, 325, 300, 25))
    pygame.draw.rect(screen, (color1), pygame.Rect(300, 350, 25, 125))

    pygame.draw.rect(screen, (200,100,0), pygame.Rect(150, 150, 25, 350))
    pygame.draw.rect(screen, (200,100,0), pygame.Rect(300, 25, 25, 325))

    draw()

    player = pygame.draw.rect(screen, (0,0,0), pygame.Rect(pp1))
    pygame.draw.rect(screen, (100,100,100), pygame.Rect(450, 225, 50, 50))
    pygame.draw.rect(screen, (100,100,100), pygame.Rect(0, 225, 25, 50))

    label = myfont.render("Level 4", True, (0,0,0))#change here
    screen.blit(label, (130,520))


    time.sleep(.1)
    count += 1



    move()
    if pp1 == [450,225,25,25] or pp1 == [450,250,25,25]:
        break


    #check if crash
    if pp1[0] == 150 and pp1[1] >= 150:
        crash = 1

    if pp1[0] == 300 and pp1[1] <= 325:
        crash = 1


    if pp1[1] == 150 and pp1[0] <= 300:
        crash = 1
        if color1 == [255,255,255]:
            crash = 0

    if pp1[1] == 325 and pp1[0] >= 150:
        crash = 1
        if color2 == [255,255,255]:
            crash = 0


    if pp1[0] == 150:
        crash = 1
        if color2 == [255,255,255]:
            crash = 0

    if pp1[0] == 300:
        crash = 1
        if color1 == [255,255,255]:
            crash = 0

    if crash == 1:
        break


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

    if count % 20 == 0:
        turn += 1
        if turn % 2 == 0:
            color1 = [255,255,255]
            color2 = [200,100,0]
        else:
            color1 = [200,100,0]
            color2 = [255,255,255]

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
    os.system("python3 lvl4.py") #change here

if pp1 == [450,225,25,25] or pp1 == [450,250,25,25]:
    os.system("python3 lvl5.py")#cahnge here
