# Top100LikedQuestions
# n°338
# Difficulty : easy
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        oneArr = []
        for i in range(0,n+1) :
            convBits = "{0:b}".format(i)
            count = 0
            for ch in convBits:
                if ch == '1':
                    count+=1
            oneArr.append(count)
            
        return oneArr
            
            
        
        
        
