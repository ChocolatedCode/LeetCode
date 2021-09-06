# leetCode n°33
# Difficulty : medium

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        N = len(nums)
        leftIdx = 0
        rightIdx = N - 1
        # print(nums)
        
        while leftIdx <= rightIdx: 
            mid = (leftIdx + rightIdx) // 2
            # print('mid : ', mid)
            # print('left , right :', leftIdx, rightIdx)
        
            if nums[mid] == target:
                return mid
            elif nums[leftIdx] <= nums[mid]:
                if target <= nums[mid] and target >= nums[leftIdx]:
                    rightIdx = mid - 1
                else:
                    leftIdx = mid + 1
            else:
                if target >= nums[mid] and target <= nums[rightIdx]:
                    leftIdx = mid + 1
                else:
                    rightIdx = mid - 1
       
        return -1
            
            
