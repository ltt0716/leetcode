from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1]]

        for i in range(1,numRows):
            temp=[]
            for j in range(i+1):

                val=0
                if j<=i-1:
                    val+=ans[i-1][j]
                if   j-1>=0:
                    val+=ans[i-1][j-1]
                temp.append(val)
            ans.append(temp)

        return ans
