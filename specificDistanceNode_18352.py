import sys
from collections import deque

def bfs(graph, start):
	visited = set()
	queue = deque([start])
	result = []

	while queue:
		node = queue.popleft()
		if node not in visited:
			visited.add(node)
			result.append(node)
			for neighbor in graph[node]:
				if neighbor not in visited:
					queue.extend([neighbor])

	return result

no_city, no_roads, dist, start = map(int, sys.stdin.readline().strip().split(' '))
city = [[] for _ in range(0, no_roads + 1)]
min_dist = [-1 for _ in range(0, no_roads + 1)]

for _ in range(no_roads):
	city_1, city_2 = map(int, sys.stdin.readline().strip().split(' '))
	city[city_1].append(city_2)
	city[city_2].append(city_1)

print(min_dist)
print(city)
print(bfs(city, start))


