# Definition for a binary tree node.
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt=defaultdict(int)
        cnt[0]=1
        arr=0
        ans=0

        def dfs(root):
            nonlocal arr,ans
            if not root:
                return
            ans+=cnt[arr-targetSum]
            arr+=root.val

            if root.left:
                dfs(root.left)
                arr-=root.left.val
            if root.right:
                dfs(root.right)
                arr-=root.right.val

        return ans
