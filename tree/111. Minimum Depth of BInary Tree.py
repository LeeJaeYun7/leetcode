# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    minHeight = 1e9 

    def dfs(self, root, height):
        if root == None:
            return

        if root.left == None and root.right == None:
            self.minHeight = min(self.minHeight, height)
            return 

        self.dfs(root.left, height+1)
        self.dfs(root.right, height+1)        

    def minDepth(self, root: Optional[TreeNode]) -> int:

        if root != None:
            self.dfs(root, 1)
        else:
            self.minHeight = 0 
            
        return self.minHeight
