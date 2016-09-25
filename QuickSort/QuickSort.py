#Implement quicksort

def QuickSort(arr):
	start = 0
	end = len(arr)-1
	quickSort(arr,start,end)	

def quickSort(arr,start,end):
	if start >= end: return
	pivotpos = partition(arr,start,end)
	quickSort(arr,start,pivotpos-1)
	quickSort(arr,pivotpos+1,end)

def swap(arr,i,j):
	temp = arr[i]	
	arr[i] = arr[j]
	arr[j] = temp

def partition(arr,start,end):
	pivotpos = start
	counter = start
	pivotElem = end
	while counter < end:
		if arr[counter] <= arr[pivotElem]:
			swap(arr,counter,pivotpos)
			pivotpos += 1
		counter += 1
	swap(arr,pivotpos,end)
	return pivotpos		

if __name__ == "__main__":
	myarr = [5,-2,7,21,-12,34,2,44,8]
	QuickSort(myarr)
	print myarr
