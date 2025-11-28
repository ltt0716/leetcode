# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans=[]

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]

        def dfs(root, targetSum):
            if root is None:
                return
            nonlocal ans
            ans.append(root.val)
            targetSum -= root.val

            if root.left == root.right and root.left is None:
                if targetSum == 0:
                    self.ans.append(ans.copy())
            else:
                dfs(root.left, targetSum)
                dfs(root.right,targetSum)
            ans.pop()

        dfs(root,targetSum)

        return self.ans

