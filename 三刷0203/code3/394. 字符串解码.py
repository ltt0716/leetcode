class Solution:
    def decodeString(self, s: str) -> str:
        n=len(s)

        stack=[]
        res=""
        multi=0

        for c in s:
            
            if c=='[':
                stack.append([multi,res])
                multi,res=0,""
            elif '0'<=c<='9':
                multi=10*multi+int(c)
            elif c==']':
                multi,last_str=stack.pop()
                res=last_str+multi*res
                multi=0

            else:
                res+=c
        return res

s = "3[a]2[bc]"
print(Solution().decodeString(s))