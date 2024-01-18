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
			# debugging 전용
			return -1
	else:
		# debugging 전용
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

def solve_quad(mat, n):
	out_str = ''
	if n == 1:
		return out_str
	else:
		mat_partition = partition(mat, n)
		out_str = out_str + "("
		for part in mat_partition:
			is_same_val = is_same(part, n // 2)

			if is_same_val == 1:
				out_str = out_str + '1'
				part = mk_visit(part, n // 2)
			elif is_same_val == 0:
				out_str = out_str + '0'
				part = mk_visit(part, n // 2)

			temp_str = solve_quad(part, (n // 2))

			out_str = out_str + temp_str
		out_str = out_str + ")"	
	return out_str

mat = []
n = int(sys.stdin.readline())
for _ in range(n):
	mat.append(list(map(int, list(sys.stdin.readline().strip()))))

output_str = ''
base_case = is_same(mat, n)
if base_case == 0:
	output_str = output_str + '0'
elif base_case == 1:
	output_str = output_str + '1'
else:
	output_str = solve_quad(mat, n)

print(output_str.replace('()', '').replace('()', ''))