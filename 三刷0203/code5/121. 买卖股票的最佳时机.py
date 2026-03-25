class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        min_p=math.inf

        for i  in prices:
            ans=max(i-min_p,ans)
            if i<min_p:
                min_p=i
        
        return ans