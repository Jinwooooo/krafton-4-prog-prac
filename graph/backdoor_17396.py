import sys
from math import inf
from heapq import heappush, heappop
input = sys.stdin.readline

def dijkstra_rift(graph, sight, no_nodes):
	h = [(0,0)]
	dist = [0] + [inf for _ in range(no_nodes - 1)]

	while h:
		d, curr_node = heappop(h)

		# reached destination end dijkstra
		if curr_node == no_nodes - 1:
			return d

		# if current distance is bigger than min distance ignore and continue
		if dist[curr_node] < d:
			continue

		for adj_node, adj_d in graph[curr_node]:
			new_d = d + adj_d
			# checking if update is min and not seen by enemy
			if new_d < dist[adj_node] and not sight[adj_node]:
				dist[adj_node] = new_d
				heappush(h, (new_d, adj_node))

	return dist[no_nodes - 1]


no_nodes, no_edges = map(int, input().strip().split(' '))
sight = list(map(int, input().strip().split(' ')))
sight[no_nodes - 1] = 0 # because nexus sight is inevitable
graph = [[] for _ in range(no_nodes)]

# optimization 1 - using adj list instead of full adj matrix
for _ in range(no_edges):
	node_1, node_2, d = map(int, input().strip().split(' '))
	graph[node_1].append((node_2, d))
	graph[node_2].append((node_1, d))

min_dist = dijkstra_rift(graph, sight, no_nodes)
if min_dist != inf:
	print(min_dist)
else:
	print(-1)
