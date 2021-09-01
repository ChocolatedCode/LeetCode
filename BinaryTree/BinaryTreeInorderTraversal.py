# Top100LikedQuestions
# leetCode n°94
# Difficulty : easy


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#1st impleemntation : Recursive approach
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # recursive approach : O(n) time,O(n) space worst case (O(logn))
        res = []

        if root is None:
            return []
        if root.left:
            res += (self.inorderTraversal(root.left))
        if root: 
            res.append(root.val)
        if root.right:
            res += (self.inorderTraversal(root.right))
        
        return res

#2nd implementation : using stack
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # iterative using stack
        res = []
        myStack = []
    
        currentNode = root
        while myStack!=[] or currentNode is not None:
            while currentNode is not None:
                myStack.append(currentNode)
                currentNode = currentNode.left

            currentNode = myStack.pop()
            res.append(currentNode.val)
            currentNode = currentNode.right     
            
        return res
            
            
