def function(J:str,S:str)->int:
	return sum(S.count(i) for i in J)

print(function("aA","aAABB"))