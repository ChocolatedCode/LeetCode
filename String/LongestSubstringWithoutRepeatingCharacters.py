# leetCode n°3
# Difficulty : medium

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        firstIdx = 0 # beginning of substring
        lastIdx = 0 # end of...
        N = len(s)
        # print('N:', N)
        maxL = 0
        currentSubStr = '' # substring

        while firstIdx < N and lastIdx < N: # O(N) time 
            if s[lastIdx] in currentSubStr : 
                if len(currentSubStr) > maxL: # O(N)
                    maxL = len(currentSubStr)
                                                  
                firstIdx += 1 # move of one character for the new substring
                lastIdx = firstIdx + 1
                countSpace = 0
                currentSubStr = s[firstIdx]            
            else: # if character not in substring, add it
                currentSubStr += s[lastIdx]
                lastIdx += 1
            # print('curr:', currentSubStr)
        # print('max : ', maxL, len(currentSubStr))
        
        return max(maxL,len(currentSubStr)) # return last substring or the previous formed
      
# Runtime: 883 ms, faster than 13.58% of Python online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 13.7 MB, less than 72.81% of Python online submissions for Longest Substring Without Repeating Characters.

                
                
