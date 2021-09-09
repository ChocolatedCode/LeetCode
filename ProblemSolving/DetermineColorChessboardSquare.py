# leetCode n°1812
# Difficulty : easy

class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        
        letDict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
        let1 = str(coordinates[0])
        let2 = int(coordinates[1])
        # print(let1, let2)
        # print(letDict[let1]%2, let2%2)
        if letDict[let1]%2 != 0 :
            if let2%2 == 0:
                return True
            else:
                return False
        else:
            if let2%2 == 0:
                return False
            else:
                return True
              
# Runtime: 12 ms
# Memory Usage: 13.4 MB
            
