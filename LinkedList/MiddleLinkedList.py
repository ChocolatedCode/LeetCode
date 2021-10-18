# leetCode n°876
# Difficulty : easy

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        current = head
        res = head
        count = 0
      
        while current:
            #print('current : ', current)
            count += 1
            current = current.next
        
        c = 0
        while c != count//2:
            res = res.next
            c += 1
        
        return res
                
 
            
# Runtime: 26 ms, faster than 26.41% of Python online submissions for Middle of the Linked List.
# Memory Usage: 13.3 MB, less than 96.59% of Python online submissions for Middle of the Linked List.


