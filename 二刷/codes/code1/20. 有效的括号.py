class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        cnt={')':'(','}':'{',']':'['}
        left="({["

        for ch in s:
            if ch in left:
                stack.append(ch)
            else:
                if len(stack)==0 or stack[-1]!=cnt[ch]:
                    return False
                stack.pop()

        if len(stack)!=0:
            return False

        return True

