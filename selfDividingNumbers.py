'''
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
'''
def selfDividingNumbers(left,right):
	t=list(range(left,right+1))
	r=[]
	flag=0
	for i in t:
		flag=0
		for x in str(i):
			if int(x)==0:
				flag=0
				break 
			if i%int(x)!=0:
				flag=0
				break
			else:
				flag=1
		if flag==1:
			r.append(i)
		#r.append(int(float(''.join([x for x in str(i) if int(x)!=0 and i%int(x)==0]))))
	return r

print(selfDividingNumbers(1,22))