import sys

def union_find(node, union_arr):
	if union_arr[node] != node:
		union_arr[node] = union_find(union_arr[node], union_arr)
	return union_arr[node]

no_nodes, no_edges = map(int, sys.stdin.readline().strip().split(' '))
union_arr = [i for i in range(0, no_nodes + 1)]
total_weight = 0
sorted_weight_arr = []

for _ in range(no_edges):
	node_1, node_2, weight = map(int, sys.stdin.readline().strip().split(' '))
	sorted_weight_arr.append([node_1, node_2, weight])
sorted_weight_arr.sort(key=lambda x: x[:][2])

# node, node, weight tuple
for node_1, node_2, weight in sorted_weight_arr:
	from_root = union_find(node_1, union_arr)
	to_root = union_find(node_2, union_arr)

	if from_root == to_root:
		continue

	total_weight += weight
	union_arr[to_root] = from_root

print(total_weight)
