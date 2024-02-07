import sys
input = sys.stdin.readline

no_seq = int(input().strip())
seq = list(map(int, input().strip().split(' ')))

dp = [0 for _ in range(no_seq)]
dp[0] = 1

for idx in range(1, no_seq):
	if seq[idx] > seq[idx - 1]:
		dp[idx] = dp[idx - 1] + 1
	else:
		dp[idx] = 1

print(sum(dp))
