# Top100LikedQuestions
# n°206
# Difficulty : easy

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Iterative with 3 pointers
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        currentNode = head
        # print('currentNode : ', currentNode)
        previousNode = None
        nextNode = None
        #nextTemp = ListNode(head)

        
        while currentNode is not None:
            nextNode = currentNode.next
            #print('nextTemp : ', nextNode)
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode

        return previousNode
            
