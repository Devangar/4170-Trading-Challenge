#Problem 3

#Find maximum sum of matrix where each value is part of unique row/column

#Variation of the Hungarian algorithm

test_matrix = [
[7, 53, 183, 439, 863], 
[497, 383, 563, 79, 973], 
[287, 63, 343, 169, 583], 
[627, 343, 773, 959, 943], 
[767, 473, 103, 699, 303]
]

matrix = [
[7, 53, 183, 439, 863, 497, 383, 563, 79, 973, 287, 63, 343, 169, 583], 
[627, 343, 773, 959, 943, 767, 473, 103, 699, 303, 957, 703, 583, 639, 913], 
[447, 283, 463, 29, 23, 487, 463, 993, 119, 883, 327, 493, 423, 159, 743], 
[217, 623, 3, 399, 853, 407, 103, 983, 89, 463, 290, 516, 212, 462, 350], 
[960, 376, 682, 962, 300, 780, 486, 502, 912, 800, 250, 346, 172, 812, 350], 
[870, 456, 192, 162, 593, 473, 915, 45, 989, 873, 823, 965, 425, 329, 803], 
[973, 965, 905, 919, 133, 673, 665, 235, 509, 613, 673, 815, 165, 992, 326], 
[322, 148, 972, 962, 286, 255, 941, 541, 265, 323, 925, 281, 601, 95, 973], 
[445, 721, 11, 525, 473, 65, 511, 164, 138, 672, 18, 428, 154, 448, 848], 
[414, 456, 310, 312, 798, 104, 566, 520, 302, 248, 694, 976, 430, 392, 198], 
[184, 829, 373, 181, 631, 101, 969, 613, 840, 740, 778, 458, 284, 760, 390], 
[821, 461, 843, 513, 17, 901, 711, 993, 293, 157, 274, 94, 192, 156, 574], 
[34, 124, 4, 878, 450, 476, 712, 914, 838, 669, 875, 299, 823, 329, 699], 
[815, 559, 813, 459, 522, 788, 168, 586, 966, 232, 308, 833, 251, 631, 107], 
[813, 883, 451, 509, 615, 77, 281, 613, 459, 205, 380, 274, 302, 35, 805]
]

SIZE = 15

def main():
	#Make all values negative for maximization
	for item in range(SIZE):
		for item2 in range(SIZE):
			matrix[item][item2] *= -1

	#Step 1
	for i in range(SIZE):
		vals = [x for x in matrix[i]]
		minval = min(vals)

		for j in range(SIZE):
			matrix[i][j] -= minval

	#Step 2
	transpose = list(zip(*matrix))
	for i in range(SIZE):
		vals = [x for x in transpose[i]]
		minval = min(vals)

		for j in range(SIZE):
			matrix[j][i] -= minval

	#Step 3
	total_covered = 0

	rows = list(range(SIZE))

	assigned_rows = set()
	assigned_cols = set()
	marked_cols = set()
	for i in range(SIZE):
		for j in range(SIZE):
			if (matrix[i][j] == 0) and (j not in assigned_cols):
				assigned_rows.add(i)
				assigned_cols.add(j)
				break

		
	marked_rows = [x for x in rows if x not in assigned_rows]
	marked_rows = set(marked_rows)

	for i in marked_rows:
		for j in range(SIZE):
			if (matrix[i][j] == 0) and (j not in marked_cols):
				marked_cols.add(j)

	for i in range(SIZE):
		for j in marked_cols:
			if (matrix[i][j] == 0) and (i not in marked_rows):
				marked_rows.add(i)

	#cover unmarked rows and marked cols
	unmarked_rows = [x for x in rows if x not in marked_rows]
	unmarked_cols = [x for x in rows if x not in marked_cols]
	unmarked_rows = set(unmarked_rows)
	unmarked_cols = set(unmarked_cols)

	total_covered = len(unmarked_rows) + len(marked_cols)

	#Step 4
	while total_covered < SIZE:
		min_val_left = 100000
		for i in marked_rows:
			for j in unmarked_cols:
				if matrix[i][j] < min_val_left:
					min_val_left = matrix[i][j]

		for i in marked_rows:
			for j in range(SIZE):
				matrix[i][j] -= min_val_left

		for i in range(SIZE):
			for j in marked_cols:
				matrix[i][j] += min_val_left

		for i in range(SIZE):
			for j in range(SIZE):
				if (matrix[i][j] == 0) and (j not in assigned_cols):
					assigned_rows.add(i)
					assigned_cols.add(j)
					break

			
		marked_rows = [x for x in rows if x not in assigned_rows]
		marked_rows = set(marked_rows)

		for i in marked_rows:
			for j in range(SIZE):
				if (matrix[i][j] == 0) and (j not in marked_cols):
					marked_cols.add(j)

		for i in range(SIZE):
			for j in marked_cols:
				if (test_matrix[i][j] == 0) and (i not in marked_rows):
					marked_rows.add(i)

		#cover unmarked rows and marked cols
		unmarked_rows = [x for x in rows if x not in marked_rows]
		unmarked_cols = [x for x in rows if x not in marked_cols]
		unmarked_rows = set(unmarked_rows)
		unmarked_cols = set(unmarked_cols)

		total_covered = len(unmarked_rows) + len(marked_cols)
		print(total_covered)
		

	print("done")


if __name__ == '__main__':
	main()