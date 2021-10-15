# leetCode n°
# difficulty : easy

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxVal = max(nums)
        idx = nums.index(maxVal)
        #rint('maxVal, idx :', maxVal, idx)
        N = len(nums)
        for i in range(N):
            if nums[i] != maxVal:
                if maxVal < 2*nums[i]:
                    return -1
        
        return idx
    
#untime: 27 ms, faster than 37.83% of Python online submissions for Largest Number At Least Twice of Others.
#emory Usage: 13.5 MB, less than 37.17% of Python online submissions for Largest Number At Least Twice of Others.

