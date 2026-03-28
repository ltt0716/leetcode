class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cnt={(0,0):1}

        def dfs(x,y):
            a,b=0,0
            
            if x-1>=0:
                if (x-1,y) in cnt.keys():
                    a=cnt[(x-1,y)]
                else:
                    a=dfs(x-1,y)
            
            if y-1>=0:
                if (x,y-1) in cnt.keys():
                    b=cnt[(x,y-1)]
                else:
                    b=dfs(x,y-1)

            return a+b
        
        return dfs(m-1,n-1)

        

