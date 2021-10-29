# leetCode n°792
# Difficulty : medium

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        N = len(nums)
        #nums = sorted(nums)
        
        count = 0
        prev = 0
        firstIdx = 0
        lastIdx = 1
        #subProd = []
        
        if nums.count(nums[0]) == N and nums[0] < k:
            return N*(N+1)/2
        while firstIdx <= N - 1:
            #tmp = []
            #print('firstIdx : ', nums[firstIdx], firstIdx)
            if nums[firstIdx] < k :
                count += 1
                
            currentProd = nums[firstIdx]
            #subProd.append(currentProd)
            #tmp.append(currentProd)
            
            while lastIdx <= N - 1:
                #print(nums[lastIdx],currentProd)
                if lastIdx != firstIdx:
                    currentProd *= nums[lastIdx]
                    if currentProd < k :
                        #print('curr : ', currentProd)
                        count += 1
                        #tmp.append(nums[lastIdx])
                        #subProd.append(tmp)
                    
                        lastIdx += 1
                    else:
                        break
                        
            #tmp = []
                
                
            #print('count : ', count)
            
            
            if firstIdx + 1 <= N-1:
                #if nums[firstIdx + 1] == nums[firstIdx]:
                #    firstIdx += 2
                #else:
                firstIdx += 1
            else:
                break
            lastIdx = firstIdx+1
            #prev = currentProd
            
            #print('new idx : ', firstIdx, lastIdx)
        
        #print('len res : ', len(subProd))
        #print('res : ', subProd)
    
        return count
                
                
        
       
    
            
