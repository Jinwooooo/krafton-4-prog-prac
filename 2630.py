import sys
from itertools import groupby

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

def is_same(arr, index):
	chk_val = arr[index]
	cond = True
	for arr_val in arr:
		if arr_val != arr[index]:
			cond = False
			break
	return cond

mat8_size = 8
mat8 = [1, 1, 0, 0, 0, 0, 1, 1,
		1, 1, 0, 0, 0, 0, 1, 1,
		0, 0, 0, 0, 1, 1, 0, 0,
		0, 0, 0, 0, 1, 1, 0, 0,
		1, 0, 0, 0, 1, 1, 1, 1,
		0, 1, 0, 0, 1, 1, 1, 1,
		0, 0, 1, 1, 1, 1, 1, 1,
		0, 0, 1, 1, 1, 1, 1, 1]
mat4_size = 4
mat4 = [1, 1, 0, 1,
		1, 1, 1, 0,
		1, 1, 0, 0,
		0, 1, 0, 0]

ctr_0 = 0
ctr_1 = 0

mat4_index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
elements_per_tuple = 2

mat_tuples = []

for i in range(0, (mat4_size*mat4_size), elements_per_tuple):
    tuple_of_elements = tuple(mat4_index[i:i + elements_per_tuple])
    mat_tuples.append(tuple_of_elements)

print(mat_tuples)
print(type(mat_tuples))



# mat4_index = []

# temp_size = mat4_size // 2

# mat_tuples = []
# for i in range(0, len(mat4_index), temp_size):
# 	tuple_of_elements = tuple(mat[i:i + temp_size])
# 	mat_tuples.append(temp_size)

# print(mat_tuples)
