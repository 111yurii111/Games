import pygame, os, time
from draw import draw3, screen

pygame.init()

os.system("clear")

myfont = pygame.font.SysFont('Corbel', 25)


draw3()
hi = myfont.render("Bose: Hello again!", True, (200,0,0))
play = myfont.render("Bose: Let's play a game", True, (200,0,0))
play2 = myfont.render("Bose: I have layed out some tyles and you have to choose", True, (200,0,0))
play3 = myfont.render("between left or right, one of them will kill you!", True, (200,0,0))
play4 = myfont.render("To begin the game to the terminal", True, (200,0,0))



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

screen.blit(play4, (10, 190))
pygame.display.flip()

print("""Just choose left or right by clicking ad or arrows
Press enter when ready""")
input()
pygame.quit()

os.system("python3 falingtyles.py")
