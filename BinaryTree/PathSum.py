# leetCode n°112
# Difficulty : easy

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
     
        def dfs(node = root, total = 0):
            # print('node : ', node.val)
            if not node:
                return False
            total += node.val
            if not (node.left or node.right) and total == targetSum:
                return True
            return dfs(node.left, total) or dfs(node.right, total)
       
        return dfs()
      
# Runtime: 28 ms, faster than 93.13% of Python online submissions for Path Sum.
# Memory Usage: 15.6 MB, less than 50.00% of Python online submissions for Path Sum.
