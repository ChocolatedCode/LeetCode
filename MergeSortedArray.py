# LeetCode n°88
# Difficulty : easy

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        # is one of arrays empty, then return the other one
        if m == 0:
            nums1[:] = nums2[:] 
            return nums1
        elif n == 0:
            return nums1
        
        
        j = m-1 # idx for values for nums1 
        i = n-1 # idx to go through nums2
        k = m+n-1 # "add" new value in nums1
        
        # O (m+n) time 
        while i > -1 and j > -1: # while arrays have still "values"
            # print('i, j , k', i, j, k)
            if nums2[i] > nums1[j]:
                nums1[k] = nums2[i]
                i -= 1
            else:
                nums1[k] = nums1[j]
                j -= 1
            k -= 1
            # print('nums1 : ', nums1) # intermediate result
        
        # print(i, j , k)
        # print(nums1)
        
        # to add remaining values
        if i > -1: #if nums2 not "empty":
            # print('here', nums1[:i+1])
            nums1[:i+1] = nums2[:i+1]
        
        return nums1 # no additional space required
        
# Runtime: 24 ms, faster than 69.48% of Python online submissions for Merge Sorted Array.
# Memory Usage: 13.2 MB, less than 99.92% of Python online submissions for Merge Sorted Array.
                          
