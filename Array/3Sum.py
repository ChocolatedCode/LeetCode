class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Naïve implementation
        # TLE 
        i = 0
        j = 1
        k = 2
        N = len(nums)
        res = []
        
        while i <= N - 3 :
            while j <= N - 2:
                while k <= N - 1:
                    # print(i,j,k)
                    if i != j and i!=k and j != k:
                        if nums[i] + nums[j] + nums[k] == 0:
                            temp = [nums[i],nums[j],nums[k]]
                            temp = sorted(temp)
                            if temp not in res:
                                res.append(temp)
                    
                    k+= 1
            
                j += 1
                k = 2
            
            j = 1
            k = 2
            i += 1
        
        return res
      
      # 2nd implementation
      N = len(nums)
        nums.sort()
        res = []
        for i in range(N - 2):
            first = nums[i]
            scnd = i + 1
            third = N - 1
            # print(first, scnd, third)
            
            while scnd < third:
                if first + nums[scnd] + nums[third] == 0:
                    if [first, nums[scnd], nums[third]] not in res:
                        res.append([first, nums[scnd], nums[third]])
                    scnd += 1
                    third -= 1
                elif first + nums[scnd] + nums[third] > 0:
                    third -= 1
                else:
                    scnd += 1
        
        return res    
    
                     
