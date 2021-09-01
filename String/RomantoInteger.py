# LeetCode n°13
# Difficulty : easy

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        myRomanNumbers = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        s = str(s)
        total = 0
        for i in range(len(s)-1):
            print('s[i]: ', s[i])
            if s[i] == 'I':
                if s[i+1] == 'V' or s[i+1] == 'X':
                    total -= myRomanNumbers[s[i]]
                else:
                    total += myRomanNumbers[s[i]]
            
            elif s[i] == 'X':
                if s[i+1] == 'L' or s[i+1] == 'C':
                    total -= myRomanNumbers[s[i]]
                else:
                    total += myRomanNumbers[s[i]]
            
            elif s[i] == 'C':
                if s[i+1] == 'D' or s[i+1] == 'M':
                    total -= myRomanNumbers[s[i]]
                else:
                    total += myRomanNumbers[s[i]]
            else:
                total += myRomanNumbers[s[i]]
            
        total += myRomanNumbers[s[-1]]
              
        return total
        
        
            
            
