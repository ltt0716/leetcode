class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickselect(l,r,target):
            if l==r:
                return nums[l]
            
            privot=nums[r]

            i,j=l-1,r+1

            while i<j:
                i+=1
                while nums[i]<privot:
                    i+=1

                j-=1
                while nums[j]>privot:
                    j-=1

                if i<j:
                    nums[i],nums[j]=nums[j],nums[i]
                   
            if j==target:
                return nums[j]
            elif j<target:
               return quickselect(j+1,r,target)
            else:
               return  quickselect(l,j-1,target)
            
        target=len(nums)-k
        return quickselect(0,len(nums)-1,target)