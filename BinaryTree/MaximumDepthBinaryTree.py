# Top100LikedQuestions
# n°104
# Difficulty : easy

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depthL = 0
        depthR = 0

        if root is None:
            return 0
        if root.left:
            depthL = self.maxDepth(root.left)
            print('L : ', depthL)

        if root.right:
            depthR = self.maxDepth(root.right)    
            print('R : ', depthR)
                    
        return max(depthL, depthR) + 1
		
		
		
		
