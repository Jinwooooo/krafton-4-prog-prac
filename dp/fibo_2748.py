import sys

input = sys.stdin.readline

pos = int(input())

dp = [0 for _ in range(90)]
dp[0] = 1
dp[1] = 1
dp[2] = 2

for idx in range(2, pos):
	dp[idx] = dp[idx - 1] + dp[idx - 2]

print(dp[pos - 1])