# LeetCode n°9
# Difficulty : easy

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #if x < 0 :
        #    return False
        
        myNum = str(x)
        revNum = ''
               
        for n in range(len(myNum)-1, -1, -1):
            revNum += myNum[n]

        if myNum == revNum:
            return True
        
        return False
    
    
    

    
    
        
