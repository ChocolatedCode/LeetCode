# leetCode n°941
# Difficulty : easy

class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
       
        
        N = len(arr)
        # print('N :', N)
        if N < 3:
            return False
        
        # up
        i = 0
        while i < N -1:
            if arr[i+1] <= arr[i]:
                break
            i += 1
        # print('up : ', i, arr[i])
            
        # find peak
        if i == 0 or i == N - 1:
            return False
        
        # down
        while i < N -1 :
            if arr[i+1] >= arr[i]:
                break
            i += 1
        # print('down : ', i, arr[i])
        # if we are at the end of the mountain
        if i == N-1:
            return True
        
        return False
# Runtime: 160 ms, faster than 94.20% of Python online submissions for Valid Mountain Array.
# Memory Usage: 14.7 MB, less than 75.96% of Python online submissions for Valid Mountain Array.
    
    
