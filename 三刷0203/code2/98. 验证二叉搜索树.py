# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root,low,up):
            if not root:
                return True
            
            if root.val>=up:
                if up!=math.inf:
                    return False
            if root.val<=low:
                if low!=-math.inf:
                    return False
            
            return dfs(root.left,low,root.val) and dfs(root.right,root.val,up)
        
        return dfs(root)
        