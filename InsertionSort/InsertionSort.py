#Implment insertion sort

def swap(arr,i,j):
	temp = arr[i]
	arr[i]=arr[j]
	arr[j] = temp

def insertionSort(arr):
	for i in range(len(arr)-1):
		for j in range(i+1,0,-1):
			if arr[j] < arr[j-1]:
				swap(arr,j,j-1)
			else: break
	
	return arr

if __name__ == "__main__":
		myarr = [-4,-7,1,73,-12,23,18]	

		sortedarr = insertionSort(myarr)
		print sortedarr
