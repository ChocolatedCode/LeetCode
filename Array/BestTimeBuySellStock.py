# Top100LikedQuestions
# leetCode n°121
# Difficulty easy

#1st implementation : 2 nested loops : 0(n^2) time
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = -1000 #what we want to maximize 
        for idxBuy in range(len(prices)): # O(n)
            for idxSell in range(idxBuy+1, len(prices)): # O(n)
                if prices[idxSell] - prices[idxBuy] > profit:
                    profit = prices[idxSell] - prices[idxBuy]
                
        
        if profit < 0 :
            return 0
        else:
            return profit # O(1) space

#--------------------------------------------------------------------#

#2nd implementation : one for loop		
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minBuy = prices[0] # O(1) space
        profit = 0 #what we want to maximize
        
        for p in prices[1:]: # O(n) time
            if p<minBuy:
                minBuy = p
            currentProfit =  p - minBuy 
            if currentProfit > profit:
                profit = currentProfit
            
        return profit

#--------------------------------------------------------------------#

#3rd implementation : Divide and Conquer O(logn) time 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # print(prices)
        return self.maxDC(prices, 0, len(prices))
    
    def maxDC(self, subArr, start, end): #divide and conquer
        
        #print(start, end,end-start)
        
	#base case
        if end-1 == start: #single number
            profit = 0
            #print('a', start, end)
            return profit
        elif (end-start)-1 == 1:#two numbers
            profit = subArr[end-1] - subArr[start]
            #print('b', profit, start, end)
            if profit < 0:
                profit = 0
            return profit
        else:
            mid = (start + end)/2
            #print('mid : ', mid)
            leftValue = self.maxDC(subArr, start, mid)
            #print('left : ', leftValue)
            rightValue = self.maxDC(subArr, mid, end)
            #print('right : ', rightValue)
            crossMin = min(subArr[start:mid])
            crossMax = max(subArr[mid:end])
            crossValue = crossMax - crossMin
            #print('cross : ', crossMax-crossMin)
            #print(subArr[mid:end])
            
            
        profit = max(leftValue, rightValue, crossValue)
        if profit < 0:
            profit = 0
        #print('c', profit, start, end)  
        #print('here')
	
        return profit # O(1) space
		
		
		
		
		
    
            
