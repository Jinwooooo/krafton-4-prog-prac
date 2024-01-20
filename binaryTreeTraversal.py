import sys

sys.setrecursionlimit(10**9)

def post_trav(l, r):
	if l > r:
		return
	else:
		mid = r + 1
		for i in range(l + 1, r + 1):
			if binary_tree[i] > binary_tree[l]:
				mid = i
				break

		post_trav(l + 1, mid - 1)
		post_trav(mid, r)
		print(binary_tree[l])

binary_tree = []

while True:
    try:
        ins_node = int(sys.stdin.readline())
        binary_tree.append(ins_node)
    except:
        break

post_trav(0, len(binary_tree) - 1)

#######################
# Object is too heavy #
#######################

# class Node:
# 	def __init__(self, data):
# 		self.left = None
# 		self.right = None
# 		self.data = data

# 	def insert(self, ins_data, post_trav_arr):
# 		if ins_data < self.data:
# 			# if left is childless
# 			if self.left is None:
# 				self.left = Node(ins_data)
# 			# if left has child, visit to check for child
# 			else:
# 				self.left.insert(ins_data, post_trav_arr)
# 		elif ins_data > self.data:
# 			# if right is childless
# 			if self.right is None:
# 				self.right = Node(ins_data)
# 			# if right has child, visit to check for child
# 			else:
# 				self.right.insert(ins_data, post_trav_arr)

# 		print(self.data)
# 		post_trav_arr.append(self.data)

# in_arr = []
# post_trav_arr = []

# while True:
# 	try:
# 		in_arr.append(int(sys.stdin.readline()))
# 	except:
# 		break

# root = Node(in_arr[0])
# in_arr = in_arr[1:]
# for in_val in in_arr:
# 	root.insert(in_val, post_trav_arr)

# for out_val in post_trav_arr:
# 	print(out_val)

