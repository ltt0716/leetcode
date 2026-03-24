class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1]]

        for i in range(1,numRows):
            tem=[]
            n=len(ans[-1])
            for j in range(i+1):
                num=0
                if j-1>=0:
                    num+=ans[-1][j-1]
                if j<n:
                    num+=ans[-1][j]
                tem.append(num)
            ans.append(tem)
        
        return ans