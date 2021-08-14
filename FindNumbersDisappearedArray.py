# Top100LikedQuestions
# n°448
# Difficulty : easy

#1st implementation
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        nums = list(dict.fromkeys(nums))
        print(nums)
        for i in range(1,n+1):
            if i not in nums:
                nums.append(i)
            else:
                nums.remove(i)
        
        return nums
		
#2nd implementation : set difference
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return set(range(1,len(nums)+1)) - set(nums)
		
	
	
	
