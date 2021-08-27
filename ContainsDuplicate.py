# Contains Duplicate
# leetCode n°217, 219

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
  
# PART 2
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        """
        M = len(nums)
        for firstIdx in range(M):
            for secondIdx in range(firstIdx+1,M):
                if nums[firstIdx] == nums[secondIdx] and firstIdx != secondIdx:
                    if abs(firstIdx - secondIdx) <= k:
                        return True
        
        
        return False
        """
    
        M = len(nums)
        idx = 0
        myDict = dict()
        while idx < M :
            if nums[idx] not in myDict:
                myDict[nums[idx]] = idx
            else:
                if abs(myDict[nums[idx]] - idx) <= k:
                    return True
                else:
                    myDict[nums[idx]] = idx
            idx += 1
            
        return False
        
        
        
        
        
                
        
                
