import collections
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
      l=r=ans=s=0

      n=len(nums)

      dir=collections.defaultdict(int)

      while r<n:
          c=nums[r]
          s+=dir[c]
          dir[c]+=1

          while s>=k:
              dir[nums[l]]-=1
              if dir[nums[l]]>=1:
                  s-=dir[nums[l]]
              l+=1
          ans+=l
          r+=1

      return ans


