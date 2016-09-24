#Implementing a stack in python
class myStack:
	def __init__(self):
		self.mylist = []
		self.numElems = 0	

	def add(self,elem):
		self.mylist.append(elem)
		self.numElems += 1

	def pop(self):
		if self.isEmpty(): return
		poppedElem = self.mylist[self.numElems-1]
		del self.mylist[self.numElems-1]
		self.numElems -= 1
		return poppedElem

	def isEmpty(self):
		return self.numElems == 0

	def size(self):
		return numElems

	def peek(self):
		if not self.isEmpty():
			return self.mylist[self.numElems -1]


if __name__ == "__main__":
	stk	= myStack()
	
	stk.add(4)
	stk.add(2)
	stk.add(1)
	stk.add(5)

	print stk.peek()

	stk.pop()
	stk.pop()
	stk.pop()
	print stk.peek()
