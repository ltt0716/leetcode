from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        before = [0] * n
        after = [0] * n

        before[0] = 1
        after[n - 1] = 1

        for i in range(1, n):
            before[i] = before[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            after[i] = after[i + 1] * nums[i + 1]

        return [before[i] * after[i] for i in range(n)]

