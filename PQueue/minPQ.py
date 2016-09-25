#Implementing a min Priority Queue

class minPQ:

	def __init__(self):
		self.myHeap = []
		self.numElems = 0

	def __swap(self,i,j):
		temp = self.myHeap[i]
		self.myHeap[i] = self.myHeap[j]
		self.myHeap[j] = temp
 
	def __swim(self,index):
		child = index
		parent = index/2
		
		while parent >= 1:
			if self.myHeap[parent-1] > self.myHeap[child-1]:
				self.__swap(parent-1,child-1)
				child = parent
				parent = parent/2
			else: break

	def add(self,elem):
		self.myHeap.append(elem)
		self.numElems += 1
		self.__swim(self.numElems)	
	
	def __sink(self,index):
		parent = index
		lchild = 2*index
		rchild = 2*index + 1
		while lchild <= self.numElems:
			minimum = parent
			if self.myHeap[parent-1] > self.myHeap[lchild-1]: minimum = lchild
			if rchild <= self.numElems and self.myHeap[minimum-1] > self.myHeap[rchild-1]: minimum = rchild
			if minimum == parent: break
			self.__swap(parent-1,minimum-1)
			parent = minimum
			lchild = 2*parent
			rchild = 2*parent +1 

	def remove(self):
		if self.numElems == 0: return
		self.__swap(0,self.numElems-1) #Swap first and last elements
		poppedElem = self.myHeap[self.numElems-1]
		self.myHeap = self.myHeap[0:self.numElems-1]
		self.numElems -= 1
		self.__sink(1)
		
		return poppedElem	

	def size(self):
		return self.numElems


if __name__ == "__main__":
	pq = minPQ()
	pq.add(30)
	pq.add(10)
	pq.add(-1)
	pq.add(4)
	pq.add(55)

	print pq.remove()
	print pq.remove()
	print pq.remove()
