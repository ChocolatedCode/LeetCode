# Contains Duplicate
# leetCode n°217, 

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Works, but not adapted for big list
        """
        mySet = []
        
        for n in nums:
            if n in mySet:
                return True
            else:
                mySet.append(n)
        
        return False
        """
        
        if len(nums) == len(set(nums)):
            return False
        
        return True
        # Runtime: 100 ms, faster than 55.85% of Python online submissions for Contains Duplicate.
        # Memory Usage: 19.1 MB, less than 53.41% of Python online submissions for Contains Duplicate.
        
        # PART 2
                for firstIdx in range(len(nums)):
            for secondIdx in range(firstIdx+1,len(nums)):
                if nums[firstIdx] == nums[secondIdx]:
                    if abs(firstIdx - secondIdx) <= k:
                        return True
        
        
        return False
                
