# Top100LikedQuestions
# leetCode n°283
# Difficulty : easy

#1st implementation
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
                #print(nums)
			
				
#2nd implementation 
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #if len(nums) == 1:
         #   return
        j = 1
        for currentElem in range(len(nums)-1):
            #print('current : ', currentElem)
            if nums[currentElem] == 0:
                #print('current : ', currentElem)
                j = currentElem+1
                nextElem = nums[j]
                while nextElem == 0 and j < len(nums)-1:
                    j+=1
                    nextElem = nums[j]
                nums[currentElem] = nums[j]
                nums[j] = 0
            
                
				
				
