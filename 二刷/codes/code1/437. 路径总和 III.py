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
        ans=0
        cnt=collections.defaultdict(int)
        cnt[0]=1

        def dfs(root,target,s):
            if not root:
                return 0

            nonlocal ans
            s+=root.val

            ans+=cnt[s-target]

            cnt[s]+=1
            dfs(root.left,target,s)
            dfs(root.right,target,s)
            cnt[s]-=1

        dfs(root,targetSum,0)
        return ans

