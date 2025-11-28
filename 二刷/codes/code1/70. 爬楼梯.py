class Solution:
    def climbStairs(self, n: int) -> int:

        cnt={0:1,1:1}

        def dfs(i):
            if  i==0:
                return 1
            if i ==1:
                return 1

            l,r=0,0
            if i-1 in cnt:
                l=cnt[i-1]
            else:
                l=dfs(i-1)
                cnt[i-1]=l
            if i-2 in cnt:
                r=cnt[i-2]
            else:
                r=dfs(i-2)
                cnt[i-2]=r


            return l+r


        return dfs(n)