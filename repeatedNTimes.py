'''
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.
'''
import collections

def repeatedNTimes(A):
	#print(collections.Counter(A))
	N=len(A)/2
	for a in A:
		if N==A.count(a):
			return a

print(repeatedNTimes([1,2,3,3]))