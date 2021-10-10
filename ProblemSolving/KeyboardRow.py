# leetCode n°500
# Difficulty : easy

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        rows = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        
        #print('words list : ', words)
        res = []
        found = False
        i = 0
        while i < len(rows):
            #print('rows i :', rows[i])
            for wrd in words:
                #print('wrd : ', wrd)
                w = 0
                while w < len(wrd):
                    #print('w : ', wrd[w])
                    if wrd[w].lower() in rows[i]:
                        #print('here')
                        w+=1
                        continue
                    else:
                        break
                if w == len(wrd):
                    res.append(wrd)
                    #print('res : ')
            i+=1
        
        return res
                
                
# Runtime: 20 ms, faster than 53.56% of Python online submissions for Keyboard Row.
# Memory Usage: 13.5 MB, less than 68.16% of Python online submissions for Keyboard Row.         
