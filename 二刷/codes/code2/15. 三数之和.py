from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        for i in range(n - 2):
            if nums[i] > 0:
                break

            left, right = 0, n - 1

            while left < right:
                cursum = nums[i] + nums[left] + nums[right]
                if cursum == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif cursum < 0:
                    left += 1
                else:
                    right -= 1

        return ans