# leetCode n°852
class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
    
   
        N = len(arr) # O(1) space
        # print('N :', N)
        if N < 3:
            return False
        
        # up
        i = 0
        while i < N -1 and arr[i+1] > arr[i]: # O(N) time
            i += 1
        # print('up : ', i, arr[i])
            
        
        return i
    
