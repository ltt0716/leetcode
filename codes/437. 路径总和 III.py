# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        cnt= collections.defaultdict(int)
        cnt[0]=1
        count=0

        def dfs(root,k):
            if root is None:
                return

            nonlocal count

            k+=root.val

            count+=cnt[k-targetSum]

            cnt[k]+=1
            dfs(root.left,k)
            dfs(root.right,k)

            cnt[k]-=1

        dfs(root,0)

        return count






