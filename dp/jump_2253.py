import sys
input = sys.stdin.readline

destination, no_stone = map(int, input().strip().split(' '))

stone = {}
for _ in range(no_stone):
	stone[int(input().strip())] = True

dp = [{} for _ in range(destination + 1)]
dp[1][0] = 0

for position in range(1, destination + 1):
	for jmp, cnt in dp[position].items():
		for accel in range(-1, 2):
			branch = jmp - accel
			nxt_position = position + branch
			if branch > 0 and jmp < nxt_position <= destination and nxt_position not in stone:
				if branch in dp[nxt_position]:
					dp[nxt_position][branch] = min(dp[nxt_position][branch], cnt + 1)
				else:
					dp[nxt_position][branch] = cnt + 1

if len(dp[destination]) == 0:
    print(-1)
else:
    print(min(dp[destination].values()))


# import sys
# from collections import deque
# input = sys.stdin.readline

# def bfs_jump(destination, visited, stone):
# 	q = deque([(1,0,0)])
# 	while q:
# 		curr, incr, ctr = q.popleft()
# 		for branch in [incr + 1, incr, incr - 1]:
# 			if branch > 0:
# 				curr = curr + branch
# 				if curr == destination:
# 					return ctr + 1
# 				if (curr < destination) and (curr not in stone) and (branch not in visited[curr]):
# 					visited[curr].append(branch)
# 					q.append((curr, branch, ctr + 1))
# 		print(q)
# 	return -1

# destination, no_empty = map(int, input().strip().split(' '))
# visited = [[] for _ in range(destination + 1)]
# stone = set()
# for _ in range(no_empty):
# 	stone.add(int(input().strip()))

# print(bfs_jump(destination, visited, stone))