# leetCode n°884
# Difficulty : easy

class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        res = []
        s1L = s1.split(' ')
        s1D = dict()
        for w in s1L:
            if w not in s1D:
                s1D[w] = 0
            s1D[w] +=1        
        s2L = s2.split(' ')
        s2D = dict()
        for w in s2L:
            if w not in s2D:
                s2D[w] = 0
            s2D[w] +=1
                
        j = 0
        for i in range(len(s1L)):          
            if j < len(s2L):
                print(s1L[i], s2L[j])
                if s1L[i] != s2L[j]:
                    if s1L[j] in res:
                        res.remove(s1L[i])
                    elif s1D[s1L[i]] == 1 and s1L[i] not in s2D :
                        res.append(s1L[i])
                    if s2L[j] in res:
                        res.remove(s2L[j])
                    elif s2D[s2L[j]] == 1 and s2L[j] not in s1D:
                        res.append(s2L[j])               
            else:
                #print('sup : ',s1L[i],s1D[s1L[i]] )
                if s1L[i] in res:
                        res.remove(s1L[i])
                elif s1D[s1L[i]] == 1 and s1L[i] not in s2D:
                    res.append(s1L[i])
                
                
            j += 1      
        for k in range(j, len(s2L)):
            if s2L[k] in res:
                res.remove(s2L[k])
            elif s2D[s2L[k]] == 1 and s2L[k] not in s1D:
                res.append(s2L[k])
                
        #print('res : ', res)      
        return res
    
    
