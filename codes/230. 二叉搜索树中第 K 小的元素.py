# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:


        def findk(root,k):

            left,right=childnum(root.left),childnum(root.right)
            if left ==k-1:
                return root.val
            elif left<k-1:
                return findk(root.right,k-left-1)
            elif left>k-1:
                return findk(root.left,k-right-1)



        def childnum(root):
            if root is None:
                return 0
            left,right=childnum(root.left),childnum(root.right)

            return left+right+1

        return findk(root,k)
