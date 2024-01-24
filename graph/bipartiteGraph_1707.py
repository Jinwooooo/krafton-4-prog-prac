import sys
sys.setrecursionlimit(10**6)

def dfs_recur_bipart(graph, node, color_arr, color_val):
	if color_arr[node] == -1:
		color_arr[node] = color_val
		for neighbor in graph[node]:
			result = dfs_recur_bipart(graph, neighbor, color_arr, 1 - color_val)
			if not result:
				return False
			elif color_arr[neighbor] == color_val:
				return False

	return True

no_cases = int(sys.stdin.readline())

for _ in range(no_cases):
	# initializing variables
	no_nodes, no_edges = map(int, sys.stdin.readline().strip().split(' '))
	graph = [[] for i in range(0, no_nodes + 1)]
	color_arr = [-1 for _ in range(-1, no_nodes + 1)]

	for _ in range(no_edges):
		node_1, node_2 = map(int, sys.stdin.readline().strip().split(' '))
		graph[node_1].append(node_2)
		graph[node_2].append(node_1)

	is_bipartite = True

	for start in range(1, no_nodes + 1):
		if color_arr[start] == -1:
			is_bipartite = dfs_recur_bipart(graph, start, color_arr, 0)
			if not is_bipartite:
				break

	if is_bipartite:
		print("YES")
	else:
		print("NO")

