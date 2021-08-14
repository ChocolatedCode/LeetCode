# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode + sorted 
        :type l2: ListNode + sorted
        :rtype: ListNode
        """
        #start case : check if one list is empty -> return the other one
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:#which node will be the first one 
            if l1.val < l2.val: #node values comparison
                myList = ListNode(l1.val)
                head = myList #entire merged list
                l1 = l1.next
            else:
                myList = ListNode(l2.val)
                head = myList
                l2 = l2.next
                
            while l1 is not None and l2 is not None: #go through both list
                print(l1,l2)
                if l1.val < l2.val:
                    myList.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    myList.next = ListNode(l2.val)
                    l2 = l2.next
                #print(head)
                myList = myList.next
                
                
            #add remaining elements
            #first option : go through the remaining one 
            #while l1 is not None:
            #    myList.next = ListNode(l1.val)
            #    l1 = l1.next
            #    myList = myList.next
            #while l2 is not None:
            #    myList.next = ListNode(l2.val)
            #    l2 = l2.next
            #    myList = myList.next
            
            #2 option : optimisation : add the entire remaining part of the remaining list
            myList.next = l1 if l2 is None else l2

        
        return head
