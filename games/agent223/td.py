import time
import os

os.system("clear")

print("Good job, don't trust phycos in Apple")

time.sleep(3)

print("Now we gotta get those bluprints")

time.sleep(2)

q = input("Ask Raymond for bluprints?: ")

if q == "yes":
    os.system("clear")
    

else:
    os.system("clear")
    print("Wrong answer")
    time.sleep(1)

print("From me to Raymond: I'll need those bluprints of the new iphone to start working, send them please")

send = input("Send?")

if send == "yes":
    print("Sent")
    time.sleep(3)

os.system("clear")

print("From Raymond to me: Of couarse")

time.sleep(1)

print("To screenshot press cmd shift 5 and save the it as ss.png")

time.sleep(2)

os.system("open bp.jpeg")

time.sleep(8)

print("Send the screenshot to us on tmf@gmail.com")

yes = input("To send it to TMF press enter")

if yes == "":
    print("")
    os.system("clear")
    to = input("To: ")
    w = input("Do you want to send ss.png?: ")

    if w == "yes":
        os.system("clear")
        print("SENT")
        os.system("python3 bf.py")



