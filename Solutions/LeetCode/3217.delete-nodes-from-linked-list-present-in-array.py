#
# @lc app=leetcode id=3217 lang=python3
#
# [3217] Delete Nodes From Linked List Present in Array
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        augmented_start = ListNode(-1, head)
        current = augmented_start

        while current.next != None:
            if current.next.val in nums_set:
                current.next = current.next.next
            else: # TODO: Condense repeated operations?
                current = current.next

        return augmented_start.next

# Note: Hash-set lookup is faster than list lookup
# TODO: Check the differences between my two solutions
            
# @lc code=end

