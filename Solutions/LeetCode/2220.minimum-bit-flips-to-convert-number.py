#
# @lc app=leetcode id=2220 lang=python3
#
# [2220] Minimum Bit Flips to Convert Number
#

# @lc code=start
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        binary_goal, binary_start = str(bin(goal)).replace("0b", ""), str(bin(start)).replace("0b", "")
        length, differences = max(len(binary_goal), len(binary_start)), 0
        binary_goal, binary_start = "0"*(length-len(binary_goal)) + binary_goal, "0"*(length-len(binary_start)) + binary_start

        for index, digit in enumerate(binary_goal):
            differences += (digit != binary_start[index])

        return differences
# @lc code=end

