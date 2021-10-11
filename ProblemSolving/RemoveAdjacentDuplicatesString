# leetCode n°1047
# Difficulty : easy

class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        mystack = []
        
        for ch in s:
            #print('ch : ', ch)
            if not mystack: #add element if empty stack
                mystack.append(ch)
            elif mystack[-1] == ch:#duplicate ajdacent element -> remove it
                mystack.pop()
            else:
                mystack.append(ch)
        
        #print('res : ', mystack)
        return ''.join(mystack)
    
# Runtime: 80 ms, faster than 77.20% of Python online submissions for Remove All Adjacent Duplicates In String.
# Memory Usage: 14.7 MB, less than 41.09% of Python online submissions for Remove All Adjacent Duplicates In String.
            
    
    
