# leetCode n°1137
# Difficulty : easy

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 0:
            return 0
        if n < 2:
            return 1
        
        T = [0 for i in range(n+1)]
        
        T[1] = 1
        T[2] = 1
        
        for n in range(3, n+1):
            T[n] = T[n-3] + T[n-2] + T[n-1]
        
        return T[-1]
        
        
