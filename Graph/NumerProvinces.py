# leetCode n°547
# Difficulty : medium

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        
        def dfs(i):
            for j in range(m):
                # print('i, j', i,j)
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)
                #print('visited : ', visited)
                    
        m = len(isConnected)
        visited = set()
        count = 0
        
        for i in range(m):
            # print('i : ', i)
            if i not in visited:
                dfs(i)
                count+=1        
        return count
        
# Runtime: 156 ms, faster than 81.94% of Python online submissions for Number of Provinces.
# Memory Usage: 14.1 MB, less than 18.21% of Python online submissions for Number of Provinces.     
        
