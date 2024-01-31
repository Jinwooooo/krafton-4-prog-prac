import sys
from math import inf
input = sys.stdin.readline

n = int(input().strip())
dp = [inf for _ in range(n + 1)]
dp[n] = 0

for idx in range(n,-1,-1):
	if idx % 3 == 0:
		dp[idx//3] = min(dp[idx//3], dp[idx] + 1)
	if idx % 2 == 0:
		dp[idx//2] = min(dp[idx//2], dp[idx] + 1)
	dp[idx-1] = min(dp[idx-1], dp[idx] + 1)

print(dp[1])
