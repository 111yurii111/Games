import time
import os
os.system("clear")
time.sleep(1)

print("Welcome to Apple")

print("My name is Raymond, I am the manager of the design department")

print("Let me introduse you to your new partner Mike, worning you, he is realy wierd, honestly, don't listen to everything he tells you")

time.sleep(3)
yes = input("Press enter when you are ready to continue")

if yes == "":
    print("")
    os.system("clear")

print("Hi mIcHaEl, I know thats not your real name, I know you are working for TMF, I used to work for them too, but I escaped, you can too,if you don't, they'll kill you after you're done after they get te blueprints they are going to blow up statue of loberty, THEY ARE TERORISTS")

time.sleep(5)

q = input("Trust him?: ")

if q == "yes":
    os.system("python3 md.py")

if q == "no":
    os.system("python3 td.py")
