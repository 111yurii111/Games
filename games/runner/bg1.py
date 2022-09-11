import pygame, os, time
from draw import draw3, screen

pygame.init()

os.system("clear")

myfont = pygame.font.SysFont('Corbel', 25)


draw3()
hi = myfont.render("Bose: Hi, my name is Mr Bose", True, (200,0,0))
play = myfont.render("Bose: Lest's play a game of hangman", True, (200,0,0))
play2 = myfont.render("Bose: I have thought of a word and u have to guess it", True, (200,0,0))
play3 = myfont.render("To begin the game to the terminal", True, (200,0,0))



screen.blit(hi, (130, 30))
pygame.display.flip()
time.sleep(1)

screen.blit(play, (130, 80))
pygame.display.flip()
time.sleep(1)

screen.blit(play2, (10, 130))
pygame.display.flip()
time.sleep(1)

screen.blit(play3, (10, 160))
pygame.display.flip()

print("Press enter when ready")
input()
pygame.quit()

os.system("python3 hm.py")
