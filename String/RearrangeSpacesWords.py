# leetCoe n°1592
# Difficulty : easy

class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        words = text.split()
        #print('words :', words)
        countSpace = 0
        for ch in text:
            if ch == ' ':
                countSpace += 1
        
        #print('count spaces : ', countSpace)
        countWords = len(words)
        #print('count words : ', countWords)
        
        if countSpace == 0:
            res = text
        else:
            if countWords == 1:
                sp = ' '*countSpace
                res = words[0] + sp
            else:
                div = countSpace /(countWords - 1)
                rest = countSpace %(countWords - 1)
                #print('div : ', div, rest)
                sp = ' '*div
                #print('sp : ', sp)
                res = sp.join(words)
                #print('res : ', res)
                if rest > 0:
                    addsp = ' '*rest
                    res += addsp
                
        #print('res : ', res)
        
        return res
    
    
# Runtime: 16 ms, faster than 75.91% of Python online submissions for Rearrange Spaces Between Words.
# Memory Usage: 13.5 MB, less than 74.45% of Python online submissions for Rearrange Spaces Between Words.  
      
