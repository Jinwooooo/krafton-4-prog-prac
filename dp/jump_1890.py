import sys
input = sys.stdin.readline

n = int(input())
mat = [list(map(int, input().strip().split(' '))) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1

for row in range(n):
	for col in range(n):
		d = mat[row][col]

		# finding valid jumps
		prow = row + d
		pcol = col + d

		# 0 in dp means it is not a valid move from previous iteration
		if dp[row][col] == 0:
			continue

		if row == n - 1 and col == n - 1:
			break

		# if down and right tile are valid jumps, min and inc
		if prow >= 0 and prow < n and pcol >= 0 and pcol < n:
			dp[prow][col] += dp[row][col]
			dp[row][pcol] += dp[row][col]
		elif prow >= 0 and prow < n:
			dp[prow][col] += dp[row][col]
		elif pcol >= 0 and pcol < n:
			dp[row][pcol] += dp[row][col]

print(dp[-1][-1])
