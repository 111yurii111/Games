import pygame, os, time, random
screen = pygame.display.set_mode([100,550])

pygame.init()

myfont = pygame.font.SysFont('Corbel',80)


left = []
right = []

#number of fake tyles on left side
No_left_tyles = random.choice(range(2,7))

options = [50,100,150,200,250,300,350,400,450]

#choosing witch tyles are fake on left side
for i in range(No_left_tyles):
    x = random.choice(range(len(options)))
    left.append(options[x])
    del options[x]
#every other tyle is on the right side
right = options

s = 1#score
def play():
    global s
    #drawing the lines and the player
    def draw():
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(50, 50, 1, 450))

        b = 50
        for i in range(10):
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, b, 100, 1))
            b += 50


    def move():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    pp[1] -= 50
                    pp[0] = 50
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    pp[1] -= 50
                    pp[0] = 0

    pp = [25,500,50,50]#player position
    crash = 0
    run = True
    while run:
        screen.fill((255,255,255))
        draw()
        player = pygame.draw.rect(screen, (0,0,0), pygame.Rect(pp))

        move()
        #check if crash
        if pp[0] == 0:#loops trhough every fake tyle on left side
            for i in range(len(left)):
                if pp[1] == left[i]:
                    crash = 1

        if pp[0] == 50:#loops trhough every fake tyle on right side
            for i in range(len(right)):
                if pp[1] == right[i]:
                    crash = 1

        if crash == 1:
            break

        if pp[1] == 0:
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.flip()


    if crash == 1:#end anymation
        screen.fill((0,0,0))
        uded = myfont.render("NO", True,(255,0,0))
        screen.blit(uded, (10,10))
        pygame.display.flip()
        time.sleep(.5)
        play()
        s += 1
        return s




play()
print("You win!")
print(f"It took you {s} tries")
