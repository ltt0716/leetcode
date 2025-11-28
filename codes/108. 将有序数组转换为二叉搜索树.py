# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        l=len(nums)
        if l==0:
            return None
        mid_index=l//2

        left=self.sortedArrayToBST(nums[:mid_index])
        right=self.sortedArrayToBST(nums[mid_index+1:])

        return TreeNode(nums[mid_index],left,right)



