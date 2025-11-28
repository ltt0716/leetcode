from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        def reverse(i,j):
            while i<j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1

        k=k%n
        reverse(0,n-1)
        reverse(0,k)
        reverse(k,n-1)