import sys

def retrieve_sorted_pos(arr, val):
	# [Special Case] insert value smaller than minimum val in list
	if val <= arr[0]:
		return -1
	# [Special Case] insert value larger than maximum val in list
	elif val >= arr[-1]:
		return len(arr) - 1
	else:
		return binary_search(arr, 0, len(arr) - 1, val)

# O(logn) to find the index to insert
def binary_search(arr, low, high, val):
	if high >= low:
		mid = (high + low) // 2

		if arr[mid] == val:
			return mid
		elif arr[mid] > val:
			return binary_search(arr, low, mid - 1, val)
		else:
			return binary_search(arr, mid + 1, high, val)
	else:
		return high

# # [DEBUG]
# arr_len = 1
# val = 2
# arr = [1]

# insert_index = retrieve_sorted_pos(arr, val)
# print(insert_index)
# arr.insert(insert_index + 1, val)
# print(arr)

arr = []

in_no = int(sys.stdin.readline())
# input first val
arr.append(int(sys.stdin.readline()))

for _ in range(1, in_no):
	arr_ele = int(sys.stdin.readline())
	insert_index = retrieve_sorted_pos(arr, arr_ele)
	arr.insert(insert_index + 1, arr_ele)

for arr_val in arr:
	print(arr_val)
