# Top100LikedQuestions
# n°617
# Difficulty : easy

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#1st implementation : Recursive
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
                        
        if root1 is None and root2 is None:
            return None
        #preorder reading
        if root1 is None:
            return root2
        elif root2 is None:
            return root1
        else:
            root1.val += root2.val
            root1.left = self.mergeTrees(root1.left, root2.left)
            root1.right = self.mergeTrees(root1.right, root2.right)
         
        return root1
        
