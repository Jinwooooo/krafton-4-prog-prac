import sys

def is_same(mat, n):
	k = n*n
	if mat[0][0] != -1:	
		mat_sum = sum(map(sum, mat))

		if mat_sum == k:
			return 1
		elif mat_sum == 0:
			return 0
		else:
			return -1
	else:
		return -2

def mk_visit(mat, n):
	for x in range(n):
		for y in range(n):
			mat[x][y] = -1

	return mat

def partition(mat, n):
	pivot = n // 2

	ul = [row[:pivot] for row in mat[:pivot]]
	ur = [row[pivot:] for row in mat[:pivot]]
	ll = [row[:pivot] for row in mat[pivot:]]
	lr = [row[pivot:] for row in mat[pivot:]]

	return ul, ur, ll, lr

def solve_origami(mat, n):
	ctr_0 = 0
	ctr_1 = 0
	if n == 1:
		return ctr_0, ctr_1
	else:
		mat_partition = partition(mat, n)
		for part in mat_partition:
			is_same_val = is_same(part, n // 2)

			if is_same_val == 1:
				ctr_1 += 1
				part = mk_visit(part, n // 2)
			elif is_same_val == 0:
				ctr_0 += 1
				part = mk_visit(part, n // 2)

			temp_ctr0, temp_ctr1 = solve_origami(part, (n // 2))
			ctr_0 += temp_ctr0
			ctr_1 += temp_ctr1

	return ctr_0, ctr_1

mat = []
n = int(sys.stdin.readline())
for _ in range(n):
	mat.append(list(map(int, sys.stdin.readline().strip().split(' '))))

no_0set = 0
no_1set = 0
base_case = is_same(mat, n)
if base_case == 0:
	no_0set = 1
elif base_case == 1:
	no_1set = 1
else:
	no_0set, no_1set = solve_origami(mat, n)

print(no_0set)
print(no_1set)



