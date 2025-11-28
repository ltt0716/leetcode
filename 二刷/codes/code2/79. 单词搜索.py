from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dir={(0,1),(1,0),(0,-1),(-1,0)}

        k=len(word)

        m,n=len(board),len(board[0])

        def dfs(i,j,index):
            if i<0 or i>=m or j>=n or j<0:
                return False
            c=board[i][j]

            if c != word[index]:
                return False

            if index==k-1:
                return True


            board[i][j]=''
            for dx,dy in dir:
                if  dfs(dx+i,dy+j,index+1):
                    return True
            board[i][j]=c



        for i in range(m):
            for  j in range(n):
                if dfs(i,j,0):
                    return True

        return False


