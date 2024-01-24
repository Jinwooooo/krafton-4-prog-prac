import sys

input = sys.stdin.readline

def dfs_recur(graph, node, visited, dfs_arr):
	if not visited[node]:
		visited[node] = True
		dfs_arr.append(node)
		for neighbor in graph[node]:
			dfs_recur(graph, neighbor, visited, dfs_arr)
	return dfs_arr

def dfs_operator(temp_val, curr_var, no_var, var_arr, opt_arr):
	max_val = -1e10
	min_val = 1e10
	if curr_var == no_var:
		max_val = max(max_val, temp_val)
		min_val = min(min_val, temp_val)
	else:
		for idx in range(4):
			if opt_arr[idx] > 0:
				if idx == 0:
					opt_arr[idx] -= 1
					dfs_operator()
				elif idx == 1:
					


# no_var = int(input())
# var_arr = list(map(int, input().strip().split(' ')))
# op_arr = list(map(int, input().strip().split(' ')))

# import sys
# MAX_ = -1e9
# MIN_ = 1e9


# def four_arith(n, ans):
#     global MAX_, MIN_, opt
#     if n == N:
#         MAX_ = max(MAX_, ans)
#         MIN_ = min(MIN_, ans)
#     else:
#         for x in range(4):
#             if opt[x] > 0:
#                 if x == 0:
#                     opt[x] -= 1
#                     four_arith(n + 1, ans + arr[n])
#                     opt[x] += 1
#                 elif x == 1:
#                     opt[x] -= 1
#                     four_arith(n + 1, ans - arr[n])
#                     opt[x] += 1
#                 elif x == 2:
#                     opt[x] -= 1
#                     four_arith(n + 1, ans * arr[n])
#                     opt[x] += 1
#                 elif x == 3:
#                     opt[x] -= 1
#                     four_arith(n + 1, int(ans / arr[n]))
#                     opt[x] += 1


# N = int(input())
# arr = list(map(int, sys.stdin.readline().strip().split()))
# opt = list(map(int, sys.stdin.readline().strip().split()))

# four_arith(1, arr[0])
# print(MAX_)
# print(MIN_)