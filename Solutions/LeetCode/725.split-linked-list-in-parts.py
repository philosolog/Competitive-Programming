#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        partitions = []
        length = 0
        current = head

        while current:
            length += 1
            current = current.next

        minimum = length//k
        remainder = length%k
        current = head

        for partition in range(k):
            partitions.append(current)
            current_size = minimum + (partition < remainder)

            for _ in range(current_size - 1):
                if current:
                    current = current.next

            if current:
                next_part = current.next
                current.next = None
                current = next_part

        return partitions

# TODO: Fully optimize
# @lc code=end

