# Definition for a binary tree node.
from typing import Optional, List
from _collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        if not root:
            return []
        q = deque([root])

        while q:
            k = len(q)

            while k > 0:
                root = q.popleft()
                left, right = root.left, root.right
                if left:
                    q.append(left)
                if right:
                    q.append(right)
                if k == 1:
                    ans.append(root.val)
                k -= 1
        return ans


