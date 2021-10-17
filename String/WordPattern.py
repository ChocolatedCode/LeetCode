# leetCode n°290
# Difficulty : easy

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        if str(pattern) != s:
            if str(pattern) == s.replace(' ',''):
                return True
        sLst = s.split()
        pLst = [ch for ch in pattern]
        #print('sLst : ', sLst)
        myDict = dict()
        idx = 0
        N = len(sLst)
        visited = []
        for i in pLst:
            if idx <= N - 1:
                if i not in myDict:
                    if sLst[idx] not in visited:
                        myDict[i] = sLst[idx]
                    else:
                        return False
                visited.append(sLst[idx])
                idx += 1
            else:
                return False         
        #print('myDict : ', myDict)
        
        idx = -1
       
        for p in pLst: # check pattern with s
            idx +=1
            if myDict[p] != sLst[idx]:
                return False
                    
        if idx < len(sLst) - 1: # if it remains words in s
            return False
        return True
                
    
  
