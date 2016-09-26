#Implementation of selection sort

def swap(arr,i,j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

def selectionSort(arr):
	for i in range(len(arr)-1):
		minimum = arr[i]
		pos =  i
		for j in range(i+1,len(arr)):
			if arr[j] < minimum: 
				pos = j
				minimum = arr[j]
		if pos != i: swap(arr,pos,i)


if __name__ == "__main__":
	myarr = [44,-3,7,12,2,34,7,-4]
	selectionSort(myarr)
	print myarr	
