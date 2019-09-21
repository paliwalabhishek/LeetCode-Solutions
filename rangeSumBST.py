'''
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

#My Soltion

class BinarySearchTree:
	def __init__(self,root):
		self.val=root
		self.left=None
		self.right=None

	def in_order(self,root):
		res=[]
		if root:
			res=self.in_order(root.left)
			res.append(root.val)
			res=res+self.in_order(root.right)
		return res

def rangeSumBST(root,L,R):
    print(root)
    #TreeNode{val: 10, left: TreeNode{val: 5, left: TreeNode{val: 3, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}, right: TreeNode{val: 15, left: None, right: TreeNode{val: 18, left: None, right: None}}}
    rootNode = BinarySearchTree(root)
    sorted_bst=rootNode.in_order(root)
    a=list(range(sorted_bst.index(L),sorted_bst.index(R)+1))
    sum=0
    for i in a:
        sum=sum+sorted_bst[i]
    return sum
'''

class Solution(object):
    def rangeSumBST(self, root, L, R):
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)

        self.ans = 0
        dfs(root)
        return self.ans

#root = TreeNode{val: 10, left: TreeNode{val: 5, left: TreeNode{val: 3, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}, right: TreeNode{val: 15, left: None, right: TreeNode{val: 18, left: None, right: None}}}
#rangeSumBST([10,5,15,3,7,13,18,1,'null',6],6,10)
	