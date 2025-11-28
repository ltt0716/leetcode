# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root:
                return None
            
            left_tail,right_tail=dfs(root.left),dfs(root.right )
            if left_tail:
                left_tail.right=root.right
                root.right=root.left
                root.left=None
            
            return right_tail or left_tail or root
        
        return dfs(root)