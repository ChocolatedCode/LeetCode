# leetCode n°1668
# Difficulty : easy

class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        
        n = len(word)
        m = len(sequence)
        k = 1
        p = word*k
        # print('pattern : ', p)
        count = 0
        
        while len(p) <= m:
            # print('k : ', k,k*n, p, sequence[:k*n])
            if p not in sequence:
                return count
            count += 1
            k+=1
            p = word*k

        # print('count : ', count)
        
        return count
            
        
# Runtime: 21 ms, faster than 35.35% of Python online submissions for Maximum Repeating Substring.
# Memory Usage: 13.7 MB, less than 13.13% of Python online submissions for Maximum Repeating Substring.
           
