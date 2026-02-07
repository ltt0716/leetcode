# Definition for a binary tree node.
import deque
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        q=deque()
        q.append([root])

        ans=[]
        while q:
            li=deque(q.pop())

            now=[]

            while li:

                cur=li.popleft()
                if len(li)==0:
                    ans.append(cur.val)
                if not cur.left:
                    now.append(cur.left)
                
                if not cur.right:
                    now.append(cur.right)

            q.append(now)
        return  ans
