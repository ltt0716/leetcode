# Definition for a binary tree node.
from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        maxsum=-inf

        def maxgain(root):
            if root is None:
                return 0

            nonlocal maxsum
            left_gain=max(maxgain(root.left),0)
            right_gain=max(maxgain(root.right),0)

            newpath=root.val+left_gain+right_gain

            if newpath>maxsum:
                maxsum=newpath

            return root.val+max(left_gain,right_gain)

        maxgain(root)

        return maxsum

