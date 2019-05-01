#Problem 1

#U1, U5, U10, U20, U50, U100 coins

#How many ways to make U500?

#Dynamic Programming Solution

def main(target):
	coins = [1, 5, 10, 20, 50, 100]
	table = [1] + [0]*target
	for coin in coins:
		for i in range(coin, target+1):
			table[i] += table[i-coin]

	print("Number of ways U500 can be made:", table[target])

if __name__ == '__main__':
	main(500)