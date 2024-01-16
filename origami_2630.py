import sys

def prettify(mat):
	for row in mat:
		print(row)
	print('-----------------------')

def is_same(mat, n):
	k = n*n
	mat_sum = sum(map(sum, mat))

	if mat_sum == k:
		return 1
	elif mat_sum == 0:
		return 0
	else:
		return -1

def partition(mat, n):
	pivot = n // 2
	print(pivot)

	ul = [row[:pivot] for row in mat[:pivot]]
	ur = [row[pivot:] for row in mat[:pivot]]
	ll = [row[:pivot] for row in mat[pivot:]]
	lr = [row[pivot:] for row in mat[pivot:]]

	return ul, ur, ll, lr

mat8_size = 8
mat8 = [[1, 1, 0, 0, 0, 0, 1, 1],
		[1, 1, 0, 0, 0, 0, 1, 1],
		[0, 0, 0, 0, 1, 1, 0, 0],
		[0, 0, 0, 0, 1, 1, 0, 0],
		[1, 0, 0, 0, 1, 1, 1, 1],
		[0, 1, 0, 0, 1, 1, 1, 1],
		[0, 0, 1, 1, 1, 1, 1, 1],
		[0, 0, 1, 1, 1, 1, 1, 1]]
mat4_size = 4
mat4 = [[1, 1, 0, 1],
		[1, 1, 1, 0],
		[1, 1, 0, 0],
		[0, 1, 0, 0]]



ul, ur, ll, lr = partition(mat8, mat8_size)
prettify(ul)
prettify(ur)
prettify(ll)
prettify(lr)

