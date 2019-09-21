def maxNumberOfBalloons( text: str) -> int:
    ans=len(text)
    for l in 'ban':
        ans=min(ans,text.count(l))
    for l in 'lo':
        ans=min(ans,text.count(l)//2)
    return ans


def reverseParentheses(s: str) -> str:
    flip = False
    stack = [[]]
    for c in s:
        if c == '(':
            stack.append([])
        elif c == ')':
            stuff = stack.pop()
            
            for c in reversed(stuff):
                stack[-1].append(c)
        else:
            stack[-1].append(c)
    return "".join(stack.pop())

def kConcatenationMaxSum(arr, k: int) -> int:
    cur=arr[0]
    prefix_max=cur
    for num in arr[1:]:
        cur+=num
        prefix_max=max(prefix_max,cur)
    prefix_max=max(0,prefix_max)
    total_sum=cur
    cur=arr[-1]
    suffix_max=max(cur,0)
    for num in reversed(arr[:-1]):
        cur+=num
        suffix_max=max(suffix_max,cur)
    def helper(arr):
        ans=cur=arr[0]
        print(arr)
        for num in arr[1:]:
        	print('num--',num)
        	print('cur--',cur)
        	if cur>0:
        		cur=num+cur
        	else:
        		cur=num
        		ans=max(ans,cur)
        return ans
    ans=0
    if k==1:
        ans=max(ans,helper(arr))
    elif k==2:
        ans=max(ans,helper(arr+arr))
    else:
        ans=max(ans,helper(arr))
        ans=max(ans,helper(arr+arr))
        ans=max(ans,prefix_max+suffix_max+(k-2)*max(0,total_sum))
    return ans%(10**9+7)

#print(maxNumberOfBalloons("krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"))
#print(max('loonbalxballpoon'))

#print(reverseParentheses("a(bcdefghijkl(mno)p)q"))

print(kConcatenationMaxSum([1,-2,3],2))





