class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n=len(s)

        cnt={}

        for index,val in enumerate(s):
            cnt[val]=index
        
        begin=0
        end=0
        ans=[]
        for i in range(n):
            end=max(end,cnt[s[i]])
            if i>=end:
                ans.append(i-begin+1)
                begin=i+1
        return ans
