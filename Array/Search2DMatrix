# leetCode n°74
# Difficulty : medium

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        Nr = len(matrix)
        Nc = len(matrix[0])
        
        if len(matrix) == 1 and len(matrix[0]) == 1:
            if matrix[0][0] == target:
                return True
            else:
                return False
            
        #find row
        for i in range(0, Nr):
            # print('first elem : ',  matrix[i][0])
            if target < matrix[i][0]:
                i = i - 1
                break
        
        # print('row : ', i)
        # find col
        """
        # 1st solution 
        for j in range(Nc):
            if target == matrix[i][j]:
                return True
        return False
        # Runtime: 59 ms, faster than 5.23% of Python online submissions for Search a 2D Matrix.
        # Memory Usage: 13.7 MB, less than 94.92% of Python online submissions for Search a 2D Matrix.    
        """
        
        # 2nd solution
        firstIdx = 0
        lastIdx = Nc - 1
        
        while firstIdx <= lastIdx:
            mid = (lastIdx - firstIdx) //2
            # print(mid, firstIdx, lastIdx)
            if target == matrix[i][firstIdx] or target == matrix[i][lastIdx] or target == matrix[i][mid]:
                # print('mid : ', mid)
                return True
            if target < matrix[i][mid]:
                lastIdx = mid
                firstIdx += 1
            if target > matrix[i][mid]:
                firstIdx = mid
                lastIdx -= 1
        
        return False
        
        # Runtime: 38 ms, faster than 22.35% of Python online submissions for Search a 2D # # Matrix.
        # Memory Usage: 13.9 MB, less than 20.48% of Python online submissions for Search a # 2D Matrix.
        
