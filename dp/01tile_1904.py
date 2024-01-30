import sys

input = sys.stdin.readline

pos = int(input())

if pos == 0:
	print(0)
elif pos == 1:
	print(1)
elif pos == 2:
	print(2)
elif pos == 3:
	print(3)
else:
	dp = [0 for _ in range(int(pos + 1))]

	dp[0] = 1
	dp[1] = 2
	dp[2] = 3

	for idx in range(2, pos):
		dp[idx] = (dp[idx - 1] + dp[idx - 2]) % 15746

	print(dp[pos - 1])
