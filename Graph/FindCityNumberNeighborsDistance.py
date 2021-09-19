# leetCode n°1334
# Difficulty : medium

class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        # distance = list(map(lambda i: list(map(lambda j: j, i)), edges))
        # init distance matrix
        distance=[[float('inf') for i in range(n)] for j in range(n)]
        
        # init diagonal values
        for i in range(n):
            for j in range(n):
                if i==j:
                    distance[i][j]=0
        #init with weights
        for a,b,c in edges:
            distance[a][b]=c
            distance[b][a]=c

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance[i][j] = min(distance[i][j],distance[i][k] + distance[k][j])

        maxi = float('Inf') # max cities
        res = []
        
        #find the cities
        maxC = float('Inf')
        for i in range(n):
            cities = 0
            for j in range(n):
                if distance[i][j] <= distanceThreshold and i!=j:
                    cities += 1
            if cities <= maxC:
                maxC = cities
                res.append([i, cities])
        
        # print('res : ', res)
        
        if len(res) == 1:
            return res[0][0]
        else:
            return res[-1][0]
# Runtime: 776 ms, faster than 32.61% of Python online submissions for Find the City With the Smallest Number of Neighbors at a Threshold Distance.
# Memory Usage: 14.6 MB, less than 52.17% of Python online submissions for Find the City With the Smallest Number of Neighbors at a Threshold Distance.
