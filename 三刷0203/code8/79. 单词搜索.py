class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])

        visited=[]

        dirs=[(0,1),(1,0),(0,-1),(-1,0)]

        leg=len(word)

        def dfs(x,y,i):
            visited.append((x,y))

            if i==leg-1:
                return True
                
            for dx,dy in dirs:
                if 0<=dx+x<m and 0<=dy+y<n and (dx+x,dy+y) not in visited and board[dx+x][dy+y]==word[i+1] :
                    flag=dfs(dx+x,dy+y,i+1)
                    if flag:
                        return True
            visited.pop()
            
            return False
            

        
        for i in range(m):
            for j in range(n):
                visited=[]
                if board[i][j]==word[0] and dfs(i,j,0):
                    return True
        
        return False

