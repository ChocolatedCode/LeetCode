
# leetCode n°17 #Top100LikedQuestions
# Difficulty : medium 

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        phoneDict = {2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
        
        digit = [int(d) for d in digits] #convert input string to in
        
        res = [phoneDict[i] for i in digit]
        # print('res:', res)           
        return [''.join(val) for val in product(*res)]
        
        
# Runtime: 8 ms, faster than 99.54% of Python online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 13.5 MB, less than 68.59% of Python online submissions for Letter Combinations of a Phone Number.
