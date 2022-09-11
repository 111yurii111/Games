import random
import time
import os
print("Write the color of the text")
input("Start")
t = time.time()
f = t + 30
s = 0
while time.time() < f:
    os.system('clear')
    o = open("coll.py", "w")

    w = ['red', 'blue', 'yellow', 'black', 'white', 'green']

    c = random.choice(w).upper()



    o.write(f"""import random
import os
import colorama
from colorama import Fore
import time

s = {s}

w = ['red', 'blue', 'pink', 'yellow', 'brown', 'purple', 'black', 'white', 'green', 'orange', 'gray',]

d = random.choice(w)

z = Fore.{c} + d

g = input(z + ": ")

if g.upper() == "{c}":
    s += 1
    print("Corect")
    time.sleep(0.5)
else:
    print('Wrong')
    time.sleep(0.5)

""")
    o.close()

    os.system("python3 coll.py")
