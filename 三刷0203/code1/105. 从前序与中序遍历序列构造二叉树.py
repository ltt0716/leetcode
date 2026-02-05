# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        order={}
        for  index,val in enumerate(inorder):
            order[val]=index


        def dfs(prel,prer,inl,inr):
            if prer<prel:
                return None
                
            root=TreeNode(val=preorder[prel])

            order_index=order[preorder[prel]]

            left_num=order_index-inl
            right_num=inr-order_index

            root.left=dfs(prel+1,prel+left_num,inl,order_index-1)
            root.right=dfs(prer-right_num+1,prer,order_index+1,inr)

            return root
        
        return dfs(0,len(preorder)-1,0,len(inorder)-1)
        