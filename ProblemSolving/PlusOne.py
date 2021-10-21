# leetCode n°66
# Difficulty : easy

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        N = len(digits)
        
        for i in range(N-1,-1,-1):#reverse reading
            print(digits[i])
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
            print('dig : ', digits)
        return [1] + digits
        
# Runtime: 36 ms, faster than 11.88% of Python online submissions for Plus One.
# Memory Usage: 13.4 MB, less than 70.27% of Python online submissions for Plus One.
