import random
import os
import time

os.system('clear')

aa = input("ROCK, PAPER or SCISORS: ").upper()

p = ("ROCK", "PAPER", "SCISORS")

b = (random.choice(p))

a = ("")

if aa == "R":
    a = "ROCK"
elif aa == "P":
    a = "PAPER"
elif aa == "S":
    a = "SCISORS"

print("You chose " + a)
print("I chose " + b)

if a == b:
    print("Tie!")
    
    
elif a == "ROCK" and b == "PAPER" or a == "SCISORS" and b == "ROCK" or a == "PAPER" and b == "SCISORS":
    print("You lose!")
    

else:
    print("You win!")

time.sleep(3)

c = input("To repet press space bar and then enter and to quit press q and then enter: ")
    
if c == " ":
    os.system("python3 rps.py")


elif c == "q":
     os.system('clear')















