from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        n=len(temperatures)
        ans=[0]*n

        n=len(temperatures)

        for i  in range(n):
            if not stack:
                stack.append(i)
                continue
            
            while stack:
                preindex=stack[-1]
                if temperatures[preindex]>=temperatures[i]:
                    break
                else:
                    pre=stack.pop()
                    ans[pre]=i-pre
            
            stack.append(i)
            
        return ans