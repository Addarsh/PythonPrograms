#Implementation of heapsort

def swap(arr,i,j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

def sink(arr,k,arrlen):
	parent = k
	lchild = 2*k 
	rchild = 2*k+1
	while lchild <= arrlen:
		maximum = parent
		if arr[lchild-1] > arr[parent-1]:maximum = lchild
		if rchild <= arrlen and arr[rchild-1] > arr[maximum-1]:maximum = rchild
		if parent != maximum:
			swap(arr,maximum-1,parent-1)
			parent = lchild
			lchild = 2*parent
			rchild = lchild + 1
		else: break

def buildHeap(arr):
	k = len(arr)/2
	for i in range(k,0,-1):
		sink(arr,i,len(arr))

def heapSort(arr):
	buildHeap(arr)
	arrlen = len(arr)
	for i in range(len(arr)):
		swap(arr,0,arrlen-1)
		arrlen -= 1
		sink(arr,1,arrlen)

if __name__ == "__main__":
	myarr = [-4,8,-10,-23,84,3,13]
	heapSort(myarr)
	print myarr 

