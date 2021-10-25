# leetCode n°
# Difficulty : hard

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        setA = set(nums)
        setB = set(range(1,len(nums)+1))
        print('setB : ',setB)
        diff = setB-setA
        print('diff : ', diff)
        
        if not diff:
            return list(setB)[-1] + 1
        
        return min(diff) #diff.pop() 
