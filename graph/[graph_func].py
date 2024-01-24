
def bfs(graph, start):
	visited = set()
	queue = deque([start])
	result = []

	while queue:
		node = queue.popleft()
		if node not in visited:
			visited.add(node)
			result.append(node)
			queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
			# for neighbor in graph[node]:
			# 	if neighbor not in visited:
			# 		queue.extend([neighbor])

	return result

def dfs_recur(graph, node, visited):
	if node not in visited:
		visited.append(node)
		for neighbor in graph[node]:
			dfs_recur(graph, neighbor, visited)
	return visited

def dfs_stack(graph, start):
	visited = set()
	stack = [start]

	while stack:
		node = stack.pop()
		if node not in visited:
			visited.add(node)
			stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
			# for neighbor in graph[node]:
			# 	if neighbor not in visited:
			# 		stack.extend([neighbor])