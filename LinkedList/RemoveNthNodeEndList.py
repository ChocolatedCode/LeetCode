# leetCode n°19
# Difficulty : Medium

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
        current = head
        removeNode = head
        N  = 0
        while current:
            current = current.next
            N += 1
        
        # print('N, n :', N, n)
        #if N == n and n == 1 :
        #    return None 
        if N - n == 0:
            return removeNode.next
        
        i = 1
        while i != N - n:
            removeNode = removeNode.next
            i += 1
            
        # print(removeNode)
        removeNode.next = removeNode.next.next
        
        return head
        
# Runtime: 20 ms, faster than 70.32% of Python online submissions for Remove Nth Node From End of List.
# Memory Usage: 13.6 MB, less than 5.09% of Python online submissions for Remove Nth Node From End of List.
        
        
        
