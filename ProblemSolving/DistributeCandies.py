# leetCode n°1103
# Difficulty : easy

class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        
        res = [0 for i in range(num_people)]
        i = 0
        turn = 0
        
        while candies > 0:
            if i < num_people:
                #print('res i', res[i], turn)
                temp = res[i]
                res[i] = min(turn*num_people + (i+1), candies)
                candies -= res[i]
                res[i] += temp
                #print('candies : ', candies)
                i += 1
            else:
                i = 0
                turn += 1
            #print('res : ', res)
            
        #print('result : ', res)
        
        return res
