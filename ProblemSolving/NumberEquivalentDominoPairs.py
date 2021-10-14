# leetCode n°1128
# difficulty : easy

class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        
        
        myDict = dict()
        
        for d in range(len(dominoes)):
            a,b = sorted(dominoes[d])
            if (a,b) not in myDict:
                myDict[(a,b)] = 0
                
            myDict[(a,b)] += 1
            
        print('my dict : ', myDict)
        maxpairs = 0
        for key,val in myDict.items():
            print('key , value : ', key,val)
            if val >= 2:
                maxpairs += (val * (val-1))//2 #combination
                
        return maxpairs
    
# Runtime: 196 ms, faster than 94.57% of Python online submissions for Number of Equivalent Domino Pairs.
# Memory Usage: 25.6 MB, less than 13.04% of Python online submissions for Number of Equivalent Domino Pairs.
