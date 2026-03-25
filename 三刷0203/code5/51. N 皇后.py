class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        l_b=[]
        r_b=[]
        col=[]


        ans=[]
        path=[]

        def backtracking(i):
            if i==n:
                ans.append(path[:])
                return
            
            for j in range(n):
                if  j not in col and i-j not in l_b and i+j not in r_b:
                    col.append(j)
                    l_b.append(i-j)
                    r_b.append(i+j)
                    path.append((i,j))
                    backtracking(i+1)
                    col.pop()
                    l_b.pop()
                    r_b.pop()
                    path.pop()
            
        backtracking(0)

        res=[]
        for li in ans:
                
            matrix=[['.' for _ in range(n)] for _ in range(n)]
            for x,y in li:
                matrix[x][y]='Q'
            tp=["".join(matrix[i]) for i in range(n) ]
            res.append(tp)

        return res
