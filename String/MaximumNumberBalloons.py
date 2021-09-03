# leetCode n°1189
# Difficulty easy

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        
        wrd = dict()
        letters = ['b','a','l','o','n']
        for ch in text: # O(N)
            if ch not in wrd and ch in letters:
                wrd[ch] = 0
            if ch in letters:
                wrd[ch] += 1
            
        # print('my dict : ', wrd)
        
        if len(wrd) == 5:
            N = min(wrd.values())
            return min(N,wrd['l']/2,wrd['o']/2 )
            
        else:
            return 0      
        
