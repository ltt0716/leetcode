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

        ans=-math.inf
        
        def remax(root):
            if not root:
                return 0
            
            left=remax(root.left)
            right=remax(root.right)
            nonlocal ans
            res=root.val+max(0,left)+max(0,right)
            ans=max(ans,res)
            return root.val+max(0,left,right)
        
        remax(root)

        return ans