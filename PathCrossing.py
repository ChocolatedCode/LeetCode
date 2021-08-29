class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        pathSum = [(0,0)]
        x, y = 0,0
        
        for Dir in path:
            if Dir == 'N':
                y += 1
            if Dir == 'E':
                x += 1
            if Dir == 'W':
                x -= 1
            if Dir == 'S':
                y -= 1
            # print(pathSum)
            # print(x,y)
            if (x,y) in pathSum:
                return True
            pathSum.append((x,y))
            
        return False
    
    
