from draw import draw, screen, move, pp1
import pygame, time, os
pygame.init()

myfont = pygame.font.SysFont('Corbel',100)
crash = 0
run = True
while run:
    screen.fill((255,255,255))
    player = pygame.draw.rect(screen, (0,0,0), pygame.Rect(pp1))


    draw()

    pygame.draw.rect(screen, (100,100,100), pygame.Rect(450, 225, 50, 50))
    pygame.draw.rect(screen, (100,100,100), pygame.Rect(0, 225, 25, 50))

    label = myfont.render("Level 0", True, (0,0,0))#change here
    screen.blit(label, (130,520))


    time.sleep(.1)

    move()
    if pp1 == [450,225,25,25] or pp1 == [450,250,25,25]:
        break


    #check if crash



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()


pygame.quit()

if crash == 1:
    os.system("python3 blank.py") #change here

if pp1 == [450,225,25,25] or pp1 == [450,250,25,25]:
    os.system("python3 blank.py")#cahnge here
