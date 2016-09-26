#Implement reversing a linked list

class Node:
	def __init__(self,key):
		self.key = key
		self.next = None

def move(head,newhead):
	movethis = head
	head = head.next
	movethis.next = None
	
	if newhead == None:
		newhead = movethis
		return head,newhead
	movethis.next = newhead
	newhead = movethis

	return head,newhead

def reverseLinkedList(head):
	newhead = None
	while head:
		head,newhead = move(head,newhead)
		#print head.key,newhead.key	
	return newhead

if __name__ == "__main__":
	head = Node(5)
	head.next = Node(3)
	head.next.next = Node(-4)
	head.next.next.next = Node(10)

	newhead = reverseLinkedList(head)
	if newhead != None:
		while newhead:
			print newhead.key," --> ",
			newhead = newhead.next
		print "NULL"
