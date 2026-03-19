class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)


        left=[-1]*n
        right=[n]*n

        stack=[]
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            
            left[i]=stack[-1] if stack else -1
            stack.append(i)

        stack=[]
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            
            right[i]=stack[-1] if stack else n
            stack.append(i)
        
        return max([heights[i]*(right[i]-left[i]-1) for i in range(n)])