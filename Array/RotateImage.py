# leetCode n°48
# Difficulty : medium

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        matrix = [[matrix[j][i] for j in range(n)] for i in range(n)]
        print('transpose : ', matrix)
        
        for row in range(n):
            for column in range(n//2):
                # print(n//2)
                # print(matrix[row][column], matrix[row][n-1-column])
                matrix[row][column],matrix[row][n-1-column] = matrix[row][n-1-column], matrix[row][column]

        print('final : ', matrix)
        
