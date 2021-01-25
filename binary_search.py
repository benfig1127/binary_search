#!/bin/python3

def find_smallest_positive(xs):
	
	if not xs:
		return None
	
	bin_search_results=find_target_index(xs,0)
	
	#print('binary search results for 0:',bin_search_results)
	
	smallest_positive_num=None
	
	if bin_search_results[0]:
		if xs[bin_search_results[1]]==0:
			smallest_positive_num=bin_search_results[1]+1
		else:
			smallest_positive_num=bin_search_results[1]
	else:
		if xs[0]>0:
			return 0
	
	#print('smallest positive number:',smallest_positive_num)
	
	return smallest_positive_num
	

def find_target_index(a_list,target):
#if the target is not in the list, then it will return where 
#the target would have been if it was actually in the sorted list	
	
	start=0
	end=len(a_list)-1
	found=False

	while start<=end and not found:
		
		midpoint= (start+end)//2
		
		if a_list[midpoint]==target:
			
			found=True
		else:
			
			if target < a_list[midpoint]:
				
				end=midpoint-1
			else:
				
				start=midpoint+1
	if found:
		
		return [found,midpoint]
	
	if a_list[midpoint-1]<target and a_list[midpoint]>target:	
	#this statement returns true if the searched 
	#number is in between the adjacent numbers but is not there
	
		return [True,midpoint]
	
	else:
		
		return [found,False]


def binary_search(xs,target,sorted_low_to_high):

	start=0
	end=len(xs)-1
	found=False
	
	while start<=end and not found:
		
		midpoint_index=(start+end)//2
		midpoint_value=xs[midpoint_index]
		
		#print('\n')
		#print('index:','\n',midpoint_index)
		#print('value:','\n',midpoint_value)
		

		if midpoint_value==target:
			
			found=True
		else:
			
			if sorted_low_to_high:
				
				if target<midpoint_value:
					
					end=midpoint_index-1
				else:
					
					start=midpoint_index+1
			else:
				
				if target>midpoint_value:
					
					end=midpoint_index-1
				else:
					
					start=midpoint_index+1
	if found:
		
		return [found,midpoint_index]
	
	else:
		
		return [found, False]
	
	
def bin_search_high_index(xs,x):
	
	found, initial_x_index = binary_search(xs,x,False)
	
	if found:
		
		if initial_x_index==0:
			#if the found index was the beginning of the list, 
			#we cannot find a higher value, thus we immiedielty 
			#return the found key and the original index 
			
			#print("Already at begining of list:")
			return [found, initial_x_index]
		
		highest_x_index = initial_x_index
		highest_x_value = xs[highest_x_index]
		
		next_highest_x_index=highest_x_index-1
		next_highest_x_value=xs[next_highest_x_index]
		
		while highest_x_value==next_highest_x_value:
			#first check to see if we have reached the beggining of the list
			
			if highest_x_index==0:
				
				#print("Reached the begining of list while checking:")
				return [found, highest_x_index]
			
			#if we are not at the beggining of the list then incriment out indicies
			#and continue out loop 
			highest_x_index-=1
			next_highest_x_index-=1
			
			highest_x_value=xs[highest_x_index]
			next_highest_x_value=xs[next_highest_x_index]
		
		
		#'highest_x_index' now contains the highest index of 
		#all of the potentially duplicate x values
		#we return this index as our highest index
		
		#print("Did not reach the begining of the list, returnning index:")
		return [found,highest_x_index]
		
	else:
		#print("Initial binary search failed, exiting:")
		return [found,0]


def bin_search_low_index(xs,x):
	
	found, initial_x_index = binary_search(xs,x,False)
	
	boundary=len(xs)-1
	#print('boundary:',boundary)
	#print('initial_x_index',initial_x_index)
	
	if found:
		
		if initial_x_index==boundary:
			return [found, initial_x_index+1]
		
		highest_x_index = initial_x_index
		highest_x_value = xs[highest_x_index]
		
		next_highest_x_index=highest_x_index+1
		next_highest_x_value=xs[next_highest_x_index]
		
		while highest_x_value==next_highest_x_value:
			
			#print('highest_x_index',highest_x_index)
			if next_highest_x_index==boundary:
				
				return [found, next_highest_x_index+1]
			
			highest_x_index+=1
			next_highest_x_index+=1
			
			highest_x_value=xs[highest_x_index]
			next_highest_x_value=xs[next_highest_x_index]
		
		
		return [found,next_highest_x_index]
		
	else:
		
		return [found,0]

#print(bin_search_low_index([1, 1, 1, 1, 1, 1, 1, 1, 1, 1],1))

def count_repeats(xs, x):
	
	found_high,index_high=bin_search_high_index(xs,x)
	found_low,index_low=bin_search_low_index(xs,x)
	
	if found_high and found_low:
		return index_low-index_high
	else:
		return 0
	

def argmin(f, lo, hi, epsilon=1e-3):
	'''
	Assumes that f is an input function that takes a float as input and returns a float with a unique global minimum,
	and that lo and hi are both floats satisfying lo < hi.
	Returns a number that is within epsilon of the value that minimizes f(x) over the interval [lo,hi]

	HINT:
	The basic algorithm is:
		1) The base case is when hi-lo < epsilon
		2) For each recursive call:
			a) select two points m1 and m2 that are between lo and hi
			b) one of the 4 points (lo,m1,m2,hi) must be the smallest;
			depending on which one is the smallest, 
			you recursively call your function on the interval [lo,m2] or [m1,hi]

	>>> argmin(lambda x: (x-5)**2, -20, 20)
	5.000040370009773
	>>> argmin(lambda x: (x-5)**2, -20, 0)
	-0.00016935087808430278
	'''









'''
****************************************************************************************
TEST CASES:

#print(find_smallest_positive([]))
#print(find_smallest_positive([-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3]))
#print(find_smallest_positive([-3, -2, -1, 0, 1, 2, 3]))
#print(find_smallest_positive([1, 2, 3]))
#print(find_smallest_positive([-3, -2, -1]) is None)


#print(bin_search([-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3],3))
#print([-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3].index(3))
#print(bin_search([-3, -2, -1, 1, 2, 3],0))
#print(bin_search([-3, -2, -1, 1, 2, 3],-3))
#print([-3, -2, -1, 0, 1, 2, 3].index(-3))
#print(bin_search([1, 2, 3],2))
#print(bin_search([-3, -2, -1],2))
#print(bin_search([-3, -2, -1],0))


#print(bin_search_low_index([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3))
#print(bin_search_high_index([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3))
#print('\n')

#print(bin_search_low_index([3, 2, 1], 4))
#print(bin_search_high_index([3, 2, 1], 4))
#print('\n')

#print(bin_search_low_index([5, 4, 3, 3, 3, 3, 3, 2, 2, 2, 1], 1))
#print(bin_search_high_index([5, 4, 3, 3, 3, 3, 3, 2, 2, 2, 1], 1))
#print('\n')

#print(bin_search_low_index([5, 4, 3, 3, 3, 3, 3, 2, 2, 2, 1], 2))
#print(bin_search_high_index([5, 4, 3, 3, 3, 3, 3, 2, 2, 2, 1], 2))
#print('\n')
#print(count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3))
#print('\n')
#print(count_repeats([3, 2, 1], 4))
#print('\n')
#print(count_repeats([5, 4, 3, 3, 3, 3, 3, 2, 2, 2, 1], 1))
#print('\n')
#print(count_repeats([5, 4, 3, 3, 3, 3, 3, 2, 2, 2, 1], 4))
#print('\n')


****************************************************************************************
'''


