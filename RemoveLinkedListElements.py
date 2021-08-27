# leetCode n°203
# Difficulty : easy

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """       
        current = head
        previous = None
           
        while current:
            if current.val != val:
                previous = current
            else:
                if current == head:
                    head = head.next
                    previous = current.next
                else:
                    previous.next = current.next
                                
            current = current.next
            # print('current:',current)
                        
        # print('head : ',head)
        
        return head
        
        
        
# Runtime: 59 ms, faster than 81.08% of Python online submissions for Remove Linked List Elements.
# Memory Usage: 20.2 MB, less than 56.61% of Python online submissions for Remove Linked List Elements.
