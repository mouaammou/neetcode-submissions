# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #     # reverse and remove and reverse

    #     curr = head
    #     prev = None

    #     while curr:
    #         temp = curr.next
    #         curr.next = prev
    #         prev = curr

    #         curr = temp
        
    #     i = 1
    #     curr = prev
    #     if n == 1:
    #         prev = prev.next
    #     else:
    #         while curr:
    #             if i + 1 == n:
    #                 curr.next = curr.next.next
    #                 break
    #             i += 1
    #             curr = curr.next

    #     curr = prev
    #     prev_1 = None
    #     while curr:
    #         temp = curr.next
    #         curr.next = prev_1
    #         prev_1 = curr

    #         curr = temp
        
    #     return prev_1


    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy.next