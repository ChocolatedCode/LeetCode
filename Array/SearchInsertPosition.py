# LeetCode n°35
# Difficulty : easy

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        while start <= end:
            
            mid = (start + end)/2
            print(start, mid , end, nums[mid])
            if target == nums[mid]:#if place found
                return mid
            
            if target > nums[mid]:#if target in upper part
                start = mid + 1 #go right
            else:
                end = mid - 1 #go left
                
                           
        return end + 1
                
            
        


               
