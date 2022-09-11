import time
import os

os.system("clear")

time.sleep(1)

print("Let's get started")

time.sleep(1)

a = input("Firts question: what year was the iphone released?: ")

if a == "2007":
    print("Corect")

    time.sleep(1)

    b = input("How rich is Apple?(Answer in billions dollars): ")

    if b =="1.2":
        print("Corect")

        time.sleep(1)

        c = input("Is iphone 7 and 8 same?: ")

        if c == "yes":
            print("Corect, many peple fail on this one")

            time.sleep(1)

            d = input("Last question: What color are blueprints?: ")

            if d == "blue":
                print("Corect")
                
                print("Congratulations, you've past the interview, you got the job!")

                time.sleep(2)

                yes = input("Press enter when you are ready to continue")

                if yes == "":
                    print("")
                    os.system("python3 ad.py")

            else:
                print("Wrong, you will need to restart the interview")

                time.sleep(1)

                q = input("To restart press enter")

                if q == "":
                    os.system("python3 id.py")
                
        else:
            print("Wrong, you will need to restart the interview")

            time.sleep(1)
            q = input("To restart press enter")
            if q == "":
                os.system("python3 id.py")

    else:
        print("Wrong, you will need to restart the interview")

        time.sleep(1)

        q = input("To restart press enter")

        if q == "":
            os.system("python3 id.py")

else:
    print("Wrong, you will need to restart the interview")

    time.sleep(1)

    q = input("To restart press enter")

    if q == "":
        os.system("python3 id.py")



