import sys

n, target = map(int, sys.stdin.readline().strip().split(' '))

tree_arr = list(map(int, sys.stdin.readline().strip().split(' ')))
tree_arr.sort(reverse = True)

temp_sum = 0
idx_ctr = 0
dec_ctr = 0

while temp_sum < target:
	# special case : if only one tree left
	if n - idx_ctr > 2:
		temp_sum += (tree_arr[idx_ctr] - tree_arr[idx_ctr+1]) * (idx_ctr + 1)
		idx_ctr += 1
	else:
		temp_sum += tree_arr[idx_ctr] * (idx_ctr + 1)
		idx_ctr += 1


print('--------------------------')
print('[debug] temp_sum = ', temp_sum)
print('[debug] target = ', target)
while temp_sum < target:
	
	temp_sum -= idx_ctr
	dec_ctr += 1
# temp_sum += idx_ctr

print('------------------------')
print('[debug] idx_ctr = ', idx_ctr)
print('[debug] dec_ctr = ', dec_ctr)
print('[debug] temp_sum = ', temp_sum)
print(tree_arr[idx_ctr] + dec_ctr)

# 4 10
# 4 5 6 7
# 3 (1 + 2 + 3 + 4 = 10)
