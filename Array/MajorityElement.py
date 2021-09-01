# Top100LikedQuestions
# leetCode n°169
# Difficulty : easy

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nCollection = dict()
        
        for i in nums:
            if i not in nCollection:
                nCollection[i] = 0
            nCollection[i]+=1
        
        return  max(nCollection, key=nCollection.get)
		
		
#Improvement : Boyer-Moore Majority Voting Algorithm 
