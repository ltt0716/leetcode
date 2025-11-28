from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        key,count=0,0

        for x in nums:
            if count==0:
                key=x
            if key==x:
                count+=1
            else:
                count-=1
        return key
