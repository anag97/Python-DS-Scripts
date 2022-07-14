# insertion sort function

def insertionSortFunction(input_list):
	unsortedList = input_list
	
	# traverse array from 2nd element to last
	for i in range(1,len(unsortedList),1):
		# let key be the element at the ith position of the array
		key = unsortedList[i]
		# let j be the element right before the key
		j = i-1
		# while j is within array & key is smaller than elem at position j
		while j >= 0 and key < unsortedList[j]:
			# Assign elem greater than key to the next position
			unsortedList[j+1] = unsortedList[j]
			# decrement from j to wherever insertion needs to occur (or zero if no insertion occurs)
			j -= 1
		# since j is decremented before exiting the loop we need to add 1 to get back to jth position
		unsortedList[j+1] = key
	
	sortedList = unsortedList
	print("Array sorted with insertion sort: " + str(sortedList))
		

insertionSortFunction([4,3,2,10,12,1,5,6])
		
		