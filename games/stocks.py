import pygame, random, time
pygame.init()
screen = pygame.display.set_mode([500, 600])
myfont = pygame.font.SysFont("monospace", 50)
myfont1 = pygame.font.SysFont("monospace", 25)
myfont2 = pygame.font.SysFont("monospace", 20)
myfont3 = pygame.font.SysFont("monospace", 20)
l = []

y = 250
x = 480
xx = 480
yy = y
lc = [255,255,255, 0]
ly = 0

spos = [0, y]
fpos = [480, y]
upcol = [0,255,0]
dcol = [255,0,0]
hmc = [0,0,0]
upp = 0
downp = 0
money = 1000
mmoney = 0


for i in range(48):
    y = random.choice(range(y-30, y + 30))
    l.append(y)
    x -= 10
    yy = y
    xx = x

yes = True
while yes:
    screen.fill((0, 0, 0))

    y = random.choice(range(y - 30, y + 30))
    if y < 100:
        ly += 40
        spos = [0, ly]
        fpos = [480, ly]
        q = 0
        for i in range(len(l)):
            l[q] += 40
            q += 1

    if y > 400:
        ly -= 40
        spos = [0, ly]
        fpos = [480, ly]
        q = 0
        for i in range(len(l)):
            l[q] -= 40
            q += 1

    if upp == 0 and downp == 0:
        spos = [0, y]
        fpos = [480, y]

    x = 480
    q = 0
    xx = 480
    yy = y
    yyy = y
    for i in range(len(l)):
        x -= 10
        y = l[q]
        q += 1
        pygame.draw.line(screen, (255,255,255), (x, y), (xx, yy), 1)
        xx = x
        yy = y

    del l[47]
    l.insert(0, yyy)

    pygame.draw.rect(screen, (255,255,255), pygame.Rect(0, 500, 500, 100))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(480, 0, 1, 470))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(0, 470, 480, 1))

    moneys = myfont2.render(("$" + str(money)), True, (255,255,255))

    cdb = pygame.draw.rect(screen, (255,255,255), pygame.Rect(150, 500, 200, 100))
    cd = myfont1.render("CLOSE DEAL", True, (0,0,0))

    upb = pygame.draw.rect(screen, (upcol), pygame.Rect(0, 500, 150, 100))
    up = myfont.render("UP", True, (255,255,255))

    downb = pygame.draw.rect(screen, (dcol), pygame.Rect(350, 500, 150, 100))
    down = myfont.render("DOWN", True, (255,255,255))

    hm = myfont3.render(("$" + str(money - mmoney)), True, (hmc))
    screen.blit(hm, (10,470))
    screen.blit(moneys, (0,0))
    screen.blit(up, (40,525))
    screen.blit(down, (370,525))
    screen.blit(cd, (175,537))

    pygame.draw.line(screen, (255,255,255), [0, yyy], [480, yyy], 3)
    pygame.draw.line(screen, lc, spos, fpos, 3)






    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            yes= False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            if upp == 0:
                if upb.collidepoint(mouse_pos):
                    upp = 1
                    ly = y
                    upcol = [100,100,100]
                    dcol = [100,100,100]
                    lc = [0,255,0,2]
                    spos = [0, ly]
                    fpos = [480, ly]
                    mmoney = money
                    money -= 100

            if downp == 0:
                if downb.collidepoint(mouse_pos):
                    downp = 1
                    ly = y
                    upcol = [100,100,100]
                    dcol = [100,100,100]
                    lc = [255,0,0,1]
                    spos = [0, ly]
                    fpos = [480, ly]
                    mmoney = money
                    money -= 100

            if downp == 1 or upp == 1:
                if cdb.collidepoint(mouse_pos):
                    money += 100
                    if upp == 1:
                        money += ly - y

                    if downp == 1:
                        money += y - ly

                    hmc = [255,255,255]
                    upp = 0
                    downp = 0
                    upcol = [0,255,0]
                    dcol = [255,0,0]
                    lc = [255,255,255, 1]
                    spos = [0, ly]
                    fpos = [480, ly]




    pygame.display.flip()
    time.sleep(.3)
pygame.quit()
