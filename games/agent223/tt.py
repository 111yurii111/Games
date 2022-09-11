import time
import os

os.system("clear")

print("Good job, don't trust phycos in Apple")

time.sleep(3)

print("I have a plan, when you are in the truck go to this location '109.345.678'")

time.sleep(2)

q = input("Get in the truck?: ")

if q == "yes":
    os.system("clear")
    

else:
    print("Wrong answer")
    os.system("clear")
    
    time.sleep(1)

print("From Ronals to me: drive to the mall '345.567.543'")

time.sleep(3)

      
yes = input("Wherre to drive")

if yes == "109.345.678":
    time.sleep(3)
    print("Driving")
    time.sleep(3)
    os.system("clear")
    print("Thanks a lot, job well done")
    time.sleep(3)
    os.system("clear")
    os.system("python3 tbf.py")



