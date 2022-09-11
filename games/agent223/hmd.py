import time
import os
os.system("clear")
time.sleep(1)

e = input("Email: ")
ps = input("Password: ")

if e == "fred.tmf@gmail.com" and ps == "fred123":
    os.system("clear")
    print("Welcome Fred")
    time.sleep(1)
    print("List of emails sent today:")
    print("To BOB")
    time.sleep(1)
    o = input("To read the email write the name of the operson emailed to ").upper()
    if o == "BOB":
        os.system("clear")
        time.sleep(1)
        print("Hey Bob, I messed up, I hired a guy that could help us blow up statue of liberty but some noname sniched on us, now i need your help to get rid of him, his computer's ip = 123.321.234,you can track him yourself  I'll pay $20000 for the job well done")
        time.sleep(6)
        print("From Mike: To screenshot press cmd shift 5 and save the it as sc.png")
        time .sleep(10)
        print("When you are done email it to the plice, their mail is police@gmail.com")
        e = input("to email it press enter")
        if e == "":
            to = input("To: ")
            w = input("Do you want to send sc.png?: ")

            if w == "yes":
                os.system("python3 f.py")
        
