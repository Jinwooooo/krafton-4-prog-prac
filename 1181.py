import sys

in_no = int(sys.stdin.readline())
in_arr = []

for _ in range(0, in_no):
	# [LESSON] if possible do not traverse through the list in for loops
	# tried to avoid having multiple occurence, which caused the time taken increase exponentially
	val = sys.stdin.readline().replace('\n', '')
	in_arr.append(val)

in_arr = list(set(in_arr)) # complexity = n (like quick sort most likely lower complexity = 1)
in_arr.sort() # complexity = nlogn
# [LESSON] utilize key in python sort library
in_arr.sort(key = len) # complexity = nlogn

for a in in_arr:
	print(a)

##############
# 환상의 똥꼬쇼 #
##############

# in_len_arr = []
# out_arr = []

# for i in in_arr:
# 	in_len_arr.append(len(i))

# ctr = len(in_arr)
# ele_len = 1

# while ctr != 0:
# 	# complexity = n (traverse the whole list)
# 	# returns all index of the condition value
# 	index_multi = [x for x, y in enumerate(in_len_arr) if y == ele_len]

# 	for index in index_multi:
# 		out_arr.append(in_arr[index])

# 	ele_len += 1
# 	ctr -= len(index_multi)

# for a in out_arr:
# 	print(a)
