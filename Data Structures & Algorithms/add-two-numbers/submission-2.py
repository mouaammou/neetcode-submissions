# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i = 1
        curr1 = l1
        val1 = 0
        while curr1:
            val1 += i * curr1.val
            i *= 10
            curr1 = curr1.next

        i = 1
        curr2 = l2
        val2 = 0
        while curr2:
            val2 += i * curr2.val
            i *= 10
            curr2 = curr2.next

        sum = (val1 + val2)

        dummy = ListNode()
        head = dummy
        while sum >= 0:
            # print(sum % 10)
            new_node = ListNode(sum % 10)
            dummy.next = new_node
            dummy = new_node
            sum //=10
            if sum == 0:
                break

        return head.next