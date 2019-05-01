#Problem 2

#Gregor: 1, 2, 3, 4, 5 -> 8 dice
#Oberyn: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 -> 4 dice
#Highest total wins

#Probability that Gregor beats Oberyn?

import itertools

def permutations(dice, num_dice, sum_dice):
	perms = itertools.product(dice, repeat=num_dice)
	for i in perms:
		if sum(i) == sum_dice:
			yield i

def main():
	gregor_dice = [1, 2, 3, 4, 5]
	oberyn_dice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	gregor_total_possibilities = 1
	oberyn_total_possibilities = 1
	for i in range(8):
		gregor_total_possibilities = gregor_total_possibilities * len(gregor_dice)
	for j in range(4):
		oberyn_total_possibilities = oberyn_total_possibilities * len(oberyn_dice)

	total_possibilities = gregor_total_possibilities * oberyn_total_possibilities

	#Calculate desired outcomes
	possible_gregor_rolls = list(range(8, 41))
	possible_oberyn_rolls = list(range(4, 41))

	desired_outcomes = 0
	for i in possible_gregor_rolls:
		for j in possible_oberyn_rolls:
			if i > j:
				desired_outcomes += (len(list(permutations(gregor_dice, 8, i))) * len(list(permutations(oberyn_dice, 4, j))))

	print("Probability that Gregor beats Oberyn =", desired_outcomes, "/", total_possibilities, "~ 58.3%")

if __name__ == '__main__':
	main()