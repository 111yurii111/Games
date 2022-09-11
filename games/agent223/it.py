import time
import os

os.system("clear")

time.sleep(1)

print("Let's get started")

time.sleep(1)

a = input("Firts question: what fruit does our company named after?: ")

if a == "apple":
    print("Corect")

    time.sleep(1)

    b = input("2+3?: ")

    if b =="5":
        print("Corect")

        time.sleep(1)

        c = input("how to spell truck?: ")

        if c == "t r u c k":
            print("Corect")

            time.sleep(1)

            d = input("Last question: what is the first color in the rainbow?: ")

            if d == "red":
                print("Corect")
                
                print("See, prety easy")

                time.sleep(2)

                yes = input("Press enter when you are ready to continue")

                if yes == "":
                    print("")
                    os.system("python3 at.py")

            else:
                print("Wrong, you will need to restart the interview")

                time.sleep(1)

                q = input("To restart press enter")

                if q == "":
                    os.system("python3 it.py")
                
        else:
            print("Wrong, you will need to restart the interview")

            time.sleep(1)
            q = input("To restart press enter")
            if q == "":
                os.system("python3 it.py")

    else:
        print("Wrong, you will need to restart the interview")

        time.sleep(1)

        q = input("To restart press enter")

        if q == "":
            os.system("python3 it.py")

else:
    print("Wrong, you will need to restart the interview")

    time.sleep(1)

    q = input("To restart press enter")

    if q == "":
        os.system("python3 it.py")



