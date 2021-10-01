# leetCode n°198
# Difficulty : medium

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        
        N = len(nums)
        res = [0 for i in range(N)]
        
        if N <= 2:
            return max(nums)
        res[0] = nums[0]
        res[1] = max(nums[0], nums[1])
        
        for i in range(2, N):
            res[i] = max(res[i-2] + nums[i], res[i-1])
        
        return max(res)
            
# Runtime: 16 ms, faster than 85.31% of Python online submissions for House Robber.
# Memory Usage: 13.5 MB, less than 16.51% of Python online submissions for House Robber.
        

    
    
    
    
        
