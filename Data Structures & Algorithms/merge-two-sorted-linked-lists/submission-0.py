# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            mergedList = list1
            curr1 = list1.next
            curr2 = list2
            
        else:
            mergedList = list2
            curr1 = list1
            curr2 = list2.next
        prev = mergedList

        while curr1 or curr2:
            if not curr1:
                prev.next = curr2
                break
            if not curr2:
                prev.next = curr1
                break

            if curr1.val <= curr2.val:
                prev.next = curr1
                prev = curr1
                curr1 = curr1.next
            else:
                prev.next = curr2
                prev = curr2
                curr2 = curr2.next
        return mergedList
            

            

