# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

#         if not nums:
#             return None
#         i,j=0,len(nums)
#         mid=i//2

#         root=TreeNode(val=nums[mid])
#         root.left=self.sortedArrayToBST(nums[i:mid])
#         root.right=self.sortedArrayToBST(nums[mid+1:j])

#         return root

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def dfs(l,r):
            if l>r:
                return None
            
            mid=(l+r)//2
            root=TreeNode(val=nums[mid])

            root.left=dfs(l,mid)
            root.right=dfs(mid+1,r)

            return root
        return dfs(0,len(nums)-1)