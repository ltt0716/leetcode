from  collections import deque 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque([root])

        ans=[]

        while q:
            k=len(q)
            tp=[]
            while k:
                node=q.popleft()
                tp.append(node.val)
                q.append(node.left)
                q.append(q.right)
            
            ans.append(tp)
        
        return ans