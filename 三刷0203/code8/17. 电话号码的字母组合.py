class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        cnt={
            2:('a','b','c'),
            3:('d','e','f'),
            4:('g','h','i'),
            5:('j','k','l'),
            6:('m','n','o'),
            7:('p','q','r','s'),
            8:('t','u','v'),
            9:('w','x','y','z')
        }
        ans=[]
        path=""
        n=len(digits)
        def dfs(i):
            nonlocal path
            if i==n:
                ans.append(path[:])
                return
            
            for c in cnt[int(digits[i])]:
                path+=c
                dfs(i+1)
                path=path[:-1]
        
        dfs(0)
        return ans