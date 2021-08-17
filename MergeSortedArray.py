class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
              
        if m == 0:
            nums1[-1] = nums2[-1]
            return nums1
        elif n == 0:
            return nums1
          
        j = 0 #idx for values != 0 for nums1
        i = n #idx to go through nums2
        k = 0 #add new value in nums1
        
        while i < m+n and abs(j) < m+n : #idx for nums2
            print('comp : ', nums1[m-1-j], nums2[n-1-i],m-1-j, n-1-i)
            if nums1[m-1-j] < nums2[n-1-i]:
                #print('here', n-1-i)
                nums1[-1+k] = nums2[n-1-i]
                i += 1
            else:
                nums1[-1+k] = nums1[m-1-j]
                nums1[m-1-j] = 0
                if j > 0:
                    j += 1
                else:
                    j = 0
            k -= 1
            print(nums1)
                  
                         
        #print('nums1 res : ', nums1)
        
        return nums1
        
