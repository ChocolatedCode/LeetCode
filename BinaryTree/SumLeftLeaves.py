# leetCode n° 404
# Difficulty : easy

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        total = 0
        
        if root:
            if root.right is None and root.left is None:
                return 0

            if self.leftLeaf(root.left):
                total += root.left.val
                # print('left : ', total)
            else:
                total += self.sumOfLeftLeaves(root.left)
                # print('else : ', total)

            if root.right:
                total += self.sumOfLeftLeaves(root.right)

            # print('last : ', total)
        
        return total         
      
    def leftLeaf(self, root):
        #print(root)
        if root is None:
            return False
        if root.right is None and root.left is None:
            return True
           
            
            
            
