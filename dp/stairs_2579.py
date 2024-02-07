import sys
input = sys.stdin.readline

no_stairs = int(input())
stairs = [int(input()) for _ in range(no_stairs)]

dp = [0 for _ in range(no_stairs)]

if len(stairs) < 3:
	print(sum(stairs))
else:
	dp[0] = stairs[0]
	dp[1] = stairs[0] + stairs[1]

	for idx in range(2, no_stairs):
		# dp[idx - 3] + stairs[idx - 1] + stairs[idx] = 2 -> 1 -> 1
		# dp[idx - 2] + stairs[idx] = 2 -> 1
		dp[idx] = max(dp[idx - 3] + stairs[idx - 1] + stairs[idx], dp[idx - 2] + stairs[idx])

	print(dp[-1])
