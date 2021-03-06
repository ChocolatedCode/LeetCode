# Top100LikedQuestions
# n°70
# Difficulty : easy

#1st implementation : Recursive
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.ComputeWays(0,n)
        
    def ComputeWays(self, currentStep, finalStep) :
        #base case
        if currentStep > finalStep:
            return 0
        if currentStep == finalStep:
            return 1
        
        return self.ComputeWays(currentStep + 1, finalStep) + self.ComputeWays(currentStep + 2, finalStep)
    
  
#2nd implementation : Memoization
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prevList = [0 for i in range(n)]
        return self.ComputeWays(0,n, prevList)
        
    def ComputeWays(self, currentStep, finalStep, previousList) :
        #base case
        if currentStep > finalStep:
            #print('o')
            return 0
        if currentStep == finalStep:
            #print('1')
            return 1
        
        if previousList[currentStep] > 0:
            #print('last')
            return previousList[currentStep]
        
        #print('final')
        previousList[currentStep] = self.ComputeWays(currentStep + 1, finalStep, previousList) + self.ComputeWays(currentStep + 2, finalStep, previousList)
		
        return previousList[currentStep]
    
        
        
          
        
        
