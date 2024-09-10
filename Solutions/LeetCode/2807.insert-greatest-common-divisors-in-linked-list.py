#
# @lc app=leetcode id=2807 lang=python3
#
# [2807] Insert Greatest Common Divisors in Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        import math

        dummy = head

        while dummy.next:
            next_dummy = dummy.next
            gcd = ListNode(math.gcd(dummy.val, next_dummy.val))
            dummy.next = gcd
            gcd.next = next_dummy
            dummy = next_dummy

        return head
# @lc code=end

