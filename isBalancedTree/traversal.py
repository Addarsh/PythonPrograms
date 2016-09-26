#Implement an inorder traversal that checks
#if a tree is balanced or not
#A balanced tree is one where at each node, the difference in height
#of left and right subtrees is atmost one

class Node:
	def __init__(self,key):
		self.key = key
		self.left = None
		self.right = None
		self.size = 1

def mysize(root):
	if root == None: return 0
	leftsize = mysize(root.left)
	rightsize = mysize(root.right)
	return 1+leftsize+rightsize

def isBalancedTree(root):
	if root == None: return True
	if (isBalancedTree(root.left) and isBalancedTree(root.right)):
 		leftCount = mysize(root.left)
		rightCount = mysize(root.right)
		if ((leftCount - rightCount <= 1) and (leftCount - rightCount >= -1)):
			return True 
	return False

if __name__ == "__main__":
	root = Node(4)
	root.left = Node(3)
	root.right = Node(5)

	root.left.left = Node(7)
	root.left.right = Node(2)
	
	print isBalancedTree(root)	
