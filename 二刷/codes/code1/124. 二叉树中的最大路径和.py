# Definition for a binary tree node.
from typing import Optional
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -math.inf

        def returmax(root):
            nonlocal ans
            if not root:
                return 0

            left = max(returmax(root.left), 0)
            right = max(returmax(root.right), 0)

            ans = max(ans, root.val + left + right)

            return root.val + max(left, right)

        returmax(root)
        return ans