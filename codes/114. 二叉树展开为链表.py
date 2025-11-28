from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:

        def convert(root):
            if root is None:
                return None

            l_tail,r_tail=convert(root.left),convert(root.right)

            if l_tail:
                l_tail.right=root.right
                root.right=root.left
                root.left=None

            return r_tail or l_tail or root

        return convert(root)