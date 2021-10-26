# leetCode n°79
# Difficulty : medium

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
                
        def searchNextLetter(w,l,c):
            
            #print('w : ', w)
            #print('row,col :', l,c,word[w],board[l][c])
            #print('visited: ', visited)
            
            if w == len(word) :#len(board) - 1:#all letters found
                return True
            if l < 0 or l >= len(board) or c < 0 or c >= len(board[0]) or word[w] != board[l][c] or (l,c) in visited:#indices limits
                #print('here')
                return False
            
            visited.append((l,c))
            up = searchNextLetter(w+1,l-1,c)
            right = searchNextLetter(w+1,l,c+1)
            down = searchNextLetter(w+1,l+1,c)
            left = searchNextLetter(w+1,l,c-1)
            visited.remove((l,c))
            return up or right or down or left
                                      
        w = 0
        l = 0
        c = 0
        
        m = len(board)
        n = len(board[0])
        #print('m,n',m,n)
        visited = []
        for l in range(m):
            for c in range(n):
                #print('search position')
                if board[l][c] == word[0]:
                    #print('found : ', l,c)
                    if searchNextLetter(0,l,c):
                        return True
        return False
    
    
