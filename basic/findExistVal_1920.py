import sys

def binary_search(arr, low, high, val):
	if high >= low:
		mid = (high + low) // 2

		if arr[mid] == val:
			return True
		elif arr[mid] > val:
			return binary_search(arr, low, mid - 1, val)
		else:
			return binary_search(arr, mid + 1, high, val)
	else:
		return False

trash_1 = int(sys.stdin.readline())
sel_arr = list(map(int, sys.stdin.readline().strip().split(' ')))
trash_2 = int(sys.stdin.readline())
chk_arr = list(map(int, sys.stdin.readline().strip().split(' ')))
out_arr = []

sel_arr.sort()

for chk_val in chk_arr:
	exists = binary_search(sel_arr, 0, len(sel_arr) - 1, chk_val)
	if exists == True:
		out_arr.append(1)
	else:
		out_arr.append(0)

for n in out_arr:
	print(n)