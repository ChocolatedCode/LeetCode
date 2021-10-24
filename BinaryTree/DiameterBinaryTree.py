# leetCode n°543
# Difficulty : easy

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def heightTree(root) :
            if root is None:
                return 0
            #print('root  : ', root.val)
            return max(heightTree(root.left), heightTree(root.right)) + 1
        
        if root is None:
            return 0
        
        print('main root : ', root.val)
        lh = heightTree(root.left)
        print('lh : ', lh)
        rh = heightTree(root.right)
        print('rh : ', rh)

        return max(lh + rh,max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right)))
