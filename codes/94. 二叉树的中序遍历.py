# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:


        ans=self.inorder(root)

        return ans
    def inorder(self,root):
        ans=[]
        stack=[]
        while root or stack:

            while  root:
                stack.append(root)
                root=root.left

            node=stack.pop()
            ans.append(node.val)

            root=node.right
        return ans

