# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:

    answer = True 

    def getHeight(self, root, height):

        leftHeight = 0
        rightHeight = 0 

        if root.left == None and root.right == None:
            return height

        if root.left == None and root.right != None:
            leftHeight = height
            rightHeight = self.getHeight(root.right, height+1)
        if root.left != None and root.right == None:  
            leftHeight = self.getHeight(root.left, height+1)
            rightHeight = height  
        if root.left != None and root.right != None:
            leftHeight = self.getHeight(root.left, height+1)
            rightHeight = self.getHeight(root.right, height+1) 
            
        if abs(leftHeight-rightHeight) >= 2:
            self.answer = False 

        return max(leftHeight, rightHeight)
        


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root == None:
            return True 
        else:
            self.getHeight(root, 1)

            if self.answer == True:
                return True
            else:
                return False 
