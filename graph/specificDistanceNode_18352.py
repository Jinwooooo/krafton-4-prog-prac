import sys
from collections import deque
from heapq import heappop, heappush

# [comeback later] there is some problem with this function
def bfs(graph, no_cities, target, start):
	visited = [False for _ in range(no_cities + 1)]
	queue = deque([start])

	min_dist = [0 for _ in range(no_cities + 1)]
	min_dist[start] = 0

	target_height = []

	while queue:
		node = queue.popleft()
		for neighbor in graph[node]:
			if not visited[neighbor]:
				visited[neighbor] = True
				queue.append(neighbor)
				min_dist[neighbor] = min_dist[node] + 1
				if min_dist[neighbor] == target:
					target_height.append(neighbor)

	print(min_dist)
	return target_height

def bfs_dijkstra(graph, no_cities, target, start):
	min_dist = [1e9 for _ in range(no_cities + 1)]
	min_dist[start] = 0
	heap = [(0, start)]

	target_height = []

	while heap:
		dist, curr_node = heappop(heap)

		if min_dist[curr_node] < dist:
			continue

		for neighbor in graph[curr_node]:
			update_dist = dist + 1
			if update_dist < min_dist[neighbor]:
				min_dist[neighbor] = update_dist
				heappush(heap, [update_dist, neighbor])
				if min_dist[neighbor] == target:
					target_height.append(neighbor)
	
	return target_height

no_cities, no_roads, target, start = map(int, sys.stdin.readline().strip().split(' '))
city = [[] for _ in range(0, no_cities + 1)]
for _ in range(no_roads):
	city_1, city_2 = map(int, sys.stdin.readline().strip().split(' '))
	city[city_1].append(city_2)

target_height_arr =  bfs_dijkstra(city, no_cities, target, start)
if not target_height_arr:
	print(-1)
else:
	target_height_arr.sort()
	for target_height_city in target_height_arr:
		print(target_height_city)

# [comeback later] there is some problem with this function
target_height_arr =  bfs(city, no_cities, target, start)
if not target_height_arr:
	print(-1)
else:
	target_height_arr.sort()
	for target_height_city in target_height_arr:
		print(target_height_city)

