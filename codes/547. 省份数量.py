from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited = [False]*n

        ans=0

        for i in range(n):
            if visited[i]==False:
                dfs(isConnected,i,visited)
                ans+=1

        return ans

def dfs(arr,i,visited):
    visited[i] = True
    for index,v in enumerate(arr[i]):
        if v==1 and not visited[index]:
            dfs(arr,index,visited)

isConnected =[[1,0,0],[0,1,0],[0,0,1]]
print(Solution().findCircleNum(isConnected))


