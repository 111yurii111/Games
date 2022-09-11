from draw import draw2, screen
import pygame, time, os
pygame.init()

os.system("clear")

myfont = pygame.font.SysFont('Corbel', 25)


draw2()
hi = myfont.render("GUT: Hi, my name is Mr Gut", True, (0,200,0))
help = myfont.render("GUT: I need your help", True, (0,200,0))
help2 = myfont.render("GUT: I was going home from shopping", True, (0,200,0))
help3 = myfont.render("and suddently my bag ripped and all", True, (0,200,0))
help4 = myfont.render("of my apples fell out", True, (0,200,0))
help5 = myfont.render("GUT: Can u collect them?", True, (0,200,0))
ready = myfont.render("GUT: If u ready, go to the terminal", True, (0,200,0))

screen.blit(hi, (130, 30))
pygame.display.flip()
time.sleep(2)
screen.blit(help, (130, 80))
screen.blit(help2, (10, 130))
screen.blit(help3, (10, 160))
screen.blit(help4, (10, 190))
screen.blit(help5, (10, 230))
pygame.display.flip()
time.sleep(5)
screen.blit(ready, (10, 280))
pygame.display.flip()


print("""INSTRUCTIONS:
-Movement is the same
-To collect the apples press space
-After collecting all the apples return to the upper left corner and press space
""")

print("Press enter when you are ready to colect apples")
input()

pygame.quit()
os.system("python3 cg.py")
