from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True

        return self.isametree(root.left,root.right)

    def isametree(self,p,q):
        if p ==None or q==None:
            return q==p
        else:
            return p.val==q.val and self.isametree(p.left,q.right) and self.isametree(p.right,q.left)


