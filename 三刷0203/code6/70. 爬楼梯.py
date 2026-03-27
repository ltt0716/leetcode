import math

class Solution:
    def climbStairs(self, n: int) -> int:
        
        cnt={0:1,1:1}

        def dfs(i):
            l=0
            r=0
            if i-1>=0:
                if i-1 in cnt.keys():
                    l=cnt[i-1]
                else:
                    l=dfs(i-1)
                    cnt[i-1]=l

            if i-2>=0:
                if i-2 in cnt.keys():
                    r=cnt[i-2]
                else:
                    r=dfs(i-2)
                    cnt[i-2]=r

            return l+r

        return dfs(n)
