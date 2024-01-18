import sys

in_val = int(sys.stdin.readline())
final_val = in_val
temp_val = 0
cycle_ctr = 0

while True:
	# separating values in to 10's and 1's and computing new value
	val_1 = (in_val // 10 + in_val % 10) % 10
	val_10 = (in_val % 10) * 10
	new_val = val_10 + val_1

	# updateing new values (keeping new_val to check for cycle condition)
	in_val = new_val
	cycle_ctr += 1

	if new_val == final_val:
		break

print(cycle_ctr)
