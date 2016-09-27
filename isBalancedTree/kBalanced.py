#Implement an algorithm that will run through all the nodes of a tree
#and return a node which is not k-balanced but all of its decendents are
#A node is k-balanced if the difference in the number of nodes on left subtree and right subtree is no more than k

class Node:
	def __init__(self,key):
		self.key =key
		self.left = None
		self.right = None
		self.size = 0

def mysize(node):
	if node == None: return 0
	leftSize = mysize(node.left)
	rightSize = mysize(node.right)
	node.size = 1 + leftSize + rightSize
	return node.size

def checkKbalanced(root,k):
	[result,node] = isKbalanced(root,k)
	if not result:return node
	return None

def isKbalanced(root,k):
	if root == None: return True,None
	leftBalance,leftNode = isKbalanced(root.left,k)
	if not leftBalance: return False,leftNode
	rightBalance,rightNode = isKbalanced(root.right,k)
	if not rightBalance: return False,rightNode

 	leftCount = mysize(root.left)
	rightCount = mysize(root.right)
	if ((leftCount - rightCount <= k) and (leftCount - rightCount >= -k)):
		return True,root
	return False,root

if __name__ == "__main__":
	root = Node(5)
	root.left = Node(6)
	root.right = Node(2)

	root.left.right = Node(1)
	root.left.left = Node(7)

	root.right.left = Node(8)
	root.right.right = Node(7)

	root.right.left.left = Node(-8)
	root.right.left.right = Node(-9)
	
	result =  checkKbalanced(root,1)
	if result:
		print result.key
