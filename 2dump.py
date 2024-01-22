def dfs_recur_bipart(graph, node, visited, color_arr, color_val):
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            if color_arr[neighbor] == -1:
                # Flip the color for the next level of recursion
                next_color_val = 1 - color_val
                color_arr[neighbor] = next_color_val
                print('***** in color_arr[neighbor] == -1 *****')
                print('curr node = ', neighbor)
                print('curr color_arr = ', next_color_val)
                print('curr color_arr = ', color_arr)
                print('-------------------------')
                result, visited = dfs_recur_bipart(graph, neighbor, visited, color_arr, next_color_val)
                if not result:
                    return False, visited
            elif color_arr[neighbor] == color_val:
                print('***** in color_arr[neighbor] == color_val *****')
                print('curr node = ', neighbor)
                print('curr color_arr = ', color_val)
                print('curr color_arr = ', color_arr)
                print('-------------------------')
                return False, visited
    return True, visited

# Example usage:
graph = {1: [3], 2: [3], 3: [1, 2]}
start_node = 1
visited = []
color_arr = {node: -1 for node in graph}
color_arr[start_node] = 0

is_bipartite, _ = dfs_recur_bipart(graph, start_node, visited, color_arr, 0)
print('Is Bipartite:', is_bipartite)



# import sys
# from collections import deque

# def bfs(graph, start):
#     # initializing
#     for m in graph.values():
#         m.sort()
#     visited = set()
#     queue = deque([])

#     # base case (root node)
#     queue.append(start)
#     # visited.add(start)
#     # for nodes in graph[start]:
#     #     queue.append(nodes)

#     print('visited = ', visited)
#     print('queue = ', queue)
#     print('-------------')

#     # iteration case (until queue is empty)
#     while queue:
#         curr_pos = queue.popleft()
#         visited.add(curr_pos)
#         for nodes in graph[curr_pos]:
#             if nodes not in visited:
#                 queue.append(nodes)
#         print('visited = ', visited)
#         print('queue = ', queue)
#         print('-------------')

#     return visited

# no_nodes, no_edges, start = map(int, sys.stdin.readline().strip().split(' '))
# graph = {}
# for k in range(1, no_nodes+1):
#     graph[k] = []
# for _ in range(no_edges):
#     ins_node, ins_edge = map(int, sys.stdin.readline().strip().split(' '))
#     graph[ins_node].append(ins_edge)
#     graph[ins_edge].append(ins_node)

# print(*bfs(graph, start))


# import sys
# from heapq import heappush, heappop, heapify

# sys.setrecursionlimit(10**6)

# class Node:
#     def __init__(self, data):
#         self.left = None
#         self.right = None
#         self.data = data

#     def insert(self, ins_data, post_order_list):
#         if ins_data < self.data:
#             if self.left is None:
#                 self.left = Node(ins_data)
#             else:
#                 self.left.insert(ins_data, post_order_list)
#         elif ins_data > self.data:
#             if self.right is None:
#                 self.right = Node(ins_data)
#             else:
#                 self.right.insert(ins_data, post_order_list)
        
#         # Append the current node's data to the post-order list if not inserted before
#         if self.data not in post_order_list:
#             post_order_list.append(self.data)

# # Read input
# in_arr = []
# while True:
#     try:
#         in_arr.append(int(sys.stdin.readline()))
#     except:
#         break

# # Build the tree and collect post-order traversal while inserting
# post_order_result = []
# inserted_values = set()
# root = Node(in_arr[0])
# for in_val in in_arr[1:]:
#     root.insert(in_val, post_order_result)

# # Print the post-order traversal
# for out_val in post_order_result:
#     print(out_val)



# import sys

# class Node:
# 	def __init__(self, data):
# 		self.left = None
# 		self.right = None
# 		self.data = data

# 	def insert(self, ins_data):
# 		# base case, no root node available
# 		if self.data:
# 			if ins_data < self.data:
# 				# 왼쪽 자식 없음
# 				if self.left is None:
# 					self.left = Node(ins_data)
# 				# 재귀느낌, 좌측 자식한테가서 데이터 삽입 하기
# 				else:
# 					self.left.insert(ins_data)
# 			elif ins_data > self.data:
# 				# 오늘쪽 자식 없음
# 				if self.right is None:
# 					self.right = Node(ins_data)
# 				# 재귀느낌, 우측 자식한테가서 데이터 삽입 하기
# 				else:
# 					self.right.insert(ins_data)

# 	# pre order traversal = 0 -> L -> R
# 	def pre_trav(self, root):
# 		result = []
# 		if root:
# 			result.append(root.data)
# 			result = result + self.pre_trav(root.left)
# 			result = result + self.pre_trav(root.right)
# 		return result

# 	# in order traversal = L -> 0 -> R
# 	def in_trav(self, root):
# 		result = []
# 		if root:
# 			result = self.in_trav(root.left)
# 			result.append(root.data)
# 			result = result + self.in_trav(root.right)
# 		return result

# 	# post order traversal = L -> R -> 0
# 	def post_trav(self, root):
# 		result = []
# 		if root:
# 			result = self.post_trav(root.left)
# 			result = result + self.post_trav(root.right)
# 			result.append(root.data)
# 		return result

# 	def print_tree(self):
# 		if self.left:
# 			self.left.print_tree()
# 		print(self.data)
# 		if self.right:
# 			self.right.print_tree()

# root = Node(27)
# root.insert(14)
# root.insert(35)
# root.insert(10)
# root.insert(19)
# root.insert(31)
# root.insert(42)

# # print('basic print = ', root.print_tree())
# print('pre print = ', root.pre_trav(root))
# print('in print = ', root.in_trav(root))
# print('post print = ', root.post_trav(root))

