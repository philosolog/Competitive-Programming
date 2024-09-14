#
# @lc app=leetcode id=2419 lang=python3
#
# [2419] Longest Subarray With Maximum Bitwise AND
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maximum_result = 0
        result = 0
        maximum = max(nums)

        for num in nums:
            if num == maximum:
                result += 1
                maximum_result = max(maximum_result, result)
            else:
                result = 0

        return max(maximum_result, result)

# TODO: Find how I can optimize the runtime & memory even more
# @lc code=end

