# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        group_prev = dummy

        while True:
            kthnode = group_prev
            for _ in range(k):
                kthnode = kthnode.next
                if kthnode is None:
                    return dummy.next
            
            group_next = kthnode.next

            prev = group_next
            curr = group_prev.next

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr

                curr = temp
            
            tmp = group_prev.next
            group_prev.next = kthnode
            group_prev = tmp
        