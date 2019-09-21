class BinarySearchTree:
	def __init__(self,value):
		self.value=value
		self.left_child = None
		self.right_child = None

	def insert_value(self,value):
		if value <= self.value and self.left_child:
			self.left_child.insert_value(value)
		elif value <= self.value:
			self.left_child = BinarySearchTree(value)
		elif value > self.value and self.right_child:
			self.right_child.insert_value(value)
		else:
			self.right_child = BinarySearchTree(value)

	def find_node(self,value):
		if value < self.value and self.left_child:
			return self.left_child.find_node(value)
		if value > self.value and self.right_child:
			return self.right_child.find_node(value)

		return value==self.value

	def find_minimum_value(self):
		if self.left_child:
			return self.left_child.find_minimum_value()
		else:
			return self.value

	def clear_node(self):
		self.value = None
		self.left_child = None
		self.right_child = None

	def pre_order(self):
		print(self.value)
		if self.left_child:
			self.left_child.pre_order()
		if self.right_child:
			self.right_child.pre_order()

	def del_node(self,value,parent):
		if value < self.value and self.left_child:
			return self.left_child.del_node(value,self)
		if value < self.value:
			return False
		if value > self.value and self.right_child:
			return self.right_child.del_node(value,self)
		if value > self.value:
			return False
		else : 
			if self.left_child is None and self.right_child is None and self==parent.left_child:
				parent.left_child = None
				self.clear_node()
			elif self.left_child is None and self.right_child is None and self==parent.right_child:
				parent.right_child = None
				self.clear_node()
			elif self.left_child and self.right_child is None and self==parent.left_child:
				parent.left_child = self.left_child
				self.clear_node()
			elif self.left_child and self.right_child is None and self==parent.right_child:
				parent.right_child = self.left_child
				self.clear_node()
			elif self.left_child is None and self.right_child and self==parent.left_child:
				parent.left_child = self.right_child
				self.clear_node()
			elif self.left_child is None and self.right_child and self==parent.right_child:
				parent.right_child = self.right_child
				self.clear_node()
			else :
				self.value = self.right_child.find_minimum_value()
				self.right_child.del_node(self.value, self)
				print(self.value)
			return True				
'''
arr=[50,76,21,4,32,100,64,52]
root_node = BinarySearchTree(50)
for i in range(1,len(arr)):
	root_node.insert_value(arr[i])
'''
#print(root_node.find_node(64))
#print(root_node.find_minimum_value())
#root_node.pre_order()
#root_node.del_node(50,None)
#root_node.pre_order()
