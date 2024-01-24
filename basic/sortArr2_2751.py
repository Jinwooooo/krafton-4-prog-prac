import sys

in_no = int(sys.stdin.readline())
arr = []

for _ in range(in_no):
	arr.append(int(sys.stdin.readline()))

arr.sort()

for arr_val in arr:
	print(arr_val)
