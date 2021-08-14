# Top100LikedQuestions
# n°2
# Difficulty : medium

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        res = l1
        rest = 0
        previous = None
        while l1 and l2:
            l1.val += l2.val + rest
            #print(l1.val)
            rest = int(l1.val/10)
            l1.val = l1.val%10
            previous = l1
            print(previous)
            print(res)
            l1 = l1.next
            l2 = l2.next
        
        if l1:
            while l1:
                l1.val += rest
                rest = int(l1.val/10)
                l1.val = l1.val%10
                previous = l1
                l1 = l1.next
                 
        elif l2 :
            previous.next = l2
            while l2:
                l2.val += rest
                rest = int(l2.val/10)
                l2.val = l2.val%10
                previous = l2
                l2 = l2.next
                
        if rest != 0:
            previous.next = ListNode(rest)
        
        return res
           
        
        
               
            
            
