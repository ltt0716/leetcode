class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)

        left=[height[0]]*n
        right=[height[-1]]*n

        for i in range(1,n):
            left[i]=max(left[i-1],height[i])
        
        for i in range(n-2,-1,-1):
            right[i]=max(right[i+1],height[i])
        
        return sum([min(right[i],left[i])-height[i] for i in range(n)])