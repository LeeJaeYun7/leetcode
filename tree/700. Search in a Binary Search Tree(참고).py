# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.subRoot = None

    def dfs(self, root, val):
        if root is None:
            return 

        if root.val == val:
            self.subRoot = root
            return 

        self.dfs(root.left, val)
        self.dfs(root.right, val)

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.dfs(root, val)
        return self.subRoot
