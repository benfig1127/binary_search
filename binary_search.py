#!/bin/python3

def find_smallest_positive(xs):
	'''
	Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
	Find the index of the smallest positive number.
	If no such index exists, return `None`.

	HINT: 
	This is essentially the binary search algorithm from class,
	but you're always searching for 0.

	>>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
	4
	>>> find_smallest_positive([1, 2, 3])
	0
	>>> find_smallest_positive([-3, -2, -1]) is None
	True
	'''
	
	if not xs:
		return None
	
	bin_search_results=bin_search(xs,0)
	#print('binary search results for 0:',bin_search_results)
	
	smallest_positive_num=None
	
	if bin_search_results[0]:
		smallest_positive_num=bin_search_results[1]+1
	else:
		if xs[0]>0:
			return 0
	
	#print('smallest positive number:',smallest_positive_num)
	
	return smallest_positive_num
	
def bin_search(a_list,target):
	
	start=0
	end=len(a_list)-1
	index=0
	found=False

	
	while start<=end and not found:
		
		midpoint= (start+end)//2
		
		#print('midpoint:',midpoint)
		
		if a_list[midpoint]==target:
			
			found=True
		else:
			if target < a_list[midpoint]:
				end=midpoint-1
			else:
				start=midpoint+1
				index+=start
	if found:
		return [found,midpoint]
	else:
		return [found,False]
	
	
#print(find_smallest_positive([]))
#print(find_smallest_positive([-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3]))
#print(find_smallest_positive([-3, -2, -1, 0, 1, 2, 3]))
#print(find_smallest_positive([1, 2, 3]))
#print(find_smallest_positive([-3, -2, -1]) is None)

#print(bin_search([-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3],3))

#print([-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3].index(3))
#print(bin_search([-3, -2, -1, 0, 1, 2, 3],-3))
#print([-3, -2, -1, 0, 1, 2, 3].index(-3))
#print(bin_search([1, 2, 3],2))
#print(bin_search([-3, -2, -1],2))


def count_repeats(xs, x):
	'''
	Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
	and that x is a number.
	Calculate the number of times that x occurs in xs.

	HINT: 
	Use the following three step procedure:
		1) use binary search to find the lowest index with a value >= x
		2) use binary search to find the lowest index with a value < x
		3) return the difference between step 1 and 2

	I highly recommend creating stand-alone functions for steps 1 and 2
	that you can test independently.

	>>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
	7
	>>> count_repeats([3, 2, 1], 4)
	0
	'''


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

