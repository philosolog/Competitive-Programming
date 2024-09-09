#
# @lc app=leetcode id=2326 lang=python3
#
# [2326] Spiral Matrix IV
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        mr, mc = 0, 1
        rl, rr = 0, m-1
        cl, cr = 0, n-1
        r, c = 0, 0

        while head:
            for i in range(cl, cr+1):
                if not head:
                    break
                matrix[rl][i] = head.val
                head = head.next

            rl += 1

            for i in range(rl, rr+1):
                if not head:
                    break
                matrix[i][cr] = head.val
                head = head.next

            cr -= 1

            for i in range(cr, cl-1, -1):
                if not head:
                    break
                matrix[rr][i] = head.val
                head = head.next

            rr -= 1

            for i in range(rr, rl-1, -1):
                if not head:
                    break
                matrix[i][cl] = head.val
                head = head.next

            cl += 1
        
        return matrix

# TODO: Go over the intuition for implementation
# @lc code=end

