import sys
sys.setrecursionlimit(10**9)

def dfs_recur(graph, node, visited):
	if node not in visited:
		visited.append(node)
		for neighbor in graph[node]:
			dfs_recur(graph, neighbor, visited)
	return visited

# adjacency matrix generation
no_nodes, no_edges = map(int, sys.stdin.readline().strip().split(' '))
graph = {} 
for k in range(1, no_nodes+1):
	graph[k] = []
for _ in range(no_edges):
	ins_node, ins_edge = map(int, sys.stdin.readline().strip().split(' '))
	graph[ins_node].append(ins_edge)
	graph[ins_edge].append(ins_node)

# marking already used nodes; 0 = marked, 1 = unmarked (default)
mk = []
for k in range(1, no_nodes+1):
	mk.append(1)

part_ctr = 0
while True:
	# iteration initialization
	visited = []
	node = mk.index(1) + 1

	# iteration data update
	part_ctr += 1
	visited = dfs_recur(graph, node, visited)
	for vertex in visited:
		mk[vertex-1] = 0

	# iteration termination condition
	if sum(mk) == 0:
		break

print(part_ctr)
