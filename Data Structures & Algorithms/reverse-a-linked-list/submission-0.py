# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = []

        curr = head
        while curr:
            tmp.append(curr.val)
            curr = curr.next
        
        curr = head
        for i in range(len(tmp) - 1, -1, -1):
            curr.val = tmp[i]
            curr = curr.next
           
        
        return head
        