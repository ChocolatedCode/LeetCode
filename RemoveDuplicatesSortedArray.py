# Top100LikedQuestions
# n°26
# Difficulty : easy

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        for j in range(1,len(nums)):
            if nums[j] != nums[i]: #if duplicate number
                i+=1
                nums[i] = nums[j]
            
        return i+1
