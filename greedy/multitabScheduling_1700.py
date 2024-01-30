import sys
from collections import deque

input = sys.stdin.readline

def get_swap_app(holes, order):
	temp_arr = []

	# input val is less than 100 so 999 works in this problem
	for val in holes:
		if val in order:
			temp_arr.append(order.index(val))
		else:
			temp_arr.append(999)

	max_index = 0
	for i in range(1, len(temp_arr)):
		if temp_arr[i] > temp_arr[max_index]:
			max_index = i

	return max_index


no_holes, no_app = map(int, input().strip().split(' '))
order = list(map(int, input().strip().split(' ')))

holes = []

# init
idx = 0
while len(holes) != no_holes:
	if order[idx] not in holes:
		holes.append(order[idx])
		idx += 1
	else:
		idx += 1

	if idx == len(order):
		break

# deque to popleft
order = deque(order[idx:])

# iteration case
change_ctr = 0
while len(order) >= len(holes):
	curr_app = order.popleft()
	if curr_app not in holes:
		chg_idx = get_swap_app(holes, order)
		holes[chg_idx] = curr_app
		change_ctr += 1

# when leftover order is less or equal to number of holes
for val in order:
	if val not in holes:
		change_ctr += 1

print(change_ctr)