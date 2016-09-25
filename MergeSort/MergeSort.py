#Implementation of merge sort algorithm

def mergeSort(arr):
	start =0
	end = len(arr) - 1
	return mergedSort(arr,start,end)

def swap(arr,i,j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp	

def merge(arr,start,mid,end):
	i = start
	j = mid+1
	newarr = arr[:]
	k = start
	while i<=mid and j<= end:
		if newarr[i] <= newarr[j]:
			arr[start] = newarr[i]
			start += 1
			i+= 1
		else:
			arr[start] = newarr[j]
			start += 1
			j+= 1

	while i<=mid:
		arr[start] = newarr[i] 
		start += 1
		i+= 1

	while j<=mid:
		arr[start] = newarr[j] 
		start += 1
		j+= 1

	return arr

def mergedSort(arr,start,end):
	if start == end: return arr
	if (start + 1) == end:
		if arr[start] > arr[end]:
			swap(arr,start,end)
		return arr
	mid = (start+end)/2

	leftarr = mergedSort(arr,start,mid)
	rightarr = mergedSort(arr,mid+1,end)

	return merge(arr,start,mid,end)

if __name__ == "__main__":

	myarr= [35,-3,4,-10,7,74,12]

	mergedsort = mergeSort(myarr)

	print mergedsort		
