import sys
from heapq import heappop, heappush

input = sys.stdin.readline

def dijkstra_maze(graph, visited, n):
	heap = []
	heappush(heap, (0,0,0))

	dx = [1,-1,0,0]
	dy = [0,0,1,-1]

	while heap:
		count, x, y = heappop(heap)
		visited[x][y] = True

		# reached destination end function
		if x == (n - 1) and y == (n - 1):
			return count

		# traverse up down right left
		for i in range(4):
			xx = x + dx[i]
			yy = y + dy[i]

			if (0 <= xx < n) and (0 <= yy < n) and not visited[xx][yy]:
				visited[xx][yy] = True

				if graph[xx][yy] == 1:
					heappush(heap, (count, xx, yy))
				else:
					heappush(heap, (count + 1, xx, yy))

n = int(input())
maze = []
for _ in range(n):
	maze.append(list(map(int, input().strip())))
visited = []
for _ in range(n):
	visited.append([False for _ in range(n)])

print(dijkstra_maze(maze, visited, n))


