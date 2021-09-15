# leetCode n°1791
# Difficulty : easy

class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        #create adjacency list G = (V, E)
        neighbours = dict()
        for a,b in edges:
            # print('a,b ', a,b)
            if a not in neighbours:
                #neighbours[a] = {}
                neighbours.setdefault(a, [])
            if b not in neighbours:
                #neighbours[b] = {}
                neighbours.setdefault(b, [])
                
            neighbours[a].append(b) # multiples neighbours
            neighbours[b].append(a) # bidirectional
        
        # print('neigh :', neighbours)
        
        for vtx in neighbours:
            # print(neighbours[vtx])
            if len(neighbours[vtx]) != 1:
                return vtx
        # Runtime: 1040 ms, faster than 16.35% of Python online submissions for Find Center of Star Graph.
        # Memory Usage: 55.7 MB, less than 6.39% of Python online submissions for Find Center of Star Graph.
           
