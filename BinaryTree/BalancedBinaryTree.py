# leetCode n°110
# Difficulty : easy

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def heightTree(root):
            
            if root is None:
                return 0
            #print('root height : ', root.val)
            return max(heightTree(root.left), heightTree(root.right)) + 1
        
        if root is None:
            return True
        
        lh = heightTree(root.left)
        #print('left height : ', lh)
        rh = heightTree(root.right)
        #print('right height : ', rh)
        
        #print('root : ', root.val)
        
        if abs(lh - rh) <= 1 and self.isBalanced(root.right) and self.isBalanced(root.left):
            return True
        
        return False
    
# Runtime: 60 ms, faster than 41.38% of Python online submissions for Balanced Binary Tree.
# Memory Usage: 18.5 MB, less than 40.61% of Python online submissions for Balanced Binary Tree.
