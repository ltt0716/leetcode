class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        n=len(s)
        path=[]

        def dfs(begin):

            if begin==n:
                ans.append(path[:])
            for i in range(begin,n):
                tp=s[begin:i+1]
                if tp==tp[::-1]:
                    path.append(tp)
                    dfs(i+1)
                    path.pop()
        dfs(0)
        return ans 