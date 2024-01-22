
def bfs(graph, start):
	visited = set()
	queue = deque([start])
	result = []

	while queue:
		node = queue.popleft()
		if node not in visited:
			visited.add(node)
			result.append(node)
			for neighbor in graph[node]:
				if neighbor not in visited:
					queue.extend([neighbor])

	return result

def dfs_recur(graph, node, visited):
	if node not in visited:
		visited.append(node)
		for neighbor in graph[node]:
			dfs_recur(graph, neighbor, visited)
	return visited