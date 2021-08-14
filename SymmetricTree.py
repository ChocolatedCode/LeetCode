# Top100LikedQuestion
# n°101
# Difficulty : easy

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#1st implementation : Recursive O(n) time and O(n) space
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.subTreeSymmetric(root,root)
        
    
    def subTreeSymmetric(self, subRightTree, subLeftTree):
        #roots
        #print(subRightTree, subLeftTree)
        if subRightTree is None and subLeftTree is None:
            return True
        if subRightTree is None or subLeftTree is None:
            return False
        
        resL = self.subTreeSymmetric(subRightTree.right, subLeftTree.left)
        resR = self.subTreeSymmetric(subRightTree.left, subLeftTree.right)
        if resL == True and resR == True and subRightTree.val == subLeftTree.val:
            return True
        else:
            return False
			
			
			

			
