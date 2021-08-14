# Top100LikedQuestions
# n°19
# Difficulty : medium
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        totalNodes = ListNode(head) # to count total number of nodes
        total = 1 #already first node in the listNode
        original  = None
        print(totalNodes)
        
        while totalNodes: # go through list to count
            total += 1
            totalNodes = totalNodes.next
            
        
        print('total : ', total)
        currentNode = head
        idx = 0
        previousNode = ListNode(None)
        
        while idx < total - n:
            print('curr :', currentNode)
            previousNode = currentNode
            currentNode = currentNode.next
        
        previousNode.next = currentNode.next          
                
        print('previous :', previousNode)
        print('currentNode : ', currentNode)
        print('head : ', head)
        
        return previousNode
