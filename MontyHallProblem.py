# Implementation of the Monty Hall Problem

import random

count = 0
attempts = 10000
for a in range(attempts):
	# Inserting all goats behind doors
	goat = False
	dict = {number:goat for number in range(1,4)}
	
	# Removing one goat and inserting the car
	car = int(random.choice(''.join([str(i) for i in dict])))
	dict[car] = True
	
	# Contestant selecting a choice
	myChoice = int(random.choice(''.join([str(i) for i in dict])))

	# Monty Hall removing one goat and the corresponding door
	MontyHallChoice = int(random.choice(''.join([str(i) for i in dict if dict[i] == False and i != myChoice])))
	del dict[MontyHallChoice]
	
	# Contestant swapping choice for the remaining door
	myChoice = int(random.choice(''.join([str(i) for i in dict if i != myChoice])))

	# If the contestant won the car
	if dict[myChoice] == True:
		count += 1

# Average successes over attempts
print(count/attempts)
# Expected Value is 2/3