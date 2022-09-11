import pygame, os, time
screen = pygame.display.set_mode([100,550])
pp = [25,500,50,50]


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
