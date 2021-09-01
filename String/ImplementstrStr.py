# leetCode n°28
# Difficulty : easy

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        N = len(needle)
        M = len(haystack)
        
        if M == N and needle == haystack:
            return 0
        
        for i in range(M - N + 1): # O(N) time
            #print(haystack[i:i+N])
            if haystack[i:i+N] == needle:
                return i
        
        return -1
        
  
# Runtime: 280 ms, faster than 45.42% of Python online submissions for Implement strStr().
# Memory Usage: 14.5 MB, less than 42.67% of Python online submissions for Implement strStr().
