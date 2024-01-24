import sys
from collections import deque

input = sys.stdin.readline

no_nodes, no_edges = map(int, input().strip().split(' '))
graph = [[] for _ in range(no_nodes + 1)]
in_degree = [0 for _ in range(no_nodes + 1)]
topological_arr = []

for i in range(no_edges):
	node_1, node_2 = map(int, input().strip().split(' '))
	graph[node_1].append(node_2)
	in_degree[node_2] += 1

queue = deque()

for ctr in range(1, no_nodes + 1):
	if in_degree[ctr] == 0:
		queue.append(ctr)

while queue:
	node = queue.popleft()
	topological_arr.append(node)
	for ctr in graph[node]:
		in_degree[ctr] -= 1
		if in_degree[ctr] == 0:
			queue.append(ctr)

print(*topological_arr)

