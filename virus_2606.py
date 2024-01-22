import sys
sys.setrecursionlimit(10**6)

def dfs_recur(graph, node, visited):
	if node not in visited:
		visited.append(node)
		for neighbor in graph[node]:
			dfs_recur(graph, neighbor, visited)
	return visited

no_nodes = int(sys.stdin.readline())
no_edges = int(sys.stdin.readline())
graph = [[] for i in range(0, no_nodes + 1)]

for _ in range(no_edges):
	node, edge = map(int, sys.stdin.readline().strip().split(' '))
	graph[node].append(edge)
	graph[edge].append(node)

visited = []
print(len(dfs_recur(graph, 1, visited)[1:]))
