# leetCode n°1029
# Difficulty : medium

class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        costsSort = sorted(costs ,key = lambda costs : float(costs[0])-costs[1], reverse=True)
        print('costSort:', costsSort)
                
        total = 0
        Na = 0
        Nb = 0
        N = len(costs)
         
        for a,b in costsSort:
            print('a,b:', a-b)
            if Nb < N/2:
                total += b
                Nb += 1
                print('b')
    
            else: 
                total += a
                Na += 1
                print('a')
            
            # print(Na,Nb)
                       
        # print('total : ', total)
        return total

      
# Runtime: 24 ms, faster than 80.73% of Python online submissions for Two City Scheduling.
#Memory Usage: 13.3 MB, less than 85.32% of Python online submissions for Two City Scheduling.   
