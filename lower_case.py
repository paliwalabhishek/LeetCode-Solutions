#Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

def toLowerCase(str:str) ->str:
	out = []
	for c in str:
		if ord(c)>=65 and ord(c)<=122:
			if ord(c)<97:
				out.append(chr(ord(c)+32))
		else:
			out.append(c)
	return ''.join(out)


print(toLowerCase('LULLOBOY'))