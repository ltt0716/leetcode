import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        n = len(nums)
        # 核心转换：找第 k 大的元素，等价于在从小到大排序后的数组中找索引为 n-k 的元素
        target_index = n - k
        return self.quick_select(nums, 0, n - 1, target_index)

    def quick_select(self, nums: List[int], left: int, right: int, k: int) -> int:
        """
        在 nums 的 [left, right] 区间内，找到排序后索引为 k 的元素。
        """
        # 如果区间只有一个元素，那它就是我们要找的
        if left == right:
            return nums[left]

        # Hoare 分区方案 (C++ 版本的 Python 实现)
        # 1. 选择基准点
        pivot = nums[left]

        # 2. 初始化左右指针，注意它们从区间的“外部”开始
        i, j = left - 1, right + 1

        # 3. 分区操作
        while i < j:
            # i 从左向右找，直到找到一个 >= pivot 的数
            i += 1
            while nums[i] < pivot:
                i += 1

            # j 从右向左找，直到找到一个 <= pivot 的数
            j -= 1
            while nums[j] > pivot:
                j -= 1

            # 如果 i 还在 j 左边，说明找到了错位的元素对，交换它们
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        # 4. 根据 k 的位置，决定去哪个子区间递归
        # 循环结束后，j 左边的都 <= pivot, j 右边的都 >= pivot
        if k <= j:
            # 目标在左半部分
            return self.quick_select(nums, left, j, k)
        else:
            # 目标在右半部分
            return self.quick_select(nums, j + 1, right, k)