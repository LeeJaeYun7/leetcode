# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    maxHeight = -1e9

    def dfs(self, root, height):

        self.maxHeight = max(self.maxHeight, height)    

        if root.left != None:
            self.dfs(root.left, height+1)

        if root.right != None:
            self.dfs(root.right, height+1)



    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root != None:    
            self.dfs(root, 1)
        else:
            self.maxHeight = 0 
            
        return self.maxHeight
