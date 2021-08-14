# Top100LikedQuestions
# n°160
# Difficulty : easy
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        countA = 0
        countB = 0
               
        nodeA = headA
        nodeB = headB
        while nodeA is not None:
            countA += 1
            nodeA = nodeA.next
            
        while nodeB is not None:
            countB += 1
            nodeB = nodeB.next
            
        if nodeA != nodeB :#different termination node
            return None
        
        count = countB - countA
        currentNodeA = headA
        currentNodeB = headB    
        print('count : ', count)
        if count < 0 :#A larger
            print('if')
            for i in range(count*-1):
                currentNodeA = currentNodeA.next
            
            while currentNodeA != currentNodeB:
                currentNodeA = currentNodeA.next
                currentNodeB = currentNodeB.next
                            
        else:
            print('else')
            for i in range(count):
                currentNodeB = currentNodeB.next
            
            while currentNodeA != currentNodeB:
                currentNodeA = currentNodeA.next
                currentNodeB = currentNodeB.next
        
        if (currentNodeA == currentNodeB):
            resNode = currentNodeA
        else:
            resNode = None
                
        print('res final : ', resNode)
        return resNode
