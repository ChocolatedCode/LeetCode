# Top100LikedQuestions
# n°136
# Difficulty: easy

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        existingArr = []
        for i in nums:
            if i not in existingArr:
                existingArr.append(i)
            else:
                existingArr.remove(i)
        
        return existingArr[0]
