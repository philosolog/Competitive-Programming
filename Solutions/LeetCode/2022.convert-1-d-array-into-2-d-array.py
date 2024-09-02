#
# @lc app=leetcode id=2022 lang=python3
#
# [2022] Convert 1D Array Into 2D Array
#

# @lc code=start
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        return [] if len(original) != m*n else [original[i*n:i*n+n] for i in range(m)]
# @lc code=end

