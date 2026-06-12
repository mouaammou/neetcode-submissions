# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr

            curr = temp
        
        slow.next = None

        list1 = head
        list2 = prev

        while list1 and list2:
            temp1 = list1.next
            temp2 = list2.next

            list1.next = list2
            list2.next = temp1

            list1 = temp1
            list2 = temp2

            