import random
import os

print("Mastermind 2 Players")

print("the colors are: (red, orange, yellow, green, blue, purple)")

rob = input("Player 1 choose the code(press cmd k after u press enter):")

os.system("clear")

print("Mastermind")

print("the colors are: (red, orange, yellow, green, blue, purple)")

print("0 = wrong color, 1 = right color wrong place, 2 = right color right place")


ar = ''
ges = ''
tray = 0
while ges != rob or tray != 10:
    ar = rob.split()
    ans = ''
    print("You have ", 10 - int(tray), "tries left")
    ges = input("Guess the code: ")
    ag = ges.split()

    if ges == "i give up":
        break

    if len(ag) != 4:
        print("Wrong amount of colors")
        continue

    x = 0
    for i in range(len(ar)):
        if ag[x] == ar[x]:
            ar[x] = " "
            ag[x] = ''
            ans += '2 '
        x += 1

    x = 0
    for i in range(len(ar)):
        if ag[x] in ar:
            ans += '1 '
        x += 1

    while len(ans) < 8:
        ans += "0 "

    print(ans)


    if ans == "2 2 2 2 ":
        break

    if tray == 10:
        break
    tray += 1

if ans == "2 2 2 2 ":
    print("Corect! You won!")
else:
    print("You lost!")
    print("the corect answer is ", rob)
