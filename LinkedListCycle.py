# Top100LikedQuestions
# n°141
# Difficulty : easy

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head is None or head.next is None:
            return False
        
        firstNode = head
        currentNode = head.next.next
        
        while currentNode is not None and currentNode.next:
            #print(firstNode.val, currentNode.val)
            if firstNode == currentNode:
                return True
                       
            currentNode = currentNode.next.next
            firstNode = firstNode.next
            #print(currentNode)
                   
        return False
