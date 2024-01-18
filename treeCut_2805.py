import sys

def chk_tree(n, tree_arr, target, mid):
	temp_sum = 0
	for i in range(n):
		if tree_arr[i] > mid:
			temp_sum += tree_arr[i] - mid
		if temp_sum >= target:
			return True
	return False

n, target = map(int, sys.stdin.readline().strip().split(' '))
tree_arr = list(map(int, sys.stdin.readline().strip().split(' ')))

left = 0
right = 2000000000
mid = 0
max_height = 0

while(left <= right):
	mid = (left + right) // 2;
	if chk_tree(n, tree_arr, target, mid):
		max_height = mid;
		left = mid + 1
	else:
		right = mid - 1

print(max_height)
