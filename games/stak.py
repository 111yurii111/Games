import pygame,time, os,random

pygame.init()
screen = pygame.display.set_mode([500,800])

drw = [100, 700, 300,50]
lst = [100, 750, 300,50]
pls = 5
a = 0
score = 0

smallfont = pygame.font.SysFont('Corbel',200)
font = pygame.font.SysFont('Corbel',50)


run = True
while run:
    screen.fill((255,255,255))
    back = pygame.draw.rect(screen, (255,255,255,0), pygame.Rect(0,0,500,800))

    lab = smallfont.render(str(score), False, (0,0,100))
    quit = font.render("Again", False, (255,255,255))
    screen.blit(lab , (30, 10))

    if drw[2] <= 0:
        while run:
            back = pygame.draw.rect(screen, (255,255,255), pygame.Rect(0,0,500,800))
            screen.blit(lab, (30, 10))
            again = pygame.draw.rect(screen, (255,0,0), pygame.Rect(0, 750, 500, 50))
            screen.blit(quit, (200, 750))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run= False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos

                    if again.collidepoint(mouse_pos):
                        pygame.quit()
                        os.system("python3 stak.py")


            pygame.display.flip()





    if a == 0:
        pygame.draw.rect(screen,(0,0,0), pygame.Rect(100, 750, 300,50))

    pygame.draw.rect(screen,(0,0,0), pygame.Rect(drw))





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if drw[0] > lst[4 * a]:
                    drw[2] -= (drw[0] - lst[4 * a])

                if drw[0] < lst[4 * a]:
                    drw[2] -= (lst[4 * a] - drw[0])
                    drw[0] += (lst[4 * a] - drw[0])
                lst += drw
                drw[1] -= 50
                a += 1
                score += 1

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            if back.collidepoint(mouse_pos):
                if drw[0] > lst[4 * a]:
                    drw[2] -= (drw[0] - lst[4 * a])

                if drw[0] < lst[4 * a]:
                    drw[2] -= (lst[4 * a] - drw[0])
                    drw[0] += (lst[4 * a] - drw[0])
                lst += drw
                drw[1] -= 50
                a += 1
                score += 1



    if drw[0] == 500 - drw[2]:
        pls = -5
    if drw[0] == 0:
        pls = 5

    x = 0
    for i in range(a + 1):
        pygame.draw.rect(screen,(0,0,0), pygame.Rect([lst[x], lst[1 + x], lst[2 + x], lst[3 + x]]))
        x += 4

    if drw[1] <= 150:
        drw[1] += 50
        y = 1
        for i in range(a):
            lst[y] += 50
            y += 4
        lst[y] += 50

    pygame.display.flip()
    time.sleep(0.03)
    drw[0] += pls
pygame.quit()
