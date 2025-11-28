# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if root is None:
            return False

        targetSum-=root.val

        if root.left ==root.right and root.left is None:
            if targetSum==0:
                return True
            else:
                targetSum+=root.val
                return False
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)