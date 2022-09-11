import random
import os
import colorama
from colorama import Fore
import time

s = 0

w = ['red', 'blue', 'pink', 'yellow', 'brown', 'purple', 'black', 'white', 'green', 'orange', 'gray',]

d = random.choice(w)

z = Fore.WHITE + d

g = input(z + ": ")

if g.upper() == "WHITE":
    s += 1
    print("Corect")
    time.sleep(0.5)
else:
    print('Wrong')
    time.sleep(0.5)

