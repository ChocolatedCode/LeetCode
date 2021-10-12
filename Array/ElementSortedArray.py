# leetCode n°1287
# Difficulty : easy


class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        myDict = {}
        for n in arr:
            if n not in myDict:
                myDict[n] = 0
            myDict[n] += 1
        
        #print('my dict : ', myDict)
        maxValue = max(myDict, key=myDict.get)
        #print('max value : ', maxValue)
        
        return maxValue
            
# Runtime: 127 ms, faster than 21.05% of Python online submissions for Element Appearing More Than 25% In Sorted Array.
# Memory Usage: 15.3 MB, less than 21.93% of Python online submissions for Element Appearing More Than 25% In Sorted Array.
