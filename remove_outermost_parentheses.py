'''
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

My Solution:

	out=[]
	temp=[]
	flag=0
	for c in S:
		if c=='(':
			temp.append(c)
		if c==')':
			temp.append(c)
		if temp.count('(') == temp.count(')'):
			out.append(''.join(temp))
			temp=[]
	_out=[]
	for ele in out:
		ele=ele[1:-1]
		_out.append(ele)
	return ''.join(_out)
'''

def removeOuterParentheses(S:str) -> str:
        cnt, res = 0, ''
        for c in S:
            if c == ')': cnt -= 1  
            if cnt != 0: res += c 
            if c == '(': cnt+=1    
        return res


res=removeOuterParentheses('(()())(())')
print(res)


