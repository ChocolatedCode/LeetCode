# Top100LikedQuestions
# n°234
# Difficulty : easy

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#array
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        OrderList = []
        currentNode = head
        print(head)
        
    
        while currentNode is not None:
            OrderList.append(currentNode.val)
            currentNode = currentNode.next
            
        for n in range(len(OrderList)):
            print(OrderList[n], OrderList[-1-n])
            if OrderList[n] != OrderList[-1-n] :
                return False
            
        return True
		

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        currentNode = head
        originalList = []
        #print('currentNode : ', currentNode)
        
        previousNode = None
        nextNode = None
        
        while currentNode is not None:
            originalList.append(currentNode.val)
            nextNode = currentNode.next
            #print('nextTemp : ', nextNode)
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode

        #print('original list : ', originalList)
        rev = previousNode
        
        i = 0
        while rev.next is not None:
            if rev.val != originalList[i]:
                return False
            rev = rev.next
            i+=1
        
        return True
    
    
    
