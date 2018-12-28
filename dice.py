def multi_roll(rolls, sides):
	import random
	a = 0
	total = 0
	working = 0

	while a < rolls:
		a += 1
		working = random.randint(1, sides)
		total += working
		print("Roll #", a, ": ", working)
	print("Total is: ", total)


while True:
	rolls = int(input("How many rolls?"))
	sides = int(input("Enter the dice that you want to roll: "))
	multi_roll(rolls, sides)
	while True:
		answer = input('Roll again? (y/n): ')
		if answer in ('y', 'n'):
			break
		print ('Invalid input.')
	if answer == 'y':
		continue
	else:
		print ('goodbye')
		break


