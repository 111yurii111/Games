from words import words #from file words.py import the words array
from random import *
import time, os

No_of_words = int(input("Number of words: "))
os.system("clear")
#wait for input to start
input("Start")

list = ""
for i in range(No_of_words):#making the list of random words

    random_word = words[randint(0, 1523)]

    list = list + random_word + " "


print(list)
time.sleep(2)
start = time.time()
user_input = input("Write: ")#user writing
finish = time.time()


total_time = round(finish - start)

wpm = (round(60 / (total_time / No_of_words)))#counting words per minute
print(list)
print(user_input)
print(total_time, " Seconds")
print(wpm, "WPM")


mistakes = 0
count = 0

length = len(user_input) - No_of_words + 1


list = list.split()
user_input = user_input.split()

for i in range(len(list)):#cheking acuracy
    check1 = []
    for letter in user_input[i]:
        check1.append(letter)
    check2 = []
    for letter in list[i]:
        check2.append(letter)

    for j in range(len(check1)):
        for k in range(len(check1[j])):
            if check1[j][k] != check2[j][k]:
                mistakes += 1


acuracy = round(100 - (mistakes / length * 100))#calculating acuracy

print(f"Acuracy: {acuracy}%")
if mistakes != 0:
    print(f"Number or errors: {mistakes}")
