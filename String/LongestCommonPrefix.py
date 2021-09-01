class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        #lengths of each strings
        Strmax = 0
        Strmin = 100
        idxmax = 0
        i = 0
        for st in strs:
            if len(st) == 0:
                return ''
            else:
                if len(st) > Strmax:
                    Strmax = len(st)
                    idxmax = i
                elif len(st) < Strmin:
                    Strmin = len(st)
                    
            i += 1
                    
                
        if strs == ['']:
            return ''
        if len(strs) == 1:
            return strs[0]
     
        prefixStr = ''
        i = 0
       
        NotFound = False
        while NotFound is False and i < Strmin:
            print(i, idxmax)
            prefixStr += str(strs[idxmax][i])
            for st in strs:
                if prefixStr not in st[:i+1]:
                    NotFound = True
                    i -= 1
                    prefixStr = prefixStr[:i+1]
                    print('prefix ', prefixStr)
                    break
                
            if NotFound is False:
                i += 1
        print('i : ', i)
        return prefixStr
