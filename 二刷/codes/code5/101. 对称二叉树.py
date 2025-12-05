# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        

            
        return self.check(root.left.root.right)
    

    def check(self,q,p):
            if p in None or q is None:
                return None      
            
            return p.val ==q.val and self.check(p.left,q.right) and self.check(p.right,q.left)