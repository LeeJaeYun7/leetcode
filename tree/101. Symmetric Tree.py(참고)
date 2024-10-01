# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:        
        
        def isMirror(l1, l2):
            if not l1 and not l2:
                return True

            if not l1 or not l2:
                return False 

            return l1.val == l2.val and isMirror(l1.left, l2.right) and isMirror(l1.right, l2.left)


        return isMirror(root.left, root.right)
