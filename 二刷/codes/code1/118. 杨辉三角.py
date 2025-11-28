from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        dp=[[1]]

        for i in range(1,numRows):
            temp=[]
            for j in range(i+1):
                ans = 0
                if j<len(dp[-1]):
                  ans+=dp[-1][j]

                if j-1>=0:
                    ans+=dp[-1][j-1]
                temp.append(ans)
            dp.append(temp)

        return dp
