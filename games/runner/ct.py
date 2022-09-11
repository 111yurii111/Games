import random, os
ip = input("heads or tails: ")

x = random.choice(range(2))

if x == 1:
    print("You won")
    input()
    os.system("python3 lvl3p2.py")

else:
    print("You lost")
    input()
    os.system("python3 hm.py")
