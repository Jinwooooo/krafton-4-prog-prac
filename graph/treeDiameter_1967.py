import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def print_t(tree):
	for row in tree:
		print(row)
	print('---------------')

def dfs_leaf(tree, dist, leaves, node):
	visited = [True] + [False for _ in range(no_nodes)]
	if not visited[node]:
		visited[node] = True
		for neighbor in tree[node]:
			dist[neighbor] = max(dist[node], dist[])

no_nodes = int(input().strip())
tree = [[] for _ in range(no_nodes + 1)]
for _ in range(no_nodes - 1):
	node_1, node_2, weight = map(int, input().strip().split(' '))
	tree[node_1].append([node_2, weight])
	tree[node_2].append([node_1, weight])
leaves = []
for idx in range(no_nodes + 1):
	if len(tree[idx]) == 1:
		leaves.append(idx)
dist = [0 for _ in range(10**4 + 1)]

print_t(tree)
print(leaves)