from draw import draw, screen, move, pp1
import pygame, time, os
pygame.init()

myfont = pygame.font.SysFont('Corbel',100)
crash = 0
run = True
while run:
    screen.fill((255,255,255))
    player = pygame.draw.rect(screen, (0,0,0), pygame.Rect(pp1))

    pygame.draw.rect(screen, (200,100,0), pygame.Rect(400, 0, 25, 500))
    pygame.draw.rect(screen, (200,100,0), pygame.Rect(300, 75, 25, 350))
    pygame.draw.rect(screen, (200,100,0), pygame.Rect(25, 75, 300, 25))

    pygame.draw.rect(screen, (200,0,0), pygame.Rect(25, 50, 25, 25))#bg1
    if pp1 == [25, 50, 25, 25]:
        break

    draw()

    pygame.draw.rect(screen, (100,100,100), pygame.Rect(450, 225, 50, 50))
    pygame.draw.rect(screen, (100,100,100), pygame.Rect(0, 225, 25, 50))

    label = myfont.render("Level 3", True, (0,0,0))#change here
    screen.blit(label, (130,520))


    time.sleep(.1)

    move()
    if pp1 == [450,225,25,25] or pp1 == [450,250,25,25]:
        break


    #check if crash
    if  pp1[0] == 400:
        crash = 1

    if pp1[0] == 300 and pp1[1] <= 400:
        crash = 1
        if pp1[1] == 25 or pp1[1] == 50:
            crash = 0

    if pp1[1] == 75 and pp1[0] <= 300:
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

if pp1 == [25, 50, 25, 25]:
    os.system("python3 bg1.py")


if crash == 1:
    os.system("python3 lvl3.py") #change here

if pp1 == [450,225,25,25] or pp1 == [450,250,25,25]:
    os.system("python3 lvl4.py")#cahnge here
