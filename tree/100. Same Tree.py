# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root, result):
        if root == None:    
            result.append(-100000)
            return 

        result.append(root.val)
        if root.left == None and root.right == None:
            return 

        self.dfs(root.left, result)
        self.dfs(root.right, result)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        result1 = [] 
        self.dfs(p, result1)
        result2 = []
        self.dfs(q, result2)

        print(result1)
        print(result2)
        if result1 == result2:
            return True
        else:
            return False
