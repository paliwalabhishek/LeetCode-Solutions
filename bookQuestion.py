#Check permutation
def checkPermuatation(a:str, b:str):
	n1=len(a)
	n2=len(b)
	if n1!=n2:
		return False
	a=sorted(a)
	b=sorted(b)
	if a!=b:
		return False
	return True
#URLify
def URLify(a:str, n:int):
	s=a.strip()
	s=s.replace(' ','%20')
	return s

#res=checkPermuatation('test','aest')
res=URLify('Mr John Smith      ', 13)
print(res)
