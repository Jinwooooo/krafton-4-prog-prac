import sys
input = sys.stdin.readline

def dfs_recur(graph, visited, pos_sol n, node, depth, curr_dist):
	if depth == n and graph[node][0] > 0:
		pos_sol.append(curr_dist + graph[node][0])
		return pos_sol

	for neighbor in range(n):
		if (not visited[neighbor] and graph[node][neighbor]):
			visited[neighbor] = True
			dfs_recur(graph, visited, pos_sol n, neighbor, depth + 1, curr_dist + graph[node][neighbor])
			visited[neighbor] = False

	return pos_sol

n = int(input().strip())

graph = []
for _ in range(n):
	graph.append(list(map(int, input().strip().split(' '))))

visited = [True] + [False for _ in range(n-1)]
pos_sol = []

print(min(dfs_recur(graph, visited, pos_sol n, 0, 1, 0)))

