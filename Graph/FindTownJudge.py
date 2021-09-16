# leetCode n°997
# Difficulty : easy

class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        neighbours = dict()
        for a,b in trust:
            # print('a,b ', a,b)
            if a not in neighbours:
                #neighbours[a] = {}
                neighbours.setdefault(a, [])
                       
            neighbours[a].append(b) # multiples neighbours
        # print(neighbours)
        
        if len(neighbours) != n - 1:
            return -1 

        stopped = False
        for i in range(1, n+1):
            for vals in neighbours.values():
                if i not in vals:
                    stopped = True
                    break
            if stopped == False:
                print('person : ', i)
                return i
            
            stopped = False
        
        return -1
#Runtime: 813 ms, faster than 24.83% of Python online submissions for Find the Town Judge.
#Memory Usage: 18.3 MB, less than 99.67% of Python online submissions for Find the Town Judge.

        
        
        
        
        
            
