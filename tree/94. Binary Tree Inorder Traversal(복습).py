# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root, result):

        if root == None:
            return 

        self.dfs(root.left, result)
        result.append(root.val)
        self.dfs(root.right, result)


    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        

        result = []
        self.dfs(root, result)

        return result 
