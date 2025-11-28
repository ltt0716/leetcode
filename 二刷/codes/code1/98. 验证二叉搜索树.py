# Definition for a binary tree node.
from typing import Optional
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def returnbigger(self,root):

        if not root:
            return -math.inf

        leftmax, rightmax = -math.inf, -math.inf

        if root.left:
            leftmax =self.returnbigger(root.left)
        if root.right:
            rightmax = self.returnbigger(root.right)

        return max(root.val, leftmax, rightmax)
    def returnsmaller(self,root):

        if not root:
            return math.inf

        leftmin, rightmin = math.inf, math.inf

        if root.left:
            leftmin =self.returnsmaller(root.left)
        if root.right:
            rightmin = self.returnsmaller(root.right)

        return min(root.val, leftmin, rightmin)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left,right=True,True
        if root.left:
            if root.val <= self.returnbigger(root.left):
                return False
            left=self.isValidBST(root.left)

        if root.right:
            if root.val <= self.returnsmaller(root.right):
                return False
            right= self.isValidBST(root.right)

        return left and right


