import random
import time
import os

q = input("Contries, Numbers, Fruits & Vegetables, Animals, Colors or Space(cn, n, f, a, c or s): ")

if q == "cn":
    from con import w

if q == "n":
    from num import w

if q == "c":
    from col import w

if q == "a":
    from an import w

if q == "f":
    from fv import w

if q == "s":
    from sp import w
    
r = input("Press enter to start")

os.system("clear")

t = time.time()

s = 0

while time.time() < t + 30:
    
    x = random.choice(w)

    def split(word):
        return [char for char in word]

    z = split(x)

    c = random.shuffle(z)

    y = "".join(z)

    print(y)

    a = input("What word is that: ")

    if a == x.lower():
        print("Corect")
        
        s = s + 1

    if a != x.lower():
        print("No")
        print("Answer is ", x)

print("Your score is: ", s)




 
