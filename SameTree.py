# leetCode n°100
# Difficulty : easy

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q): # O(n) time (go through entire tree, n nodes)
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        #print(p.val, q.val)
        # if the roots are the same
        if p is None and q is None:
            return True
        #if only one of the root is None
        elif p is None or q is None:
            return False
        # if there is two differents values
        elif p.val != q.val:
            return False
        # if roots are the same
        else:
            # if left, right are the same
            left = self.isSameTree(p.left, q.left) # are left child values the same
            right = self.isSameTree(p.right, q.right)# are right child values the same
        
        return (left and right) # true if child right and left are the same
        # if balanced tree : O (log n) space, else O(n) space
      
# Runtime: 16 ms, faster than 77.04% of Python online submissions for Same Tree.
# Memory Usage: 13.6 MB, less than 13.03% of Python online submissions for Same Tree.   
        
            
            
            
        
