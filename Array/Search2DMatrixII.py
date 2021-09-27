# leetCode n° 240
# Difficulty : medium

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        
        for row in matrix:
            if target >= row[0] and target <= row[-1]:
                for num in row:
                    if num == target:
                        return True
        
        return False
    
# Runtime: 136 ms, faster than 82.31% of Python online submissions for Search a 2D Matrix II.
# Memory Usage: 19.3 MB, less than 99.13% of Python online submissions for Search a 2D Matrix II.
