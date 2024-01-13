import sys

max_val = 0
max_index = 1

for i in range(0,9):
	curr_val = int(sys.stdin.readline())

	if max_val < curr_val:
		max_val = curr_val
		max_index = i+1

print(max_val)
print(max_index)

