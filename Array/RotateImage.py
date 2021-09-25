# leetCode n°48
# Difficulty : medium

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        #matrix = [[matrix[j][i] for j in range(n)] for i in range(n)] # correct but not modify in place
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i] 
        print('transpose : ', matrix)
        
        for row in range(n):
            for column in range(n//2):
                # print(n//2)
                # print(matrix[row][column], matrix[row][n-1-column])
                matrix[row][column],matrix[row][n-1-column] = matrix[row][n-1-column], matrix[row][column]

        print('final : ', matrix)
        
# Runtime: 24 ms, faster than 56.31% of Python online submissions for Rotate Image.
# Memory Usage: 13.4 MB, less than 72.45% of Python online submissions for Rotate Image.
        
