#Implement Binary Search solution

def Bsearch(arr,elem):
	start = 0
	end = len(arr)-1
	while start <= end:
		mid = (start + end)/2	
		if(arr[mid] == elem): return True
		if(arr[mid] > elem): end = mid -1
		if(arr[mid] < elem): start = mid+1
	return False

if __name__ == "__main__":
	myarr = [-4,1,5,6,9,23]
	elem = 2
	print Bsearch(myarr,elem)

