#Implement Binary Search solution

def Bsearch(arr,elem):
	start = 0
	end = len(arr)-1
	return bsearch(arr,elem,start,end)


def bsearch(arr,elem,start,end):
	if(start > end): return False
	mid = (start + end)/2	
	if(arr[mid] == elem): return True
	if(arr[mid] > elem): return bsearch(arr,elem,start,mid-1)
	if(arr[mid] < elem): return bsearch(arr,elem,mid+1,end)

if __name__ == "__main__":
	myarr = [-4,1,5,6,9,23]
	elem = 4
	print Bsearch(myarr,elem)

