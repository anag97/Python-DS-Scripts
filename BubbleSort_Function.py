# Python function for Bubble Sort
def bubbleSortFunction(input_List):
	unsorted_list = input_List
	# For loop from last element decrementing to the first element
	for i in range(len(unsorted_list)-1,0,-1):
		# For loop from first element to element of (i-1) index
		for j in range(i):
			# Swaps two elements if the smaller index has the larger number 
			if unsorted_list[j] > unsorted_list[j+1]:
				temp = unsorted_list[j]
				unsorted_list[j] = unsorted_list[j+1]
				unsorted_list[j+1] = temp

	sorted_list = unsorted_list

	print("\nAfter the bubble sort, here is the sorted list: \n" + str(sorted_list))
	print("\n")

bubbleSortFunction([23,14,25,31,11])


		
	