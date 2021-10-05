class Solution(object):
    # leetCode n°279
    # Difficulty : medium
    
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = []
    
        for i in range(1, n+ 1):
            if i*i <= n:
                memo.append(i*i)
            else:
                break

        # print(memo)
        nsq = [None]*(n+1)
        nsq[0] = 0

        for i in range(n+1):
            if nsq[i] != None:
                for num in memo:
                    #print(i+num)
                    if i + num <= n:
                        if nsq[i + num]:
                            #print(i+num, nsq[i]+1 , nsq[i + num])
                            nsq[i + num] = min(nsq[i]+1 , nsq[i + num])
                        else:
                            nsq[i + num] = nsq[i] + 1
                    #print('nsq :', nsq)

        #print('last : ', nsq)
    
        return nsq[n]

    
    
