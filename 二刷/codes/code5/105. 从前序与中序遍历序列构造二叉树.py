# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def dfs(pl,pr,il,ir):

            if pr<pl :
                return None
            
            x=preorder[pl]
            root=TreeNode(val=x)

            index=inorder.index(x)

            llen=index-il
            rlen=ir-index

            root.left=dfs(pl+1,pl+llen,il,index-1)
            root.right=dfs(pr-rlen+1,pr,index+1,ir)

            return root
        

        root=dfs(0,len(preorder)-1,0,len(inorder)-1)
        return root




        