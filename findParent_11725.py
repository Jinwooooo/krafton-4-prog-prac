import sys
from collections import deque
sys.setrecursionlimit(10**6)

no_nodes = int(sys.stdin.readline())
graph = [[] for i in range(0, no_nodes + 1)]
parent_arr = [0 for i in range(0, no_nodes + 1)]

for _ in range(no_nodes - 1):
	node, edge = map(int, sys.stdin.readline().strip().split(' '))
	graph[node].append(edge)
	graph[edge].append(node)

visited = [False] * (no_nodes + 1)
stack = deque([1])

while stack:
	curr_pos = stack.pop()
	visited[curr_pos] = True

	for neighbor in graph[curr_pos]:
		if not visited[neighbor]:
			parent_arr[neighbor] = curr_pos
			stack.add(neighbor)

for a in parent_arr[2:]:
	print(a)
