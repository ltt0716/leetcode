# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0:
            return None

        val=preorder[0]
        root=TreeNode(val=val)
        index=inorder.index(val)
        preorder.pop(0)

        left_inorder=inorder[:index]
        right_inorder=inorder[index+1:]

        left_preorder=preorder[:len(left_inorder)]
        right_preorder = preorder[len(left_inorder):]

        root.left=self.buildTree(left_preorder,left_inorder)
        root.right=self.buildTree(right_preorder,right_inorder)

        return root


