import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input().strip())
seq = list(map(int, input().strip().split(' ')))

# # O(n^2)
# dp = [1 for _ in range(n)]

# for row in range(1, n):
# 	for col in range(row):
# 		if seq[row] > seq[col]:
# 			dp[row] = max(dp[row], dp[col] + 1)

# print(max(dp))

# O(nlogn) by using binary search insertion to reduce time
dp = [float('inf') for _ in range(n + 1)]
dp[0] = float('-inf')
result = 0

for num in seq:
	idx = bisect_left(dp, num)
	dp[idx] = num
	result = max(result, idx)


if float('inf') in dp:
	end = dp.index(float('inf'))
	dp = dp[1:end]
else:
	dp = dp[1:]

print('longest increasing subsequence ctr = ', result)
print('longest increasing subsequence list = ', dp)

# def findPlace(e):
# 	start = 0
# 	end = len(LIS) - 1

# 	while start <= end:
# 		mid = (start + end) // 2
	
# 		if LIS[mid] == e:
# 			return mid
# 		elif LIS[mid] < e:
# 			start = mid + 1
# 		else:
# 			end = mid - 1

# 	return start