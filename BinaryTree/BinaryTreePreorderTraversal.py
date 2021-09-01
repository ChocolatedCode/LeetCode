# LeetCode n°144
# Difficulty : easy

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
                
        res = []
        self.preOrderNode(root, res)
                
        return res
    
    def preOrderNode(self, currentNode, resList):
        
        if currentNode:
            resList.append(currentNode.val)
            self.preOrderNode(currentNode.left, resList)
            self.preOrderNode(currentNode.right, resList) 
    
# Runtime: 12 ms, faster than 94.81% of Python online submissions for Binary Tree Preorder Traversal.
# Memory Usage: 13.7 MB, less than 5.15% of Python online submissions for Binary Tree Preorder Traversal.
  
            
