def uniqueOccurrences(arr):
	dic = {}
	l = []
	for a in arr:
		c = arr.count(a)
		if a not in dic.keys():
			dic[a] = c
			if l.count(c)==0:
				l.append(c)
			else:
				return False
	return True

def equalSubstring(s,t,maxCost):
	if (maxCost==0):
		return 1
	else:
		l = [abs(ord(s[x])-ord(t[x])) for x in range(len(s))]
		cost=r=0
		for i in range(len(s)):
			cost=cost+l[i]
			if cost>maxCost:
				cost=cost-l[i-r]
			else:
				r=r+1
		return r
		
				
def removeDuplicates(s,k):
	stack=[]
	for c in s:
		if not stack:
			stack.append([c,1])
		elif stack[-1][0] != c:
			stack.append([c,1])
		elif stack[-1][1]+1 < k:
			stack[-1][1] += 1
		else:
			stack.pop()
	print(stack)
	t=[]
	for c,ct in stack:
		t.extend([c]*ct)
	return "".join(t)


removeDuplicates("deeedbbcccbdaa",3)

#print(uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))
#print(equalSubstring("krrgw","zjxss",19))
#print(equalSubstring("abcd","bcdf",3))

