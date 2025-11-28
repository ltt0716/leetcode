from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        key,count=0,0

        for i in nums:
            if count==0:
                key=i
            if key==i:
                count+=1
            else:
                count-=1

        return key
