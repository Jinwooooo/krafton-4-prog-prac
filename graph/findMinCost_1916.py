import sys
from heapq import heappop, heappush

input = sys.stdin.readline

def dijkstra(graph, start, end, no_city):
	min_dist = [1e9 for _ in range(no_city + 1)]
	min_dist[start] = 0
	heap = [(start, 0)]

	while heap:
		curr_node, dist = heappop(heap)
		
		if min_dist[curr_node] < dist:
			continue

		for neigh_node, neigh_dist in graph[curr_node]:
			update_dist = dist + neigh_dist
			if update_dist < min_dist[neigh_node]:
				min_dist[neigh_node] = update_dist
				heappush(heap, [neigh_node, update_dist])

	return min_dist

no_city = int(input())
no_bus = int(input())
city = [[] for _ in range(no_city + 1)]
for _ in range(no_bus):
	node_1, node_2, dist = map(int, input().strip().split(' '))
	city[node_1].append((node_2, dist))
start, end = map(int, input().strip().split(' '))

print(dijkstra(city, start, end, no_city)[end])
