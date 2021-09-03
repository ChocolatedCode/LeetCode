# leetCode n° 671
# Difficulty: easy

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node) : #depth-first search
            if node:
                myArr.add(node.val)
                dfs(node.left)
                dfs(node.right)
                

        myArr = set() # O(N) space
        dfs(root) # O(N) time 
        
        # print (myArr)
        
        minV = root.val
        minV2 = float('inf')
        
        for val in myArr : # O(N) time
            if val > minV and val < minV2:
                minV2 = val
        
        return minV2 if minV2 != float('inf') else -1
    
# Runtime: 24 ms, faster than 11.23% of Python online submissions for Second Minimum Node In a Binary Tree.
# Memory Usage: 13.5 MB, less than 43.51% of Python online submissions for Second Minimum Node In a Binary Tree.
