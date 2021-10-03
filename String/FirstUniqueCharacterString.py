# leetCode n°387
# Difficulty : easy

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        strDict = {}
        # count each letter and record it in a dict
        for i in s:
            if i not in strDict:
                strDict[i] = 1
            else: 
                strDict[i] += 1
                
        #print('mmyStrDict : ', strDict)
        
        # go through s to find first letter
        for i in range(len(s)):
            if strDict[s[i]] == 1:
                return i
            
        return -1
        
# Runtime: 120 ms, faster than 77.94% of Python online submissions for First Unique Character in a String.
# Memory Usage: 14.4 MB, less than 43.10% of Python online submissions for First Unique Character in a String.
