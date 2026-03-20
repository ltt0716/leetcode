class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
<<<<<<< HEAD
        left=[0]*n
        right=[0]*n

        stack=[]
        for i in range(n):
            while stack and stack[-1]>=heights[i]:
                stack.pop()

=======


        left=[-1]*n
        right=[n]*n

        stack=[]
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            
>>>>>>> f7c9f0c6bcc15d59002e4547f6b9335e3ec53490
            left[i]=stack[-1] if stack else -1
            stack.append(i)

        stack=[]
        for i in range(n-1,-1,-1):
<<<<<<< HEAD
            while stack and stack[-1]>=heights[i]:
                stack.pop()

            right[i]=stack[-1] if stack else n
            stack.append(i)

        ans=0
        for i in range(n):
            ans=max(ans,heights[i]*(right[i]-left[i]-1))

        return ans
=======
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            
            right[i]=stack[-1] if stack else n
            stack.append(i)
        
        return max([heights[i]*(right[i]-left[i]-1) for i in range(n)])
>>>>>>> f7c9f0c6bcc15d59002e4547f6b9335e3ec53490
