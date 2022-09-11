import time
import os

os.system("clear")

print("Good job, you've made a good choice, you won't regret it")

time.sleep(3)

print("Now we gotta take them down, but we don't have enough evedance to do so")

time.sleep(3)

print("Mesege from TMF: How can you trust him, he is working for Apple, they are the bad guys,do the right thing and get us those bluprints")

time.sleep(5)

print("They hacked your computer so we can't do this much longer, or they will send a killer after you like they did to me")

time.sleep(5)

q = input("Still trust him?: ")

if q == "yes":
    os.system("python3 mmd.py")

if q == "no":
    os.system("python3 td.py")

