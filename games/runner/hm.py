a = 0
while True:
	import random, os
	with open(".words.txt", "r") as file:
		allText = file.read()

		words = list(map(str, allText.split()))

		w = random.choice(words)

	print("HANGMAN")
	print("")
	print("___")
	print("|")
	print("|")
	print("|")
	print("|")
	print("------")

	s = 0
	wg = ['','','','','','']
	z = -1

	def split(word):
	    return [char for char in word]

	ww = split(w)
	c = split(w)
	a = 0
	b = 0
	l = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	for i in range(len(w)):
		b = 0
		for i in range(len(l)):
			if ww[a].__contains__(l[b]):
				ww[a] = '_'
			b = b + 1
		a = a + 1



	while s != 6:
		y = ''
		print(' '.join(ww))
		g = input("Letter: ")
		if g == "i give up":
			s = 6
			break
		if g == w:
			break
		a = 0
		while a != len(w):
			if g == c[a]:
				ww[a] = g
				y = True
			a = a + 1




		if y != True:
			z += 1
			wg[z] = g
			s += 1


		if s == 0:
			print("")
			print("___")
			print("|")
			print("|")
			print("|")
			print("|")
			print("------")

		if s == 1:
			print("")
			print("___")
			print("| o")
			print("|")
			print("|")
			print("|")
			print("------")

		if s == 2:
			print("")
			print("___")
			print("| o")
			print("| |")
			print("|")
			print("|")
			print("------")

		if s == 3:
			print("")
			print("___")
			print("| o")
			print("| |")
			print("|/")
			print("|")
			print("------")

		if s == 4:
			print("")
			print("___")
			print("| o")
			print("| |")
			print("|/ \ ")
			print("|")
			print("------")

		if s == 5:
			print("")
			print("___")
			print("| o")
			print("|/|")
			print("|/ \ ")
			print("|")
			print("------")

		print("Wrong gueses: ", " ".join(wg))

		if ww == c:
			break

	if s == 6:
		print("")
		print("___")
		print("| o")
		print("|/|\ ")
		print("|/ \ ")
		print("|")
		print("------")
		print("You Loose!")
		print("The corect word is ", w)
		a += 1
		if a >= 1:
			inp = input("Do you want to flip a coin to skip hangman?: ")
			if inp == "yes":
				os.system("python3 ct.py")
				break
			else:
				continue
		print("again?")
		input()

	else:
		print("You won!")
		print("Press enter to continue")
		input()
		os.system("python3 lvl3p2.py")
