'''
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]
0,1,2,3,4
'''
#MySolution == TimeExceeded
'''	
a=list(range(0,len(s)+1))
_s=[]
_s.extend(s)
t=[]
for i in range(len(_s)):
	if _s[i]=='I':
		x=min(a)
		a.remove(x)
		t.append(x)
	if _s[i]=='D':
		y=max(a)
		a.remove(y)
		t.append(y)
t.append(a[0])
return t
'''

def diStringMatch(S):
    lo, hi = 0, len(S)
    ans = []
    for x in S:
        if x == 'I':
            ans.append(lo)
            lo += 1
        else:
            ans.append(hi)
            hi -= 1

    return ans + [lo]


t="DDIDIDDDIDDDDDDIDIDDDDDDDIIIDIIDDIDDDIDIDDIIIIDIIIIIDDIDDDDDIDIDIDIDIIDIIDIDIIDIDIDDDDDDDDDIIDDDDIIIDDDIDIIIDIIDDDIIDIDIDDDIIDIDIIIDIIIDDIIIDDDIDIIDDIDDIIDDIIDDDIIDDIDIIDIIIDDDDDIIIIIIDIIIIIIIIIIDIIDDIDIIDDIDDIDDDDIIDIIIIDDDDIDDIIDIIDIDIDDIIIDIDDDDIDIDDDIDDIIDDDDIDIIDDDIIIIDIDDIIIIDIDDIIDDDDIDDIDIDIDDIIIDDDIIIIIDIDIDDDDIIDIDDIIDIIDIIDIDDIDDIDIIIDIDDDIDIDDDDIDDDIIIDIIDIIIDDIIIDIIDIIDDIIDIDDIDDIDIDDIIIIIIDIDDDIIDIDDDIIDIIDDDDIDDDDDDIDDDIDIDIIIIIDIIDDDIDIIDIIIDDDIIIDIIIIDIIDDIIIIIIIDDDDIIDIDIDIIDIIDIIIDIIIIDDIDDDIIDDIIIDDDIDDIDIIIIIIDIDIDDIIIIDDIDIDIDIIDIDIDIIDIIIIIIIIIIDDDDIIIIDDIDIIDDIIIDIDDIDDIDIIIDIDDIIDDDIDIIIIDDIDDDDIDDDIDIDIDIDIIIIDDIDDIDDDDIIIDIIDIIDDIIIDDIDIIDDDDDIDIIDDDIDIDDIIDDIDIDDIDDIDIDDDIDDIIIDIIIDIIIDDDIIDIIDDDDDDDDIIDDDIDDDDIDIIIIIDDDIDDDDIIIDIDIDDDIIIIDIIDIIDIDIIDIIIIDDDDDDIDDDIDIDIDIIDIIIIIDIIIIIIDIIIIDDIDIDDIIDIDIDDIIDIIIIIDIIDIDDDIDIDIDIIDDDIDIIIIIIIIDIDDIIIDIIIIIDIDIDDIIDDIIDIDIIDDIIIDDIDDDIDDIDIIDDDDDDIDDDIIIDIIIDDDDDIIIDIDDIIIDIIDDDDDDDIIIDIIDIIIIDDDIDIDIDIIIIIIDIDIDDDDDIIDIDIDIDIDIIIDDDIDIDDDDIIIDDDDIIDDDDDIIDIIIDDDDDIDDDDDDIIDDDIIIIIIIIDDDDIIIIIDIIDIDIIDIIIIDIIDIIDIIDDIDDDIDDDIIIDDIDIIDDDDDDDDIIIIIIIDIDIDDDIIIIDDDIDIDIDIIIIIIIIIDDIDIIIIIDDIDDIDDIIDDIIDIDIIIDIDIIIDIIDDIDDIIDIDIIIIDIIIDIDIDDDDIDIIIDDDIDDDIIDDDIDIDDIDIDIIDDIDIIDIDIDIDIIDDDIDIDIDIIIDIDDDIIDDIDIDIIIIIIIDDDIIDDDIDIIIIIIDDDIIIDDIDIDIDDDDDDIDIDIIDIIDIIIIIDIDDDIIDDIDIIDDIIDDIIIIDDIDIIIIIIDDIDIIDDDIDDDIIDIDIIDDDDIDDIIDDDIDIIIIDDIDIDDIIDDDIIIDIDDDIDDDIIDDDIDDDDIIIDDIDDIIIIIIDDDDIIDIDDIDDIDIIDIIDIIIIDIDIDIDIIIIIDIDDDDDIDIIDDDIIDIIDIIIIDDIDDDDDIDDDIIDDIDDDIDDDIIIDDDIDIDDIIIDIDIIDDIDIDDIDDDDDDIIDIIIDDDIIDIIDDDIDIDIDIIDIDDDDDIDIDDIIDIDIDIDIDDDIDIDIIDIIIDDDDIIIIIIIDIDIDDIDDDDDIDDDIIIDIIIDIIIDIIIDIDDDIIDDDDDDDIDDIDIIIIDIDIDDDIIIIDDDDIIIDDIIDDDIIDIDIIIIDIIIIIIIDIDDDIIDIIDDDIDDDDDIIIIIIDDDIIIDIDDIIIDIIIDIIIDDDIDIIDDDIDIIIIDDDIIDDDIIDDIDDDDDDDDDDDDDDIIDIDDIIIIIDIIIDDDDDIIIDDDDIIDDDDDDDIIIIIIDDDDDDDIDIDIDIIIDDDDDDDDDIIIIDDIDDIIIDDIIIIDDIDIIIDDDIDIIDDIIDDIIIIDDDIDIDDIDDDIDDDIIDDIIDDIDIIDIIIDIDDDIDDIIDDIIIDDIDDIDIDDDIIDIIIIIDIIIDDIIDDIDDIDDDIDDDIDIDIDDIDIIDIDIDDIDDIIIDDDDDDDDDDIDIDIDIIIDIIIIIIIDIDIIDIIDIIDIDDIIIIDDDIDDIDIDDIIDDDDDIIDIIIDIIDDIIDDIIIDDDIIDIDDDIIDIDIDIIDDDIDIDDDIIIIDIIIDDIDDDDDIIDIIIIDIDDIDDDIDDIIIDIIDIDIIDDDIIDDIDDDIIIDDDIIDDDIDIDDIIIDIIDDIDIIDDIDIDDIDIDDIIDDDDIDDDIDDIDDDIDIIIDDIDDIDIDDDIDDIDDIDDIIIIIDIIIIIIIDDDIIIDDDIDIDIIDDIIIDDIDDIDIDDDDDDDDDIIDDIDDDIIIIDDIDIDIIIIIIDIIIDDIDIDIIDDDIDDDDIIIDDDDDIIDIIIDIIIDDIDIIIIDIIDIIDIIDDDDDIDDIIDDDDDDDDIIDDIDDDDDDDIDIDDDDIIDDIDIIDDDIIIIIIDDDDDDDIIDIDDIDIIDDIIDIIDIIDDIIDDIIIDIDIIIIDDDDDIIIDDDDIIIIIDDDDDIDIDDIIDDDDDDIIIDDDIIDDIDDIDDDIDDDDDIDDDDIIIIIIIDIDIDDDIDDIIDIIDIIIDDIIIIIDIDDDDDDDIIIDIDDIIDIDDIDIDDIDDIIIIIDDIIDIIDIDDIIDDIDDDIDDDDDDDDIDDIIDIDDIDDDDIIIDIDIDIIIIDIDDIDDDDDIDIDDIDIIIIDIIDDIIDIDDIIDDDDDDIDDDIIDDIDIDIDIIDIDDDDIIDIIDIIDDIDIDDIDIDIDDIIDDDDDDIIIDDIDIDIIDDIIDIDDDDIDIDDIDIDIIDDDIDDDDDIIIDDIDDIIDIIIIDIIIIDIIDDDIDDDIDIDDDDDDDDDDDDIDIIIDDDDDIDIIDDDIDDDIDDDDDIIIDIIDDDIDIDDIIDIDIDDDDIIDDDDIDIDDDDDDIDDIIDDDIDIIIDDIIIDDDIDIDDDIDIDIIDDDDDIDIIDIDIIDDDIIDDIDDIDDIDDIDDDDDIDIIDDIIIIDDDIIIDDDIDIIIIDDIDDIDDIIDDIDDIIDIIIIDDIIDIIDDDIDIDIDIDDDDDIIDDDIIDDIIDDDIDDIIDIDDDDDDDIDDDIDIDIDDDIDIDDIIIIIDDDIDDDIDDDDDIDDIIIDIDDDIDDDIDIIDIIIDDDIIIIDIIDDDDIIDIIDIDIDDIDIIIDDDIIIDIIDIIIIIIIIIDDIDDDIDIIDIDDIIDDIIDIDIDIDDIDIDDIDDIDDIDDDIDDDDIDIDDIIIIIIIIIIIIDDIDDDDDIDDDIDDIIDIIIDIDIDDDIDDIIDIDDIIDIIDIIIIDIDDIDDIIDDDDDIIIDIIDIDDDIIIIDDIIIIDIIDIIDIDDIIIDIIIDIDIIDIDDDIDIIIDIIDIIIDIIIDIDIIIDDDIDDDIIDIDIDDIDIIDIDIDIDIIDIDDIDDDIDDIIDDIIIDDDDIDDIDIDDIIDDIIDDDDDDIIDDDIIDDIDIIIDIIDDDDIDIDDDIDDIDDIDIDDDDDIIIIDDDIIIDDIIIDIIDDDIDDIIDDIDDDIIDIIIIDDDIDIDDIIIIIDIDDDIDDIIDIIDDIDIIIDIDDDDDIIDIIIIIDDDIDIDDDIDDIIDIIDIIDDIDDIDIIIDIIIDDDDIDIIDDDIIDIDIIIIDDIIIIDDIIIDDDDDDDDIIIIIIIIDDDIIDIDIDDDDIDIDDDIIIDIDDDIDDIDDDIDDDDDDDIDDIIIIIDIIDDDIDDIDDIIIDIDIDDIIDIIIDDIDIDIIIIIIIIIIDIIIDDDIDIIIDIDIDDIDIIIIIIIDIDDIDDIIDIIIDIDDDIDDDDDDIIDDDIIDIDIDIIDIDDIDIDIIIIDDIIDDIDDDIIIDDIIIIDDIIDDIIIIIIDIIIIDIDIDDDDIDIIIIDIIIIDIDIDDDIIIDIDIDDIDIDIDIIIDDDIIIIDIDIDIDDDIDIIDDDDDIDIDIIIIDIIIDIDIIIIDDIDIIDIDDDIIDIDDIDDIIDDDIIIIIIDIDDDDIDDDIIDIDIDDDDDDDDDIIIIDIDDIDDDDIDDDDIIDDIIIIIDIIDIDIDIIIIIDDDIDIDDDIDIDIDIDIIIDDIIIIIDDDDIIIIDIIDIDDIIDIIIDDDDIIIDIDIIDIDIIIDIDDDDDIIIIDDIDIDIIIDDIIIDIDDDIIIIDIDIIIDIIIDIIIIIIIDIIIIIIIDIIIDIIDIIIIDIIIDDDDIDIIDDDIDDIDDDDIDDDDIIIIIDDIDIDIDIIIDDDIDDDIDIIIIIDIIDDDDIIDIDDDIIIDDDDIDDIDDIDDIDIDDDIDIIDDIDDDDDIDIIIDIDDIDIIDIIIIDDIIIIDDIDDIDIDDIDIIIDDDDIIDIIIIIIIDIIDIIDIIIDDDDIIIDIIIIDIIIDIDDDDDIDDIIDDDIDDDIIDDDIIDDIIDDDDDIDIDIDDIIIIDDDIDIDDIDIDIDDIIIDIIIDIIIDDDDDIIDIIDIDIDDDDDDDIDIDDIIDDIIDDIIDIDDIIIDDDIDIDDDIIDDIIDIIDDDDIDIIIIIDDIIIDIIDDDDIDIDIIDDIIDDIDIDDIDDIDIDDIIIDDIIDDIDDDDIIDIIDIIIIIDIDIDDDIDIDIIDDDIIDDDIDDDDIDDIDIIIDIDIIDDIIDDIIIIDIDDDIIIIDDIDIIDIDDDDDIIIDIIIDDDIDDIIDIDDDIIDDDDIIIDIDIIIIIIIDIDDIIIDIIDIDDIIIIDDIDDIIDDIDIDIDDDIDIDDDIIDIIDIIDIDDDDIDDIIIDDDIDDIIDDIIIDDDIDDDIDIDDDDIIIDDDDIDIDDDDDDDIIDIIDIIDDIDDIDDIDIIDIDIDIDDDDDDIIDDIDIDDIIIIIIIIIIDIIDDIDDDDDDIDIDIIDIIDIIIDDIIIDIDIIDIIDIIIDDDDDIDIIIDIIIDIIIDIDIIIDIDDDDDIDDDIDIDDIDIDIIIIIIDIDIIIDIIIIDIIIDDIIDIDDIIIDIDDIDDIIDIIIIIIIDIIDDIDDIDDIIDDDIIDIDDIIIIIDDDDDIDDIDIDIIIIDIDIIIDDIIDIIIIIIIDIIDIIDIIDDIIIDDIIIIDIDIIDDDDIIIDDDDIIDIIIDIDDDDDDDIIDDIDDIIIDDIDIDDDDIIDIDIIIDDIIDDIIIIDDDDIIIDDDIDDDDIIIIIIIIDIDDDDIDIDIDDIIDIDDDDDDDIIIDDIDDIDDDIDDIIDDIIIDDIIIIDDDIIDIIIIIDDDDDIDIDDDDIIIDIDDIIIDIIIIIIDDIIIDIDIDDIDIDIIIIDIDIIDIIIDDIIIDIDIDIDDIIDDDDDIDDIDIIDDDDDIIDIIIIDIIIIIDIIDDIDIDDIDIDIDDDIDDDIIIIIDIDIIIIDIIDDIIIDDDDIIDIDIIIDIIIIIIIIDIDDIIIIIIDIIIIIDIDIIIDIIIDDIIIIIIDDDIDIIIIIDIIIDDIIIIDIDIDDDIIDDIDIIDDIIIDIIIDIDDIDIIDIIIIIIDIDIDDDIDIIDDIIDIDIDDDIDIDDDIIDIIIIDDDIDIDDIIIDDIDIIIDIIIIIIDDIDDDDIIIIDDIIIIIDDIDDDIDIIIIDIDIDIIDDDIIIDDDDDIDIIDDDIDDIIIDDDIIIDIDDIIIIIIDDIIIDDIDIIIIDDDIDDIDDDIDDIIDDIDDDDDIDIIDDIIIDIDDIDDDDDIIIDDDIIDDIDDDDDDDIIIDIDDDIIDIDIIDDIDIDDIIIDDIDDDDIIDDIDIIIDIDDIDIDDIDIIIDIIDDIIIIDDIIDIDDIIDDDIDDIIIDDIDIDDIIIIIIDIDIDDDIDDDDIDDDDDDIDIIDIIIIIIIDIDDDDIIIDIDDDDDIIDDDIIIIDDDIDIIIIIDDDDIIDIIDIIIDDDIIIDDDDIDDDDIDIDIDDIDDDDIDDDIIIDDIIIDIDIIDIDIDDDIDIDDDIDIIDIDDIDDIDDDDIIDIIIDDDIDIIDIIIIDIIDIDDDDIDDDIDIIIIDIIDIIDDDDIDDDDDIDIDIDIDDIIIDIDIDDIIIIDIDDIDIIDDDDDDIIDDDDDDDIDIDDIIIIIDIDDDIDIIDIDDIIDIIDIDDIIDDDDIIDDDIIDDIIIDIDDIDIDIIIDDDDIDIIDDDDDIIIDDIDDIIDIDDDDDIDDDDDDIDDDIIDIDDDDIIDIIIIDDIIIIDIDIIIIIIIDDDDDIDIIIDDDIIDIDDDIDDDDDDDDIDDIDDIDIDDIIDDIDDIDIIDDIDIDDDDIDDDDIDDDIDIIDDIDIIDIDDIDIIIDDIDIDDDIDIDDDIIDIDDIIIDDDIDDDIIDIIDIDDDIDIIIIIDDDIIIIDIIDDDDDIDIIDDDIDIIIIDIIIDIDIIIIIIIIDDDDIIDIIDIIDDIIDIDDDDIIIIDDIIIIDIDIDIDIIIIDDDDDIIIDIDIDIIIIIDIIDDDIDDDIDIDIDDIDIIIDDIDIIIIIDDDIIDIDIDIIIDDIIDDIDDIDDIIIDDIIIDIIIIDDDDIIDDDDDIIIIIDDIIIIDIIIDIDDDIIIIIDIIDDDDIDIDDDDIIDDIIIIIDIDIIDIIDDDIDIIIIDIIDDDDDDIDDIIDIIDDDIIIIDDDDDIDDIDDDIDIIIDDDDDIIIIDIDDDDIIDIIIIDIIIDDIIIIDIDDDDDIIIIDDIDDIIDDIDIDIIDIIDDDIIDIIDDDDDIIDIIIIDDIDIDDIIIDDIIIIDIIIIIDDDIDIDIIDDIIDDDDDIIIIIDIIIIDDIIDIIIDIIIDIIDIDIDIDDDIIDDDDDDIDDIDDIDDDIIIDIDIIIDIIDDDIDDIIDDIDIIIDIIIIDIDDDDIDIDIDIDIDIIIIIDDIIIIDDDIIDDIDDIIIIDDIDIDIDIIIDDDDIDDIIIIDDDIIDIIDDIIDIDIDDDDIIDIIIDIIDDDIDIIIDIDIIDDDDDDDDIDDIIDDIIDIDIDDDDDIIIDDIDIIIIIDIDDDIIDIDIIIIDIIDDIDIIIIDIIDIIIDIDDDDDIDDDIIDDDIIIDDIDIIDIDDDDIIDDDIIIDDIIIIIIIIDIDIIDDDIIDIDIDIIIDIDIDIDDDIDDDDIIIIIIDDIIIIIDIDDDDIDDIIDIDIDDDIDDDIDDDDIDDDDIIDIDDDDDDDDDDIIIIDIIDDIIDDIDIIIIIDIIIIDDIIDIDIDDIIDDIIIDIDDIIDIIIDIIDIDDIDIDDDDDDDDDIDIDDIDIIDDDDDDIIDDIDIIDIDIDDIIIDIDDDDDDIIDDIDDIDDIDDDDIDIDIIDDIIIIDDDDDDDIDDIIDDDIDIIIIIIDIIIIDDIDDDDIDDDIIIDDDDDDIDDDIDIDIDIIIDDIIIDIIDIDIIIIIDDDDIIIDDDIDDIDDIIDIIDDIDIIDIIIDIIIDDIDIIIIDDIDIIDIIDDDIDIIDDDIDDDIDIIIDIDIIIDDDDDDDIDIIIIIDDIIIIDIIIDDDIIIDIDIIDIIDDDDIDIIIDDDDIIDDDDIIIDIIDIDIIDIDIIDIIDDIDDIDDIDDDIIDDDDIIIIIDIDIIIDDIIIDDIDIIIDDIIIDDIDDIIDIIDDIIDDDIIDDDIIIIDDDDIIDIIDDIDDDDDDIIIIDDDDIIIIDIDIIDDIIIIDIIDIDIDDDIIDDIDIDDDDDDDIDIDIDIDIIIIIIDDDDIDIIIDIDIIDDDDIDIIIIDIIDIDDDIIDIDDIDIIDDIIIIDDDDIIDIDDIIDIIIDDIDDIIIIDIIIDDDIDDDDIDIIDDDIIIDDDIDDDDIIIDIIIIDIDIDDIDIDIIIIDIDDDIIIIDIDDDIIIIDDDDIDDDIIDIDIIDIIIDIIIIDDDIDDIDDIDIDIDIIIIIDIIDDIIDIDIDDIDIDDDDIIIIIDDIIDIDDDIIDIDDIIIIIIDIIIDDDDDDDDDDDIIDDDDDIIIIDIDDIDIDDDDDIDIDDDIDDDIIIIIIIIDIIDIDIDIIDIDIDIDDIDDIIDIDDDIIDDIDDIIIDIDDIDDDDDIIIIDDIDIIIDIIIIDIDDDDDIIDDDDIDDIIDDDDDIDIIDDIDDIDDIIIIIIIDIIIIDIDDIDDDIIIIDIDIIDIIDIIDDDDIIIDDDIDDIIDIDDIIDDIDDIIDDIDIDDIDDIIIIDIDDIDDDIDIIDIIDDIDIIIIDIIDDDIIIDDDIDIDDDDIDDIDIDIDIDDIIIIDIIDIIIIDIDIIIIIDDDDIIDDDDDDIIDDDDIDIDIIDDIDDDDDDIIIDIIDDDDIDDIIDIDIDIIIIDIIDIIDIIDDIDDDIIDIIIIDDDIIDIIDDIIDIDIDDIDIIIIDDDIDDIIDIDDDDDDIDDDDIDIIDDIIDDDDIDDIDIIDIIIIDIIIDDDIDIDDIIDIDIDIDIIIIIIIIIIDIIIDIIDDDIDIDDDIIIDIIIIIIIDIIIIIIIDDIIDIIDDIIDIDIDIIIIIIIDIDIDDIDDDDDIDIIIDIIDIDDIIIIIIIDIIDDDDIIIIDIIIIIDDDIIIDDDDIDDIIIDDDIIIIDIIDIDDDDDDDIIIIDIDDIDDIIIIIDDIDDDDIDDDDDDIIDDDDDIDIIDDDIIIIIIIDIIIIDDDDIDDIIIDIIDIDDDIIDDIIDIDIIIDIDDIDDDIDIIIDDDDDDIIIDDIIIDIIDIIDDIIDIIIDDDIDDDIIDDDDIDDIDIIIDDIIDIIIIIIIIIIDIIDIIDIDIIDDIIIDIDIDDDIIIDDIDIIDIDIDIDDDIDIDIIDIDDDDDIDDDDIIIDDDDDDIIIIIIIDDDIIIDDDDDDDDDDDDIDIDIDIIIIDIDDIIDDIDDIDIDDIDIIDIDIIIDDDDDIIIIDIDIIDDIIIDDDIIDDDIIDDIIIIDIDDIDDDDIDIIDIIDIDDIIDDDIDIDIDDDDDIDDDIDDIIIDIIDIDDDIDDDDDDDDDDIDIDDIDDDIDDIDDDDDIIDIDIDIIIIDIIDIDIIDDIDDDDIDIIIDDIDDDIDIIIIIDDDIDIDIDDIIIIIIIDDDIIDIDDDIDIDDIDIDIIIIIIIIDIDDDIIDIIIIDIDDDDIIIDIIDDIIIDDDIIIIIIIIIDDIDIIIDDIIIIIIIDIDIIIDIDIIDIDIIDDIIIDDIDIDIDDDDDDDIIIDDDDIIIIIIIDDIDDIIIDDDDIIIIDDDIDDDDDIDDIIDIDIIDIIDDDDDIDDIIDIDIDIDIDDDDDDIDIDDIIIDDDIIDIIDIIIDIDDDDDIDDIDIDDDIIDIDIIIDDDDIDDIDIDDDIDIIIIIDIDIIDIDIDDDIIDIIIDIDIDIIIDIDIDIDDDDIDDIIDIIDIDDIIIDIIDIDIIIIIDDDDIIDDDIIIIDIDIDIIIDDDIDIDDDDDIIDIIDDIIDIDIDDIIDIIDIIDIIIDDDIDDIDDIDDIIDIIIIDIDIIIIIDIDDIIDDIIDDIIDDIDIDIIDIIDDIIIIDIDIIDIDIDIDDDDIIDIIIDDDDIDIDIIIDIDDIIDIDIIDDDIDIIDIIDDIIDDIIDIDIIIDIDDIDDIDDDIIIIDDDDDIIDDIDDIIIDIIIIIIDIDIIIDIDIIDDDDIDDDIDIIIIDIIDIIDDIIIIDIDDIIDIIDDDDIDDIIDIIIDDDIIIIIDDDIIDDIDDDIDDDDDDIIDIDDIDIIIIDDDDDIDDIDIIDIDDIDIIDIDIDIDIDIIDDDIDIIIDDDIDIIIDIIDDIIIIIDIIDDDIDIDIIDIIIIIDDDDDDIDDDDDIDIIDIDDIDDDDDIDIDIDDIDIIDIIDIIIIIDIIDIIDDIIDIDIIIIIIDIIDIIIIDDDDDDIDDDDDIDDIDDDDIDIIDDIIDIIDIDIIDDIDIDDDIDIDIIIIIIIDIDDIDDIIIDIDIIIDIIIIDDIIIIIDIIDIIIDDIDIIIIDIDIIIDDIIIIDDDIIDDDIIIDIIIIDIDIIIIDIDDIDIDIDIIDIDDDIIDIIIDDDIDDDIIIDIIIIIDDIIIDIDIIDIIDDDIDIIDDII"
print(diStringMatch('IDID'))