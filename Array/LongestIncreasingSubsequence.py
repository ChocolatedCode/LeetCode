# leetCode n°300
# Difficulty : medium

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
    
        def LongestSub(nums):
            N = len(nums)

            LIS = [1 for _ in range(N)]
            #print('LIS : ', LIS)

            for last in range(1,N):
                for first in range(last):
                    #print('nums : ', nums[first], nums[last])
                    if nums[first] < nums[last] and LIS[last] < LIS[first] + 1:
                        #print('temp : ',LIS[first] + 1)
                        LIS[last] = LIS[first] + 1
                       
            #print('res LIS : ', LIS, max(LIS))
            
            return max(LIS)
                        
        return LongestSub(nums)   
