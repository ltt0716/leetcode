from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[1]!=inf

    def dfs(self,node):
        if node is None:
            return inf,-inf

        l_min,l_max=self.dfs(node.left)
        r_min,r_max=self.dfs(node.right)

        cur=node.val

        if cur<=l_max or cur>=r_min:
            return -inf,inf

        return min(l_min,cur),max(cur,r_max)



