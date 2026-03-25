class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        cnt={'}':'{',']':'[',')':'('}
        for c in s:
            if c in "{[(":
                stack.append(c)
            else:
                if not stack or stack[-1]!=cnt[c]:
                        return False
                stack.pop()
            
        if not stack:
            return True
        else:
            return False