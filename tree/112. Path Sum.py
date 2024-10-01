# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    answer = False 

    def dfs(self, root, sum, targetSum):

        sum += root.val 

        if root.left == None and root.right == None:
            if sum == targetSum:
                self.answer = True 
            return 

        if root.left != None:
            self.dfs(root.left, sum, targetSum)
        
        if root.right != None:
            self.dfs(root.right, sum, targetSum)


    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if root == None:
            return False 
        
        self.dfs(root, 0, targetSum)

        return self.answer
