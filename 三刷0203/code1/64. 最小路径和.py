class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])

        mp=[[math.inf for _ in range(n)]  for _ in range(m)]
        
        mp[0][0]=grid[0][0]

        for i in range(m):
            for j in range(n):
                if j-1>=0:
                    mp[i][j]=min(mp[i][j],grid[i][j]+mp[i][j-1])

                if i-1>=0:
                    mp[i][j]=min(mp[i][j],grid[i][j]+mp[i-1][j])

        return mp[m-1][n-1] 

