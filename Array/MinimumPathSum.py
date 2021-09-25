# leetCode n°64
# Difficulty : medium

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        total = 0
        #go through grid and compute directly the new value
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:#start point
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] = min(grid[i][j] + grid[i][j-1], grid[i][j] + grid[i-1][j])
        
        return grid[-1][-1]
        
# Runtime: 80 ms, faster than 65.07% of Python online submissions for Minimum Path Sum.
# Memory Usage: 14.5 MB, less than 83.17% of Python online submissions for Minimum Path Sum.
