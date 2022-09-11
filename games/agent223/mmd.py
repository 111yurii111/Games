import time
import os

os.system("clear")

time.sleep(1)

print("You have to switch computers fast! The password is 9999")

yes = input("To switch computers press enter")

if yes == "":
    os.system("clear")
    ps = input("Password: ")
    if ps == "9999":

        os.system("clear")

        time.sleep(1)

        print("Switched computers succesfully")

        time.sleep(1)

        print("Hello again, I have a plan, I can hack into their network and you gotta sceenshot their emails")

        time.sleep(4)
    
        print("One small problem, I need a name of someone from there, do you know anyone from there?")

        name = input("Name: ").upper()

        if name == "FRED": 
            print("oooo yeeee, now,  you will have to log in as fred.tmf@gmail.com and the password is fred123")

            time.sleep(1)

            g = input("To start the hack press enter")
            if g == "":
                os.system("clear")
                os.system("python3  hmd.py")

