# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        clone = ListNode(0, None)
        result = clone
        while list1 or list2:   
            if list1 == None:
                clone.next = list2 
                break
            elif list2 == None:
                clone.next = list1
                break

            if list1.val <= list2.val:
                clone.next = ListNode(list1.val)
                list1 = list1.next
            elif list1.val > list2.val:
                clone.next = ListNode(list2.val)
                list2 = list2.next
            
            clone = clone.next

        return result.next

        