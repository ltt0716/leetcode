from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans=0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.childlen(root)
        return self.ans
    def childlen(self,root):
        if root == None:
            return -1
        max_left = self.childlen(root.left) + 1
        max_right = self.childlen(root.right) + 1

        self.ans=max(self.ans,max_left+max_right)
        return max(max_left,max_right)