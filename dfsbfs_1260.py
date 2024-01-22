import sys
from collections import deque

def dfs_stack(graph, start):
	# intializing
	for m in graph.values():
		m.sort(reverse=True)
	visited = [start]
	stack = []

	# base case (root node neighbors)
	for nodes in graph[start]:
		stack.append(nodes)

	# iteration case (until stack is empty)
	while stack:
		curr_pos = stack.pop()
		if curr_pos not in visited:
			visited.append(curr_pos)
			for nodes in graph[curr_pos]:
				stack.append(nodes)
	return visited

def dfs_recur(graph, node, visited):
	if node not in visited:
		visited.append(node)
		for neighbor in graph[node]:
			dfs_recur(graph, neighbor, visited)
	return visited

def bfs(graph, start):
	# initializing
	for m in graph.values():
		m.sort()
	visited = [start]
	queue = deque([])

	# base case (root node neighbors)
	for nodes in graph[start]:
		queue.append(nodes)

	# iteration case (until queue is empty)
	while queue:
		curr_pos = queue.popleft()
		if curr_pos not in visited:
			visited.append(curr_pos)
		for nodes in graph[curr_pos]:
			if nodes not in visited:
				queue.append(nodes)

	return visited

no_nodes, no_edges, start = map(int, sys.stdin.readline().strip().split(' '))
graph = {}
for k in range(1, no_nodes+1):
	graph[k] = []
for _ in range(no_edges):
	ins_node, ins_edge = map(int, sys.stdin.readline().strip().split(' '))
	graph[ins_node].append(ins_edge)
	graph[ins_edge].append(ins_node)


print(*dfs_stack(graph, start))

print(*bfs(graph, start))

for m in graph.values():
	m.sort()
visited = []
print(*dfs_recur(graph, start, visited))


# no_nodes = 4
# no_edges = 5
# start = 1
# no_nodes = 5
# no_edges = 5
# start = 3
# no_nodes = 1000
# no_edges = 1
# start = 1000

# test_arr = [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4]]
# test_arr = [[5, 4], [5, 2], [1, 2], [3, 4], [3, 1]]
# test_arr = [[999, 1000]]

# graph = {}
# for k in range(1, no_nodes+1):
# 	graph[k] = []

# for n in test_arr:
# 	graph[n[0]].append(n[1])
# 	graph[n[1]].append(n[0])

# print(graph)



