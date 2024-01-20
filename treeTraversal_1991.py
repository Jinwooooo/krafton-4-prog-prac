import sys

class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

	def __str__(self):
		return str(self.data)

	def insert(self, root, parent_data, left_data, right_data):
		curr_node = self.find_node(root, parent_data)

		if left_data == '.' and right_data == '.':
			return
		elif left_data == '.' :
			curr_node.right = Node(right_data)
		elif right_data == '.':
			curr_node.left = Node(left_data)
		else:
			curr_node.left = Node(left_data)
			curr_node.right = Node(right_data)
	
	def find_node(self, root, target):
		if root is None:
			return None

		if root.data == target:
			return root

		left_node = self.find_node(root.left, target)
		if left_node:
			return left_node

		right_node = self.find_node(root.right, target)
		return right_node

	# pre order traversal = 0 -> L -> R
	def pre_trav(self, root):
		result = []
		if root:
			result.append(root.data)
			result = result + self.pre_trav(root.left)
			result = result + self.pre_trav(root.right)
		return result

	# in order traversal = L -> 0 -> R
	def in_trav(self, root):
		result = []
		if root:
			result = self.in_trav(root.left)
			result.append(root.data)
			result = result + self.in_trav(root.right)
		return result

	# post order traversal = L -> R -> 0
	def post_trav(self, root):
		result = []
		if root:
			result = self.post_trav(root.left)
			result = result + self.post_trav(root.right)
			result.append(root.data)
		return result

root = Node('A')

for _ in range(int(sys.stdin.readline())):
	in_val = sys.stdin.readline().strip().split(' ')
	root.insert(root, in_val[0], in_val[1], in_val[2])

print(''.join(root.pre_trav(root)))
print(''.join(root.in_trav(root)))
print(''.join(root.post_trav(root)))


# root.insert(root, 'A', 'B', 'C')
# root.insert(root, 'B', 'D', '.')
# root.insert(root, 'C', 'E', 'F')
# root.insert(root, 'E', '.', '.')
# root.insert(root, 'F', '.', 'G')
# root.insert(root, 'D', '.', '.')
# root.insert(root, 'G', '.', '.')