# leetCode n°189
# Difficulty : medium

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
       
        N = len(nums)
        step = k % N
        nums[:] =  nums[N-step:] + nums[:N-step]
        
        return nums
    
# Runtime: 188 ms, faster than 77.26% of Python online submissions for Rotate Array.
# Memory Usage: 25.2 MB, less than 14.33% of Python online submissions for Rotate Array.
