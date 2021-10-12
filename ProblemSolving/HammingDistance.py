# leetCode n°461
# Difficulty : easy

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bx = bin(x)
        #print('x bin :', bx)
        by = bin(y)
        #print('y bin :', by)
        countDiff = 0
        
        i = len(bx)-1
        j = len(by)-1
        
        while i >= 2 and j >= 2:
            if bx[i] != by[j]:
                countDiff += 1
            i -= 1
            j -= 1
            
        #print('count : ', countDiff)
        #print('i,j :', i,j)
        while i >= 2:
            #print('bx i ', bx[i])
            if int(bx[i]) == 1:
                countDiff += 1
            i -= 1
        #print('after i : ', countDiff)
        while j >= 2:
            #print('by i ', by[j])
            if int(by[j]) == 1:
                countDiff += 1
            j -= 1
        #print('after j : ', countDiff)
        
        return countDiff
        
            
            
