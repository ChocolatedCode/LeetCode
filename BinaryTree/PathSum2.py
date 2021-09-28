# leetCode n°113
# Difficulty : medium

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        
        def leaf(node = root, total = 0, path = []):
            #print('node :', node.val)
            print('total : ', total)
            #print('path : ', path)
            if node is None:
                return []
            if not (node.left or node.right) and total+node.val == targetSum:
                # print('path : ', path)
                path.append(node.val)
                paths.append(path[:])
                
            leaf(node.left, total+node.val, path+[node.val])
            leaf(node.right, total+node.val, path+[node.val])
        
        paths = []
        leaf()
        return paths
    
# Runtime: 80 ms, faster than 5.24% of Python online submissions for Path Sum II.
# Memory Usage: 19.9 MB, less than 10.43% of Python online submissions for Path Sum II.

