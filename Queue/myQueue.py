#Implementing queue class in python
class myQueue:

	def __init__(self):
		self.mylist = []
		self.numElems = 0

	def enqueue(self,elem):
		self.mylist.append(elem)	
		self.numElems += 1

	def size(self):
		return self.numElems

	def isEmpty(self):
		return self.numElems == 0

	def dequeue(self):
		if self.numElems == 0: return
		poppedElem = self.mylist[0]
		self.mylist = self.mylist[1:]
		self.numElems -= 1
		return poppedElem


if __name__ == "__main__":
	myQ = myQueue()
	myQ.enqueue(3)
	myQ.enqueue(-1)
	
	print myQ.dequeue()
	myQ.enqueue(9)
	myQ.enqueue(5)

	print myQ.dequeue()
	print myQ.size()
	
	
