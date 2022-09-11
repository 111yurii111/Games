import pygame, time
screen = pygame.display.set_mode([500,600])

pygame.init()

myfont = pygame.font.SysFont('Corbel',140)
myfont1 = pygame.font.SysFont('Corbel',40)
run = True
while run:
    screen.fill((0,0,0))

    win = myfont.render("You won!!!", True,(0,255,0))
    credits = myfont1.render("Made by Yurii Boyko Studios", True,(0,255,0))
    credits2 = myfont1.render("Coder: Yurii Boyko", True,(0,255,0))
    credits3 = myfont1.render("Grafic designer: Yurii Boyko", True,(0,255,0))
    credits4 = myfont1.render("Creative mananger: Yurii Boyko", True,(0,255,0))
    credits5 = myfont1.render("Level designer: Yurii Boyko", True,(0,255,0))

    screen.blit(win, (10,50))
    screen.blit(credits, (10,300))
    screen.blit(credits2, (10,340))
    screen.blit(credits3, (10,380))
    screen.blit(credits4, (10,420))
    screen.blit(credits5, (10,460))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()


pygame.quit()
