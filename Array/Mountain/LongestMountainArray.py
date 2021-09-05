# leetCode n°845
# Difficulty : medium

class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        N = len(arr)
        if N < 3:
            return 0
            
        firstIdx = 0
        i = 0
        lastIdx = 1
        maxL = 0
        peakIdx = 0
        
        ascend = True
        
        while firstIdx < N : 
            # print(firstIdx,i, lastIdx)
            if ascend :
                if arr[lastIdx] > arr[i]:
                    lastIdx += 1
                    if lastIdx == N:
                        break
                    i += 1
                else:
                    peakIdx = i                                                                                                                                         
                    if peakIdx == 0 or peakIdx == firstIdx:
                        firstIdx += 1
                        i = firstIdx
                        lastIdx = firstIdx + 1
                        if lastIdx == N:
                            break
                        ascend = True
                    else: 
                        ascend = False
                    # print(ascend)
            elif ascend == False:
                if arr[lastIdx] < arr[i]:
                    lastIdx += 1
                    if lastIdx == N:
                        maxL = max(maxL, len(arr[firstIdx:lastIdx]))
                        break
                    i += 1
                else:
                    peakIdx = max(arr[firstIdx:lastIdx])
                    # print('peakIdx', peakIdx)
                    # print('end',maxL, len(arr[firstIdx:lastIdx]))
                    if peakIdx != arr[i]:
                        maxL = max(maxL, len(arr[firstIdx:lastIdx]))
                    ascend = True
                    firstIdx += 1
                    lastIdx = firstIdx + 1
                    if lastIdx == N:
                        break
                    i = firstIdx
        
        return maxL
        
# Runtime: 160 ms, faster than 28.17% of Python online submissions for Longest Mountain in Array.
# Memory Usage: 14.7 MB, less than 12.68% of Python online submissions for Longest Mountain in Array.
        
