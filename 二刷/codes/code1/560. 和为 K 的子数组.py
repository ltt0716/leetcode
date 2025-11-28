import collections
from  typing  import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        arr=0
        cnt=collections.defaultdict(int)
        cnt[0]=1

        ans =0
        for num in nums:
            arr+=num

            ans+=cnt[arr-k]

            cnt[arr]+=1

        return ans
