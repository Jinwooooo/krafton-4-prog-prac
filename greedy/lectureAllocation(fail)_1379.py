import sys
from heapq import heappop, heappush

input = sys.stdin.readline

min_hall = int(input())
lecture = [list(map(int, input().strip().split(' '))) for _ in range(min_hall)]
lecture.sort(key = lambda x: (x[2], x[1]))

hall = []
used = []

for no, start, end in lecture:
	if not hall or hall[0] > start:
		heappush(hall, end)
		used.append(len(hall))
	else:
		heappop(hall)
		heappush(hall, end)
		used.append(len(hall))

print(len(hall))
for hall in used:
	print(hall)
