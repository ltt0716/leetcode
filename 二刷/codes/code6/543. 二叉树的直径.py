# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        ans=0
        def retmax(root):
            nonlocal ans

            if not root:
                return 0
            
            left=retmax(root.left)
            right=retmax(root.right)

            ans=max(ans,right+left)

            return max(left,right)+1

        retmax(root)

        return ans

