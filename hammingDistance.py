def hammingDistance(x,y):
	f=[]
	f.extend(bin(x).replace('0b',''))
	s=[]
	s.extend(bin(y).replace('0b',''))
	if len(f)!=len(s):
		if len(s)>len(f):
			for i in range(len(s)-len(f)):
				f.insert(0,'0')
		else :
			for i in range(len(f)-len(s)):
				s.insert(0,'0')	
	res=[e1 for e1,e2 in zip(f,s) if e1!=e2]
	return len(res)
	

print(hammingDistance(1,4))
#Xor Implementation
print(bin(1^4)[2:].count("1"))

