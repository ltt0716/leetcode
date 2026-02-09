# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0
            
            return 1+max(dfs(root.left),dfs(root.right)) 
        
        ans=0
        def getans(root):
            nonlocal ans

            left=dfs(root.left)
            right=dfs(root.right)

            ans=max(ans,left+right)

            return max(left,right)
        getans(root)
        return ans