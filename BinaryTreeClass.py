from queue import Queue

class BinaryTree:
	def __init__(self,value):
		self.value=value
		self.left_child=None
		self.right_child=None

	def insert_left(self,value):
		if self.left_child == None:
			self.left_child = BinaryTree(value)
		else:
			new_node = BinaryTree(value)
			new_node.left_child = self.left_child
			self.left_child = new_node

	def insert_right(self,value):
		if self.right_child == None:
			self.right_child = BinaryTree(value)
		else:
			new_node = BinaryTree(value)
			new_node.right_child = self.right_child
			self.right_child = new_node

	def pre_order(self):
		print(self.value)
		if self.left_child:
			self.left_child.pre_order()
		if self.right_child:
			self.right_child.pre_order()

	def in_order(self):
		if self.left_child:
			self.left_child.in_order()
		
		print(self.value)

		if self.right_child:
			self.right_child.in_order()

	def post_order(self):
		if self.left_child:
			self.left_child.post_order()

		if self.right_child:
			self.right_child.post_order()

		print(self.value)

	def bfs(self):
		q = Queue()
		q.put(self)
		while not q.empty():
			current_node = q.get()
			print(current_node.value)
			if current_node.left_child:
				q.put(current_node.left_child)
			if current_node.right_child:
				q.put(current_node.right_child)


# inseration of Binary Tree
'''
rootNode = BinaryTree(11)
rootNode.insert_left(8)
rootNode.insert_right(16)

node_8 = rootNode.left_child
node_8.insert_left(5)
node_8.insert_right(10)

node_5 = node_8.left_child
node_10 = node_8.right_child

node_16 = rootNode.right_child
node_16.insert_right(18)
node_16.insert_left(7)

node_18 = node_16.right_child
node_7 = node_16.left_child
'''

#rootNode.pre_order()
#rootNode.in_order()
#rootNode.bfs()
