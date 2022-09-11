import pygame, os, time
from draw2 import screen, pp, draw, move
pygame.init()

myfont = pygame.font.SysFont('Corbel',80)

crash = 0

run = True
while run:
    screen.fill((255,255,255))
    draw()
    player = pygame.draw.rect(screen, (0,0,0), pygame.Rect(pp))

    move()


    #check if crash

    if pp[0] == 0:
        if pp[1] == 500 or pp[1] == 450 or pp[1] == 400 or pp[1] == 300 or pp[1] == 50:
            crash = 1

    if pp[0] == 50:
        if pp[1] == 350 or pp[1] == 250 or pp[1] == 200 or pp[1] == 100:
            crash = 1




    if crash == 1:
        break


    if pp[1] == 0:
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()


if crash == 1:
    sec = 1
    for i in range(3):
        screen.fill((0,0,0))
        uded = myfont.render("NO", True,(255,0,0))
        screen.blit(uded, (10,10))
        pygame.display.flip()
        time.sleep(1)
        sec -= 1

pygame.quit()

if pp[1] == 0:
 os.system("python3 lvl6p2.py") #change here

if crash == 1:
    os.system("python3 falingtyles.py") #change here
