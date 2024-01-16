import sys

def josephus(curr_arr, k, index):
	if len(curr_arr) == 1:
		out_arr.append(curr_arr[0])
		return

	index = ((index + k) % len(curr_arr))
	out_arr.append(curr_arr.pop(index))
	
	josephus(curr_arr, k, index)

# recur limit
sys.setrecursionlimit(10**6)

# system input
in_tuple = list(map(int, input().split(' ')))
curr_arr = []
out_arr = []

# creating circular list
for i in range(in_tuple[0]):
	curr_arr.append(i+1)
 
n = in_tuple[0]
k = in_tuple[1] - 1
index = 0

josephus(curr_arr, k, index)

out_arr = ', '.join(list(map(str, out_arr)))
print('<' + out_arr + '>')
