# Top100LikedQuestions
# LeetCode n°53
# Difficulty : easy

#1st implementation : 2 nested loops 
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_max = nums[0] #init max sum
        print(nums)
        
        for firstIndex in range(0, len(nums)):
            for lastIndex in range(firstIndex+1,len(nums)+1):
                tot = sum(nums[firstIndex:lastIndex])
                #print(firstIndex, lastIndex, tot)
                if tot > sum_max:
                    sum_max = tot
                
        return sum_max

#2nd implementation : Divide and conquer
class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #print(nums[0:4])
        #print(nums[4:-1])
        return self.MaxSubArraySum(nums, 0, len(nums)-1)
    
    def MaxSubArraySum(self,arr, start, end):
        # print(arr)
        if start == end: #base case
            return arr[start]
        else:
            mid = (start + end)/2
            #print(mid)
            LeftSubArr = self.MaxSubArraySum(arr, start, mid)
            RightSubArr = self.MaxSubArraySum(arr, mid+1, end)
            CrossSubArr = self.MaxCrossSubArraySum(arr, start, mid, end)
        
        return max(LeftSubArr, RightSubArr, CrossSubArr)
            
    def MaxCrossSubArraySum(self,arr, start, mid, end):
        crossSumL = -1000
        crossSumR = -1000
        
        s=0
        for i in range(mid+1, end + 1):
            s = s + arr[i]
            if s > crossSumR:
                crossSumR = s
        
        #print('second for')
        s = 0
        for j in range(mid,start-1,-1):
            s = s + arr[j]
            if s > crossSumL:
                crossSumL = s
                
        return crossSumL + crossSumR

#3rd implementation : Kadane's algorithm		
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Kadane's algorithm 
        # maxSum[i] = max(A[i], A[i] + maxSum[i-1])
        
        currentSum = nums[0]
        totalMax = currentSum
        
        if len(nums) == 1:
            return nums[0]
        
        for i in range(1,len(nums)):
            currentSum = max(nums[i], nums[i] + currentSum)
            print(currentSum, totalMax)
            
            if currentSum > totalMax:
                totalMax = currentSum
        
        return totalMax
            
