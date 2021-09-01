# Top100LikedQuestions
# n°11
# Difficulty : medium

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        N = len(height)
        firstIdx = 0
        secondIdx = - 1
        area = 0
        
        while firstIdx < N+secondIdx:
            print(firstIdx, secondIdx) 
            temp = min(height[firstIdx], height[secondIdx])*(N+secondIdx - firstIdx)
            area = max(area, min(height[firstIdx], height[secondIdx])*(N+secondIdx - firstIdx))
            
            if height[firstIdx] > height[secondIdx]:
                secondIdx -=1
                
            else:
                firstIdx +=1
                        
        return area
    
    
                
            
        
