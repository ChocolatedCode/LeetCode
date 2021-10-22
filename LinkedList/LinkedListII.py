# leetCode n°142
# Difficulty : medium

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        firstNode = head
        scndNode = head
        
        while scndNode and scndNode.next :
            #print('first,scnd : ', firstNode.val,scndNode.val)
            firstNode = firstNode.next
            scndNode = scndNode.next.next
            
            if firstNode == scndNode :#cycle
                while head:
                    #print('head, first : ', head.val, firstNode.val)
                    if head == firstNode:
                        return head
                    head = head.next
                    firstNode = firstNode.next
        return None
        
        
# Runtime: 72 ms, faster than 15.35% of Python online submissions for Linked List Cycle II.
# Memory Usage: 19.7 MB, less than 57.85% of Python online submissions for Linked List Cycle II.
        

        
                   
