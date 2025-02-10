# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        multiplier = 1
        while l1.next:
            num1 += l1.val * multiplier
            multiplier *= 10
            l1 = l1.next
        num1 += l1.val * multiplier
        num2 = 0
        multiplier = 1
        while l2.next:
            num2 += l2.val * multiplier
            multiplier *= 10
            l2 = l2.next
        num2 += l2.val * multiplier
        
        num3 = num1 + num2

        divisor = 10
        l = ListNode()
        head = l

        while num3 // divisor != 0:
            l.val = num3 % divisor
            l.next = ListNode()
            l = l.next
            num3 //= divisor

        l.val = num3 % divisor

        return head