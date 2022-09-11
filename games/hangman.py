import random

#opens and chooses random words from a hiden text file full of ranodm words
with open("words.txt", "r") as file:
	allText = file.read()

	words = list(map(str, allText.split()))

random_word = random.choice(words)

print("HANGMAN")
print("")
print("___")
print("|")
print("|")
print("|")
print("|")
print("------")

wrong_gues = 0
wrong_latters = []



encrypt= list(random_word)
word_split = list(random_word)
abc = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
for i in range(len(random_word)):
	for j in range(len(abc)):
		if encrypt[i].__contains__(abc[j]):
			encrypt[i] = '_'


while wrong_gues != 6:
	yes = False
	print(' '.join(encrypt))
	gues = input("Letter: ")
	if gues == "i give up":
		wrong_gues = 6
		break

	if gues == random_word:
		break
	for i in range(len(random_word)):
		if gues == word_split[i]:
			encrypt[i] = gues
			yes = True


	for i in range(wrong_gues):
		if gues == wrong_latters[i]:
			print("Already guesed")
			yes = True

	if yes == False:
		if gues != "":
			wrong_latters += gues
			wrong_gues += 1


	if wrong_gues == 0:
		print("")
		print("___")
		print("|")
		print("|")
		print("|")
		print("|")
		print("------")

	if wrong_gues == 1:
		print("")
		print("___")
		print("| o")
		print("|")
		print("|")
		print("|")
		print("------")

	if wrong_gues == 2:
		print("")
		print("___")
		print("| o")
		print("| |")
		print("|")
		print("|")
		print("------")

	if wrong_gues == 3:
		print("")
		print("___")
		print("| o")
		print("| |")
		print("|/")
		print("|")
		print("------")

	if wrong_gues == 4:
		print("")
		print("___")
		print("| o")
		print("| |")
		print("|/ \ ")
		print("|")
		print("------")

	if wrong_gues == 5:
		print("")
		print("___")
		print("| o")
		print("|/|")
		print("|/ \ ")
		print("|")
		print("------")

	if len(wrong_latters) > 0:
		print("Wrong gueses: ", " ".join(wrong_latters))

	if encrypt == word_split:
		break


if wrong_gues == 6:
	print("")
	print("___")
	print("| o")
	print("|/|\ ")
	print("|/ \ ")
	print("|")
	print("------")
	print("You Lost!")
	print("The corect word is ", random_word)
else:
	print("The corect word is ", random_word)
	print("You Won!")
