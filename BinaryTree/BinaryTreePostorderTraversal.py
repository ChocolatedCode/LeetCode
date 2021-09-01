# leetCode n°145
# Difficulty : easy

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.postOrderNode(root, res)
                
        return res
    
    def postOrderNode(self, currentNode, resList):   
        if currentNode is None :
            return []
        
        self.postOrderNode(currentNode.left, resList)
        self.postOrderNode(currentNode.right, resList)
        resList.append(currentNode.val)
            
# Runtime: 12 ms, faster than 93.96% of Python online submissions for Binary Tree Postorder Traversal.
# Memory Usage: 13.4 MB, less than 50.07% of Python online submissions for Binary Tree Postorder Traversal.      
        
            
            
                                   
            
            
            
            
    
  
            
