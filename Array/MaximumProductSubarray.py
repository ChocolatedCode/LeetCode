# leetCode n°152
# Difficulty : medium

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Kadane's algorithm 
        # maxSum[i] = max(A[i], A[i] + maxSum[i-1])
        
        previousMax = nums[0]
        previousMin = nums[0]
        totalMax = previousMax
        
        if len(nums) == 1:
            return nums[0]
        
        for i in range(1,len(nums)):
            currentMax = max(nums[i], nums[i] * previousMax, nums[i] * previousMin)
            currentMin = min(nums[i], nums[i] * previousMax, nums[i] * previousMin)
            totalMax = max(currentMax, totalMax)
            previousMax = currentMax
            previousMin = currentMin

        return totalMax
    
    
# Runtime: 67 ms, faster than 12.40% of Python online submissions for Maximum Product Subarray.
# Memory Usage: 13.9 MB, less than 46.93% of Python online submissions for Maximum Product Subarray.   
        
    
