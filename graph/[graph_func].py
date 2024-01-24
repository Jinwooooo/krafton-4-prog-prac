# bfs, dfs, union_find, dijkstra

def bfs(graph, start, visited):
	visited # = [False for _ in range(no_nodes)]
	queue = deque([start])
	dfs_arr = []

	while queue:
		node = queue.popleft()
		if not visited[node]:
			visited[node] = True
			dfs_arr.append(node)
			queue.extend(neighbor for neighbor in graph[node] if not visited[neighbor])
			# for neighbor in graph[node]:
			# 	if not visited[neighbor]:
			# 		queue.extend([neighbor])

	return result

def dfs_recur(graph, node, visited, dfs_arr):
	if not visited[node]:
		visited[node] = True
		dfs_arr.append(node)
		for neighbor in graph[node]:
			dfs_recur(graph, neighbor, visited, dfs_arr)
	return dfs_arr

def dfs_stack(graph, start):
	visited # = [False for _ in range(no_nodes)]
	stack = [start]

	while stack:
		node = stack.pop()
		if not visited[node]:
			visited[node] = True
			stack.extend(neighbor for neighbor in graph[node] if not visited[neighbor])
			# for neighbor in graph[node]:
			# 	if not visited[neighbor]:
			# 		stack.extend([neighbor])

def union_find(node, union_arr):
	if union_arr[node] != node:
		union_arr[node] = union_find(union_arr[node], union_arr)
	return union_arr[node]


def dijkstra(graph, start, target, n):
	visited = [False for _ in range(n + 1)]
	visited[start] = True
	min_d = [1e9 for _ in range(n + 1)]
	min_d[start] = 0
	heap = [(0, start)]

	while heap:
		cr_d, cr_n = heappop(heap)
		
		if cr_n in visited:
			continue
		visited[cr_n] = False

		for nx_n, nx_d in graph[cr_n]:
			new_d = cr_d + nx_d
			if new_d < min_d[nx_n]:
				min_d[nx_n] = new_d
				heappush(heap, (new_d, new_n))

	return min_d



