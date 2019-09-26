from random import randint

def diceroller(dice):
	n = int(dice.split("d")[0])
	m = int(dice.split("d")[1])
	res = 0
	scores = []
	for i in range(n):
		x = randint(1, m)
		scores.append(x)
		res += x
	print(res, " : ", end = "")
	for i in scores:
		print(i, " ", end = "")
	print("")

diceroller("6d4")
diceroller("1d2")
diceroller("1d8")
diceroller("3d6")
diceroller("4d20")
diceroller("100d100")
