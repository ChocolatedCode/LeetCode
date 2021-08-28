# leetCode n°459
# Difficulty : easy

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Second trial 
        # Generate a pattern : adding each round a new letter
        # Geenerate a list of length (s)
        # Conversion to a string to compare with the original string s
    
        N = len(s)
        for i in range(1,N/2+1):
            pattern = s[0:i]
            temp = len(s) //len(pattern)
            res = ''.join([pattern]*temp)
            #print('res : ', res)
           
            if res == s:
                return True

        return False
        
        """
        # First trial : ok, if length of string is relatively small
        # Split the string in 2,3,4... elements until you find the pattern
        # Otherwise return false
        i = 2
        if len(s)%2 != 0: 
            i+=1
            
        N = len(s)/i
        # print(N)
        sList = [s[j*N:j*N+N] for j in range(0, i)] # create a list with i elements
        print(sList)
        
        while len(sList[0]) >= 1:
            # print('first elem : ', sList[0]) # what is my pattern
            res = sList.count(sList[0])
            if res == i and res == len(sList): # how many pattern compared to the length of my string
                return True
            else: # separate the string s in i + 1 elements
                i += 1
                N = len(s)/i
                sList = [s[j*N:j*N+N] for j in range(0, i)]
                # print('N,new sList: ',N,sList)
                        
        return False
        """

        
