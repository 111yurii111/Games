import pygame, os
pygame.init()
screen = pygame.display.set_mode([500, 500])

xo = 2
win = 0
prs = 0
#colors
xc = (100, 0, 0)
oc = (0, 0, 100)
lc = (0, 165, 0)

#b1
b1 = ''
b1c = (0, 0, 0)
b1p = 0

#b2
b2 = ''
b2c = (0, 0,0)
b2p = 0

#b3
b3 = ''
b3c = (0, 0, 0)
b3p = 0

#b4
b4 = ''
b4c = (0, 0, 0)
b4p = 0

#b5
b5 = ''
b5c = (0, 0, 0)
b5p = 0

#b6
b6 = ''
b6c = (0, 0, 0)
b6p = 0

#b7
b7 = ''
b7c = (0, 0, 0)
b7p = 0

#b8
b8 = ''
b8c = (0, 0, 0)
b8p = 0

#b9
b9 = ''
b9c = (0, 0, 0)
b9p = 0


smallfont = pygame.font.SysFont('Corbel',250)

run = True
while run:
    screen.fill((0, 0, 0))

    #lines
    pygame.draw.rect(screen, lc, pygame.Rect(165, 0, 10,500))
    pygame.draw.rect(screen, lc, pygame.Rect(330, 0, 10,500))
    pygame.draw.rect(screen, lc, pygame.Rect(0, 165, 500,10))
    pygame.draw.rect(screen, lc, pygame.Rect(0, 330, 500,10))




    #buttons
    b1 = pygame.draw.rect(screen, b1c, pygame.Rect(0, 0, 165, 165))
    b2 = pygame.draw.rect(screen, b2c, pygame.Rect(175, 0, 155, 165))
    b3 = pygame.draw.rect(screen, b3c, pygame.Rect(340, 0, 165, 165))
    b4 = pygame.draw.rect(screen, b4c, pygame.Rect(0, 175, 165, 155))
    b5 = pygame.draw.rect(screen, b5c, pygame.Rect(175, 175, 155, 155))
    b6 = pygame.draw.rect(screen, b6c, pygame.Rect(340, 175, 165, 155))
    b7 = pygame.draw.rect(screen, b7c, pygame.Rect(0, 340, 165, 165))
    b8 = pygame.draw.rect(screen, b8c, pygame.Rect(175, 340, 155, 165))
    b9 = pygame.draw.rect(screen, b9c, pygame.Rect(340, 340, 165, 165))




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            #if buton presed
            if b1p == 0:
                if b1.collidepoint(mouse_pos):
                    print("Pressed b1")
                    b1 = pygame.draw.rect(screen, b1c, pygame.Rect(0, 0, 165, 165))
                    xo += 1
                    b1p = 1
                    prs += 1

            if b2p == 0:
                if b2.collidepoint(mouse_pos):
                    print("Pressed b2")
                    b2 = pygame.draw.rect(screen, b2c, pygame.Rect(175, 0, 155, 165))
                    xo += 1
                    b2p = 1
                    prs += 1

            if b3p == 0:
                if b3.collidepoint(mouse_pos):
                    print("Pressed b3")
                    b3 = pygame.draw.rect(screen, b3c, pygame.Rect(340, 0, 165, 165))
                    xo += 1
                    b3p = 1
                    prs += 1

            if b4p == 0:
                if b4.collidepoint(mouse_pos):
                    print("Pressed b4")
                    b4 = pygame.draw.rect(screen, b4c, pygame.Rect(0, 175, 165, 155))
                    xo += 1
                    b4p = 1
                    prs += 1

            if b5p == 0:
                if b5.collidepoint(mouse_pos):
                    print("Pressed b5")
                    b5 = pygame.draw.rect(screen, b5c, pygame.Rect(175, 175, 155, 155))
                    xo += 1
                    b5p = 1
                    prs += 1

            if b6p == 0:
                if b6.collidepoint(mouse_pos):
                    print("Pressed b6")
                    b6 = pygame.draw.rect(screen, b6c, pygame.Rect(340, 175, 165, 155))
                    xo += 1
                    b6p = 1
                    prs += 1

            if b7p == 0:
                if b7.collidepoint(mouse_pos):
                    print("Pressed b7")
                    b7 = pygame.draw.rect(screen, b7c, pygame.Rect(0, 340, 165, 165))
                    xo += 1
                    b7p = 1
                    prs += 1

            if b8p == 0:
                if b8.collidepoint(mouse_pos):
                    print("Pressed b8")
                    b8 = pygame.draw.rect(screen, b8c, pygame.Rect(175, 340, 155, 165))
                    xo += 1
                    b8p = 1
                    prs += 1

            if b9p == 0:
                if b9.collidepoint(mouse_pos):
                    print("Pressed b9")
                    b9 = pygame.draw.rect(screen, b9c, pygame.Rect(340, 340, 165, 165))
                    xo += 1
                    b9p = 1
                    prs += 1



        #x or o
        if xo % 2 != 0:
            x = smallfont.render('X' , True, xc)

            if b1p == 1:
                b1p = "x"

            if b2p == 1:
                b2p = "x"

            if b3p == 1:
                b3p = "x"

            if b4p == 1:
                b4p = "x"

            if b5p == 1:
                b5p = "x"

            if b6p == 1:
                b6p = "x"

            if b7p == 1:
                b7p = "x"

            if b8p == 1:
                b8p = "x"

            if b9p == 1:
                b9p = "x"

        if xo % 2 == 0:
            o = smallfont.render('O' , True, oc)

            if b1p == 1:
                b1p = "o"

            if b2p == 1:
                b2p = "o"

            if b3p == 1:
                b3p = "o"

            if b4p == 1:
                b4p = "o"

            if b5p == 1:
                b5p = "o"

            if b6p == 1:
                b6p = "o"

            if b7p == 1:
                b7p = "o"

            if b8p == 1:
                b8p = "o"

            if b9p == 1:
                b9p = "o"

        #x
        if b1p == "x":
            bx1 = screen.blit(x , (25, 10))

        if b2p == "x":
            bx2 = screen.blit(x , (190, 10))

        if b3p == "x":
            bx3 = screen.blit(x , (360, 10))

        if b4p == "x":
            bx4 = screen.blit(x , (25, 180))

        if b5p == "x":
            bx5 = screen.blit(x , (190, 180))

        if b6p == "x":
            bx6 = screen.blit(x , (360, 180))

        if b7p == "x":
            bx7 = screen.blit(x , (25, 350))

        if b8p == "x":
            bx8 = screen.blit(x , (190, 350))

        if b9p == "x":
            bx9 = screen.blit(x , (360, 350))


        #o
        if b1p == "o":
            bo1 = screen.blit(o , (20, 10))

        if b2p == "o":
            bo2 = screen.blit(o , (190, 10))

        if b3p == "o":
            bo3 = screen.blit(o , (355, 10))

        if b4p == "o":
            bo4 = screen.blit(o , (20, 175))

        if b5p == "o":
            bo5 = screen.blit(o , (190, 180))

        if b6p == "o":
            bo6 = screen.blit(o , (355, 180))

        if b7p == "o":
            bo7 = screen.blit(o , (20, 345))

        if b8p == "o":
            bo8 = screen.blit(o , (190, 345))

        if b9p == "o":
            bo9 = screen.blit(o , (355, 345))



        #scoring
        if b1p == 'x' and b2p == 'x' and b3p == 'x':
            pygame.draw.rect(screen, xc, pygame.Rect(0, 80, 500, 5))
            win += 1

        if b1p == 'o' and b2p == 'o' and b3p == 'o':
            pygame.draw.rect(screen, oc, pygame.Rect(0, 80, 500, 5))
            win += 1



        if b4p == 'x' and b5p == 'x' and b6p == 'x':
            pygame.draw.rect(screen, xc, pygame.Rect(0, 250, 500, 5))
            win += 1

        if b4p == 'o' and b5p == 'o' and b6p == 'o':
            pygame.draw.rect(screen, oc, pygame.Rect(0, 250, 500, 5))
            win += 1



        if b1p == 'x' and b4p == 'x' and b7p == 'x':
            pygame.draw.rect(screen, xc, pygame.Rect(82, 0, 5, 500))
            win += 1

        if b1p == 'o' and b4p == 'o' and b7p == 'o':
            pygame.draw.rect(screen, oc, pygame.Rect(82, 0, 5, 500))
            win += 1



        if b3p == 'x' and b5p == 'x' and b7p == 'x':
            pygame.draw.line(screen, xc, (500, 0), (0, 500), 5)
            win += 1

        if b3p == 'o' and b5p == 'o' and b7p == 'o':
            pygame.draw.line(screen, oc, (500, 0), (0, 500), 5)
            win += 1



        if b2p == 'x' and b5p == 'x' and b8p == 'x':
            pygame.draw.rect(screen, xc, pygame.Rect(245, 0, 5, 500))
            win += 1

        if b2p == 'o' and b5p == 'o' and b8p == 'o':
            pygame.draw.rect(screen, oc, pygame.Rect(250, 0, 5, 500))
            win += 1



        if b3p == 'x' and b6p == 'x' and b9p == 'x':
            pygame.draw.rect(screen, xc, pygame.Rect(415, 0, 5, 500))
            win += 1

        if b3p == 'o' and b6p == 'o' and b9p == 'o':
            pygame.draw.rect(screen, oc, pygame.Rect(415, 0, 5, 500))
            win += 1



        if b7p == 'x' and b8p == 'x' and b9p == 'x':
            pygame.draw.rect(screen, xc, pygame.Rect(0, 418, 500, 5))
            win += 1

        if b7p == 'o' and b8p == 'o' and b9p == 'o':
            pygame.draw.rect(screen, oc, pygame.Rect(0, 418, 500, 5))
            win += 1



        if b1p == 'x' and b5p == 'x' and b9p == 'x':
            pygame.draw.line(screen, xc, (0, 0), (500, 500), 5)
            win += 1

        if b1p == 'o' and b5p == 'o' and b9p == 'o':
            pygame.draw.line(screen, oc, (0, 0), (500, 500), 5)
            win += 1


        if prs == 9:
            win += 1



        if win > 3:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                os.system("python3 /Users/yura/desktop/python/xo/xo.py")



        pygame.display.update()

pygame.quit()
