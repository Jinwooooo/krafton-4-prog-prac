import sys
input = sys.stdin.readline

line = [int(input().strip()) for _ in range(int(input().strip()))]
dp = [1 for _ in range(len(line))]

# finding longest increasing subsequence
for i in range(1, len(line)):
	for j in range(i):
		if line[i] > line[j]:
			dp[i] = max(dp[i], dp[j] + 1)

# since max(dp) already is in the right order, other element move is the least move
print(len(line) - max(dp))
