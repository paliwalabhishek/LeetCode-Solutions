def defangIPaddr(address:str)->str:
	x=address.replace(".","[.]")
	return x

print(defangIPaddr("1.1.1.1"))