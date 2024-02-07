import sys
input = sys.stdin.readline

no_days = int(input())
schedule = [list(map(int, input().strip().split(' '))) for _ in range(no_days)]

dp = [0 for _ in range(no_days + 1)]

for day in range(no_days):
	for curr in range(day + schedule[day][0], no_days + 1):
		if dp[curr] < dp[day] + schedule[day][1]:
			dp[curr] = dp[day] + schedule[day][1]

print(dp[-1])
