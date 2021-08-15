# LeetCode n°83
# Difficulty : easy

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
     
        currentNode = head # reference pointing the head of the listNode
        # previousVal = None # no need to remember previous element
        
        while head and head.next: # O(n) time complexity
            # print('prev : ', previousVal)
            # previousVal == head.val
            if head.val == head.next.val: # compare currentNode value with the nextNode
                head.next = head.next.next # modify the listNode 
            else:
                head = head.next # if values are different, go directly to nextNode
            
        # print('head : ', head)
        # print('current : ', currentNode)
        return currentNode # O(n) space complexity
    
# Runtime : 24 ms, faster than 94.22% of Python online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 13.5 MB, less than 67.70% of Python online submissions for Remove Duplicates from Sorted List.
    
    


    
        
