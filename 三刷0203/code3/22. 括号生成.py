class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans=[]

        def backtrack(s,i,j):
            print(i,j)
            if len(s)==n*2 and i==j:
                ans.append(s)
                return
            if i<n:
                s+='('
                backtrack(s,i+1,j)
                s.pop()

            if i>j:
                s+=')'
                backtrack(s,i,j+1)
                s.pop()

        backtrack("",0,0)
        return ans