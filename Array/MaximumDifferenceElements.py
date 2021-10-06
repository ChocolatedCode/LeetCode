# leetCode n°2016
# Difficulty : easy

class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        diff = 0
        minVal = float('inf')
        N = len(nums)
        maxVal = 0
        
        for i in range(N):
            if nums[i] < minVal :
                minVal = nums[i]
            
            if nums[i] - minVal > diff and maxVal - minVal != 0:
                diff = nums[i] - minVal
            #print('diff : ', diff)
        
        if diff == 0:
            return -1
        return diff
                
                
# Runtime: 24 ms, faster than 97.82% of Python online submissions for Maximum Difference Between Increasing Elements.
# Memory Usage: 13.4 MB, less than 95.33% of Python online submissions for Maximum Difference Between Increasing Elements.
        
